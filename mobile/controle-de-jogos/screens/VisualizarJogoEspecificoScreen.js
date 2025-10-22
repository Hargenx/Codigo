import { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import { encontrarJogoPorNome } from '../database/BaseDados';

const VisualizarJogoEspecificoScreen = () => {
    const [nome, setNome] = useState('');
    const [jogo, setJogo] = useState(null);

    const handleBuscarJogo = () => {
        encontrarJogoPorNome(nome, (jogoEncontrado) => {
            setJogo(jogoEncontrado);
        });
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Visualizar Jogo Específico</Text>
            <TextInput
                style={styles.input}
                placeholder="Nome do Jogo"
                value={nome}
                onChangeText={setNome}
            />
            <Button title="Buscar Jogo" onPress={handleBuscarJogo} />
            {jogo && (
                <View style={styles.jogoDetails}>
                    <Text>Nome: {jogo.nome}</Text>
                    <Text>Plataforma: {jogo.plataforma}</Text>
                    <Text>Gênero: {jogo.genero}</Text>
                    <Text>Nota: {jogo.nota}</Text>
                    <Text>Sobre: {jogo.sobre}</Text>
                </View>
            )}
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16,
        justifyContent: 'center',
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 10,
        paddingHorizontal: 10,
    },
    jogoDetails: {
        marginTop: 10,
    },
});

export default VisualizarJogoEspecificoScreen;