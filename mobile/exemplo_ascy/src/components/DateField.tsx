import React, { useCallback, useState } from "react";
import { View, Text, Button, Platform, StyleSheet } from "react-native";
import DateTimePicker, {
  DateTimePickerEvent,
} from "@react-native-community/datetimepicker";

export function DateField({
  valueISO,
  onChangeISO,
}: {
  valueISO: string;
  onChangeISO: (iso: string) => void;
}) {
  const [open, setOpen] = useState(false);

  const onChange = useCallback(
    (e: DateTimePickerEvent, d?: Date) => {
      if (Platform.OS === "android") setOpen(false);
      const type = (e as any)?.type;
      if (d && (!type || type === "set")) onChangeISO(d.toISOString());
    },
    [onChangeISO]
  );

  const date = new Date(valueISO);
  return (
    <View style={{ gap: 6 }}>
      <Text style={sD.text}>Data: {date.toLocaleDateString("pt-BR")}</Text>
      <Button title="Escolher data" onPress={() => setOpen(true)} />
      {open && (
        <DateTimePicker
          mode="date"
          display={Platform.OS === "ios" ? "inline" : "calendar"}
          value={date}
          onChange={onChange}
        />
      )}
    </View>
  );
}

const sD = StyleSheet.create({
  text: { color: "#cbd5e1" },
});
