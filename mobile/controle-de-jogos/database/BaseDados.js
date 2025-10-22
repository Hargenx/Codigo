import { openDatabaseAsync } from 'expo-sqlite';

let _db = null;

async function getDb() {
    if (_db) return _db;

    const db = await openDatabaseAsync('ControleJogos.db');

    await db.execAsync(`
    CREATE TABLE IF NOT EXISTS jogos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT,
      plataforma TEXT,
      genero TEXT,
      nota REAL,
      sobre TEXT
    );
  `);

    _db = db;
    return db;
}

const adicionarJogo = async (nome, plataforma, genero, nota, sobre, callback) => {
    const db = await getDb();
    try {
        const res = await db.runAsync(
            'INSERT INTO jogos (nome, plataforma, genero, nota, sobre) VALUES (?, ?, ?, ?, ?)',
            [nome, plataforma, genero, nota, sobre]
        );
        const insertId = Number(res.lastInsertRowId ?? null);
        if (callback) callback(insertId);
        return insertId;
    } catch (error) {
        console.error('Erro ao adicionar jogo:', error);
        if (callback) callback(null);
        return null;
    }
};

const listarJogos = async (callback) => {
    const db = await getDb();
    const rows = await db.getAllAsync('SELECT * FROM jogos');
    if (callback) callback(rows);
    return rows;
};


const encontrarJogoPorNome = async (nome, callback) => {
    const db = await getDb();
    const row = await db.getFirstAsync('SELECT * FROM jogos WHERE nome = ?', [nome]);
    const result = row ?? null; 
    if (callback) callback(result);
    return result;
};

const alterarJogo = async (id, nome, plataforma, genero, nota, sobre, callback) => {
    const db = await getDb();
    try {
        const res = await db.runAsync(
            'UPDATE jogos SET nome = ?, plataforma = ?, genero = ?, nota = ?, sobre = ? WHERE id = ?',
            [nome, plataforma, genero, nota, sobre, id]
        );
        const rowsAffected = Number(res.changes ?? 0); // mantém: callback recebe rowsAffected
        if (callback) callback(rowsAffected);
        return rowsAffected;
    } catch (error) {
        console.error('Erro ao alterar jogo:', error);
        if (callback) callback(0);
        return 0;
    }
};

const excluirJogo = async (id, callback) => {
    const db = await getDb();
    try {
        const res = await db.runAsync('DELETE FROM jogos WHERE id = ?', [id]);
        const rowsAffected = Number(res.changes ?? 0);
        if (callback) callback(rowsAffected);
        return rowsAffected;
    } catch (error) {
        console.error('Erro ao excluir jogo:', error);
        if (callback) callback(0);
        return 0;
    }
};

export { adicionarJogo, listarJogos, alterarJogo, encontrarJogoPorNome, excluirJogo };