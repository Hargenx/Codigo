import { useEffect, useRef, useState } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { safeStringify } from "../storage/json";

/**
* useStoredState<T>
* - Carrega 1x o valor do AsyncStorage
* - Persiste quando o estado muda (após load)
* - Evita loops usando defaults estáveis via useRef
*/
export function useStoredState<T>(key: string, initial: T) {
    const initRef = useRef(initial);
    const [value, setValue] = useState<T>(initRef.current);
    const loadedRef = useRef(false);

    // Load once
    useEffect(() => {
        let active = true;
        (async () => {
            try {
                const raw = await AsyncStorage.getItem(key);
                if (!active) return;
                if (raw != null) setValue(JSON.parse(raw));
            } finally {
                loadedRef.current = true;
            }
        })();
        return () => {
            active = false;
        };
    }, [key]);

    // Persist on change (after load)
    useEffect(() => {
        if (!loadedRef.current) return;
        AsyncStorage.setItem(key, safeStringify(value)).catch(() => { });
    }, [key, value]);

    return [value, setValue] as const;
}