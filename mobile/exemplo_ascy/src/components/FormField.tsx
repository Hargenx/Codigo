import React from "react";
import { View, Text, TextInput, StyleSheet } from "react-native";

export function FormField({
  label,
  value,
  onChangeText,
  placeholder,
  accessibleLabel,
}: {
  label: string;
  value: string;
  onChangeText: (t: string) => void;
  placeholder?: string;
  accessibleLabel?: string;
}) {
  return (
    <View style={{ marginBottom: 10 }}>
      <Text style={sF.label}>{label}</Text>
      <TextInput
        value={value}
        onChangeText={onChangeText}
        placeholder={placeholder}
        placeholderTextColor="#8a8a8a"
        style={sF.input}
        accessibilityLabel={accessibleLabel || label}
      />
    </View>
  );
}

const sF = StyleSheet.create({
  label: { color: "#9ca3af", marginBottom: 4 },
  input: {
    backgroundColor: "#0b1220",
    color: "#e5e7eb",
    borderWidth: 1,
    borderColor: "#1f2937",
    borderRadius: 10,
    paddingHorizontal: 10,
    paddingVertical: 8,
  },
});
