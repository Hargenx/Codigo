import React, { useCallback, useEffect, useMemo, useRef, useState } from "react";
import {
  View,
  Text,
  TextInput,
  FlatList,
  Pressable,
  Platform,
  StyleSheet,
  ActivityIndicator,
  Alert,
} from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { SafeAreaProvider, SafeAreaView } from "react-native-safe-area-context";
import DateTimePicker, {
  DateTimePickerEvent,
} from "@react-native-community/datetimepicker";

/**
 * Expo demo of AsyncStorage + Date Picker + simple log.
 * Best practices highlighted:
 *  - namespaced keys
 *  - typed (TS) storage helpers
 *  - safe JSON (parse/serialize) + error handling
 *  - idempotent load on mount and explicit refresh/clear
 *  - minimal, accessible UI
 */

// 1) Types & Keys -------------------------------------------------------------

type Profile = { name: string; note: string };

type LogEntry = { id: string; ts: string; message: string };

const STORAGE_KEYS = {
  PROFILE: "demo:profile:v1",
  SELECTED_DATE_ISO: "demo:selectedDateISO:v1",
  LOG: "demo:log:v1",
} as const;

// 2) Safe JSON helpers --------------------------------------------------------

function safeStringify<T>(value: T): string {
  try {
    return JSON.stringify(value);
  } catch (e) {
    // As a fallback, attempt to stringify errors
    return `"__SERIALIZATION_ERROR__:${String(e)}"`;
  }
}

function safeParse<T>(raw: string | null, fallback: T): T {
  if (raw == null) return fallback;
  try {
    return JSON.parse(raw) as T;
  } catch {
    return fallback;
  }
}

// 3) Reusable AsyncStorage hook (typed) --------------------------------------

function useAsyncStorageItem<T>(key: string, initial: T) {
  const initialRef = useRef(initial);
  const [value, setValue] = useState<T>(initialRef.current as T);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<Error | null>(null);

  const refresh = useCallback(async () => {
    setLoading(true);
    try {
      const raw = await AsyncStorage.getItem(key);
      setValue(safeParse<T>(raw, initialRef.current as T));
      setError(null);
    } catch (e) {
      setError(e as Error);
    } finally {
      setLoading(false);
    }
  }, [key]);

  const save = useCallback(
    async (next: T | ((prev: T) => T)) => {
      setValue((prev) => {
        const out = typeof next === "function" ? (next as (p: T) => T)(prev) : next;
        AsyncStorage.setItem(key, safeStringify(out)).catch((e) => setError(e as Error));
        return out;
      });
    },
    [key]
  );

  const clear = useCallback(async () => {
    try {
      await AsyncStorage.removeItem(key);
      setValue(initialRef.current as T);
      setError(null);
    } catch (e) {
      setError(e as Error);
    }
  }, [key]);

  useEffect(() => {
    refresh();
  }, [refresh]);

  return { value, save, clear, refresh, loading, error } as const;
}

// 4) Small utilities ----------------------------------------------------------

function nowISO() {
  return new Date().toISOString();
}

function formatDateBR(iso: string | null | undefined): string {
  if (!iso) return "—";
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return "—";
  return d.toLocaleDateString("pt-BR", { timeZone: "UTC" });
}

function uid() {
  return Math.random().toString(36).slice(2, 10);
}

// 5) Main App -----------------------------------------------------------------

export default function App() {
  // Profile (name + note)
  const profile = useAsyncStorageItem<Profile>(STORAGE_KEYS.PROFILE, {
    name: "",
    note: "",
  });

  // Selected date (ISO)
  const initialDateISO = useRef(new Date().toISOString()).current;
  const selectedDate = useAsyncStorageItem<string>(
    STORAGE_KEYS.SELECTED_DATE_ISO,
    initialDateISO
  );

  // Log list
  const log = useAsyncStorageItem<LogEntry[]>(STORAGE_KEYS.LOG, []);

  const addLog = useCallback(
    (message: string) =>
      log.save((prev) => [
        { id: uid(), ts: nowISO(), message },
        ...prev,
      ].slice(0, 200)),
    [log]
  );

  const [showPicker, setShowPicker] = useState(false);

  const onChangeDate = useCallback(
    (e: DateTimePickerEvent, date?: Date) => {
      if (Platform.OS === "android") setShowPicker(false);
      const type = (e as any)?.type as string | undefined; // 'set' | 'dismissed' on Android
      if (date && (type === undefined || type === "set")) {
        const iso = date.toISOString();
        selectedDate.save(iso);
        addLog(`Data selecionada: ${formatDateBR(iso)} (ISO: ${iso.slice(0, 10)})`);
      } else if (type === "dismissed") {
        addLog("Seleção de data cancelada");
      }
    },
    [selectedDate, addLog]
  );

  const saveProfile = useCallback(() => {
    // Validate minimal fields
    const name = profile.value.name.trim();
    if (!name) {
      Alert.alert("Validação", "Informe um nome antes de salvar.");
      return;
    }
    profile.save({ ...profile.value, name });
    addLog(`Perfil salvo: ${name}`);
  }, [profile, addLog]);

  const clearAll = useCallback(async () => {
    await Promise.all([
      profile.clear(),
      selectedDate.clear(),
      log.clear(),
    ]);
    addLog("Storage limpo (perfil, data, log)");
  }, [profile, selectedDate, log, addLog]);

  const anyLoading = profile.loading || selectedDate.loading || log.loading;

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.safe}>
      <View style={styles.container}>
        <Text style={styles.h1}>AsyncStorage + DatePicker + Log</Text>

        {anyLoading ? (
          <View style={styles.rowCenter}>
            <ActivityIndicator />
            <Text style={{ marginLeft: 8 }}>Carregando…</Text>
          </View>
        ) : null}

        {/* PROFILE SECTION */}
        <Section title="Perfil">
          <LabeledInput
            label="Nome"
            value={profile.value.name}
            onChangeText={(t) => profile.save({ ...profile.value, name: t })}
            placeholder="Seu nome"
            testID="input-name"
          />
          <LabeledInput
            label="Anotações"
            value={profile.value.note}
            onChangeText={(t) => profile.save({ ...profile.value, note: t })}
            placeholder="Observações (opcional)"
            multiline
            numberOfLines={3}
            testID="input-note"
          />
          <View style={styles.row}>
            <Btn title="Salvar perfil" onPress={saveProfile} />
            <Btn title="Recarregar" variant="ghost" onPress={profile.refresh} />
          </View>
        </Section>

        {/* DATE SECTION */}
        <Section title="Data selecionada">
          <Text style={styles.mono}>
            {formatDateBR(selectedDate.value)} — ISO: {selectedDate.value.slice(0, 10)}
          </Text>
          <View style={styles.row}>
            <Btn title="Escolher data" onPress={() => setShowPicker(true)} />
            <Btn title="Hoje" variant="ghost" onPress={() => onChangeDate({} as any, new Date())} />
          </View>
          {showPicker && (
            <DateTimePicker
              value={new Date(selectedDate.value)}
              mode="date"
              display={Platform.OS === "ios" ? "inline" : "calendar"}
              onChange={onChangeDate}
              style={{ alignSelf: "stretch" }}
            />
          )}
        </Section>

        {/* ACTIONS */}
        <Section title="Ações do Storage">
          <View style={styles.row}>
            <Btn title="Recarregar tudo" variant="ghost" onPress={() => { profile.refresh(); selectedDate.refresh(); log.refresh(); addLog("Refresh manual executado"); }} />
            <Btn title="Limpar tudo" variant="danger" onPress={clearAll} />
          </View>
        </Section>

        {/* LOG SECTION */}
        <Section title={`Log (${log.value.length})`}>
          <View style={[styles.row, { marginBottom: 8 }]}>
            <Btn title="Adicionar linha de teste" variant="ghost" onPress={() => addLog("Linha de teste adicionada")}/>
            <Btn title="Limpar log" variant="danger" onPress={log.clear} />
          </View>

          <FlatList
            data={log.value}
            keyExtractor={(item) => item.id}
            style={{ maxHeight: 220 }}
            contentContainerStyle={{ paddingBottom: 8 }}
            renderItem={({ item }) => (
              <View style={styles.logItem}>
                <Text style={styles.logTs}>{new Date(item.ts).toLocaleTimeString("pt-BR")}</Text>
                <Text style={styles.logMsg}>{item.message}</Text>
              </View>
            )}
            ListEmptyComponent={<Text style={{ opacity: 0.6 }}>Sem eventos ainda.</Text>}
          />
        </Section>

        {/* ERROR SURFACE */}
        {(profile.error || selectedDate.error || log.error) && (
          <View style={styles.errorBox}>
            <Text style={styles.errorTitle}>Erros</Text>
            {profile.error && <Text style={styles.errorText}>Perfil: {String(profile.error.message || profile.error)}</Text>}
            {selectedDate.error && <Text style={styles.errorText}>Data: {String(selectedDate.error.message || selectedDate.error)}</Text>}
            {log.error && <Text style={styles.errorText}>Log: {String(log.error.message || log.error)}</Text>}
          </View>
        )}
      </View>
    </SafeAreaView>
  )}
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

// 6) UI helpers ---------------------------------------------------------------

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <View style={styles.section}>
      <Text style={styles.h2}>{title}</Text>
      {children}
    </View>
  );
}

function Btn({
  title,
  onPress,
  variant = "solid",
}: {
  title: string;
  onPress: () => void;
  variant?: "solid" | "ghost" | "danger";
}) {
  return (
    <Pressable
      accessibilityRole="button"
      onPress={onPress}
      style={({ pressed }) => [
        styles.btn,
        variant === "ghost" && styles.btnGhost,
        variant === "danger" && styles.btnDanger,
        pressed && { opacity: 0.75 },
      ]}
    >
      <Text style={[styles.btnText, variant !== "solid" && styles.btnTextGhost]}>{title}</Text>
    </Pressable>
  );
}

function LabeledInput(props: React.ComponentProps<typeof TextInput> & { label: string }) {
  const { label, style, ...rest } = props;
  return (
    <View style={{ marginBottom: 12 }}>
      <Text style={styles.label}>{label}</Text>
      <TextInput
        {...rest}
        style={[styles.input, style]}
        placeholderTextColor="#888"
      />
    </View>
  );
}

// 7) Styles -------------------------------------------------------------------

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: "#0f172a" }, // slate-900
  container: {
    flex: 1,
    padding: 16,
    gap: 16,
  },
  section: {
    backgroundColor: "#111827", // gray-900
    borderRadius: 14,
    padding: 14,
    borderWidth: StyleSheet.hairlineWidth,
    borderColor: "#1f2937", // gray-800
  },
  h1: { fontSize: 20, fontWeight: "700", color: "#e5e7eb" },
  h2: { fontSize: 16, fontWeight: "700", color: "#d1d5db", marginBottom: 10 },
  label: { color: "#9ca3af", marginBottom: 6 },
  input: {
    backgroundColor: "#0b1220",
    color: "#e5e7eb",
    paddingHorizontal: 12,
    paddingVertical: 10,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: "#1f2937",
  },
  mono: { fontFamily: Platform.select({ ios: "Menlo", android: "monospace" }) as any, color: "#cbd5e1" },
  row: { flexDirection: "row", gap: 10, alignItems: "center" },
  rowCenter: { flexDirection: "row", alignItems: "center" },
  btn: {
    backgroundColor: "#2563eb",
    paddingHorizontal: 12,
    paddingVertical: 10,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: "#1f2937",
  },
  btnGhost: { backgroundColor: "transparent", borderColor: "#374151" },
  btnDanger: { backgroundColor: "#dc2626", borderColor: "#7f1d1d" },
  btnText: { color: "#f8fafc", fontWeight: "700" },
  btnTextGhost: { color: "#e5e7eb" },
  logItem: {
    paddingVertical: 8,
    borderBottomWidth: StyleSheet.hairlineWidth,
    borderBottomColor: "#1f2937",
  },
  logTs: { fontSize: 12, color: "#94a3b8", marginBottom: 2 },
  logMsg: { color: "#e5e7eb" },
  errorBox: {
    marginTop: 8,
    padding: 10,
    backgroundColor: "#7f1d1d",
    borderRadius: 10,
  },
  errorTitle: { color: "#fecaca", fontWeight: "700", marginBottom: 4 },
  errorText: { color: "#fee2e2" },
});
