import { useCallback } from "react";
import { useStoredState } from "../storage/useStoredState";
import { KEYS } from "../storage/keys";


export function useLog(key: string = KEYS.log, max = 100) {
    const [entries, setEntries] = useStoredState<string[]>(key, []);


    const add = useCallback(
        (message: string) =>
            setEntries((prev) => [
                `${new Date().toLocaleTimeString("pt-BR")} — ${message}`,
                ...prev,
            ].slice(0, max)),
        [setEntries, max]
    );


    const clear = useCallback(() => setEntries([]), [setEntries]);


    return { entries, add, clear } as const;
}