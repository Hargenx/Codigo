import React, { useRef } from "react";
import { View, Text, Button, FlatList, StyleSheet } from "react-native";
import { SafeAreaProvider, SafeAreaView } from "react-native-safe-area-context";
import AsyncStorage from "@react-native-async-storage/async-storage";

import { KEYS } from "./src/storage/keys";
import { useStoredState } from "./src/storage/useStoredState";
import { useLog } from "./src/log/useLog";
import { FormField } from "./src/components/FormField";
import { DateField } from "./src/components/DateField";

export default function App() {
  const [name, setName] = useStoredState<string>(KEYS.name, "");
  const initialISO = useRef(new Date().toISOString()).current;
  const [dateISO, setDateISO] = useStoredState<string>(KEYS.date, initialISO);
  const log = useLog(KEYS.log, 100);

  return (
    <SafeAreaProvider>
      <SafeAreaView style={s.safe}>
        <View style={s.card}>
          <Text style={s.h1}>Storage + Date + Log (Modular)</Text>

          <FormField
            label="Nome"
            value={name}
            onChangeText={setName}
            placeholder="Seu nome"
          />
          <Button
            title="Salvar perfil"
            onPress={() => log.add(`Perfil salvo: ${name || "(vazio)"}`)}
          />

          <View style={{ height: 10 }} />
          <DateField
            valueISO={dateISO}
            onChangeISO={(iso) => {
              setDateISO(iso);
              log.add(
                `Data: ${new Date(iso).toLocaleDateString(
                  "pt-BR"
                )} (ISO ${iso.slice(0, 10)})`
              );
            }}
          />

          <View style={s.row}>
            <Button
              title="Hoje"
              onPress={() => setDateISO(new Date().toISOString())}
            />
            <Button
              title="Limpar tudo"
              color="#b91c1c"
              onPress={async () => {
                await AsyncStorage.multiRemove([
                  KEYS.name,
                  KEYS.date,
                  KEYS.log,
                ]);
                setName("");
                setDateISO(initialISO);
                log.clear();
                log.add("Storage limpo");
              }}
            />
          </View>

          <Text style={[s.h2, { marginTop: 12 }]}>Log</Text>
          <FlatList
            data={log.entries}
            keyExtractor={(item, idx) => `${idx}`}
            style={{ maxHeight: 180 }}
            renderItem={({ item }) => <Text style={s.log}>{item}</Text>}
            ListEmptyComponent={<Text style={s.muted}>Sem eventos.</Text>}
          />
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

const s = StyleSheet.create({
  safe: { flex: 1, backgroundColor: "#0b1220", padding: 12 },
  card: { backgroundColor: "#111827", borderRadius: 12, padding: 12, gap: 8 },
  h1: { color: "#e5e7eb", fontSize: 18, fontWeight: "700" },
  h2: { color: "#d1d5db", fontSize: 16, fontWeight: "700" },
  muted: { color: "#9ca3af" },
  row: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    gap: 8,
    marginTop: 8,
  },
  log: {
    color: "#e5e7eb",
    paddingVertical: 4,
    borderBottomWidth: StyleSheet.hairlineWidth,
    borderBottomColor: "#1f2937",
  },
});
