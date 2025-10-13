export function safeStringify<T>(value: T): string {
    try {
        return JSON.stringify(value);
    } catch (e) {
        return `"__SERIALIZATION_ERROR__:${String(e)}"`;
    }
}


export function safeParse<T>(raw: string | null, fallback: T): T {
    if (raw == null) return fallback;
    try {
        return JSON.parse(raw) as T;
    } catch {
        return fallback;
    }
}