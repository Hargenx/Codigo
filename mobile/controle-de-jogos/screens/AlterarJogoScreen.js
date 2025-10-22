import { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import { alterarJogo, encontrarJogoPorNome } from '../database/BaseDados';

const AlterarJogoScreen = ({ navigation }) => {
    const [id, getId] = useState('')
    const [nome, setNome] = useState('');
    const [plataforma, setPlataforma] = useState('');
    const [genero, setGenero] = useState('');
    const [nota, setNota] = useState('');
    const [sobre, setSobre] = useState('');

    const handleEncontrarJogo = () => {
        encontrarJogoPorNome(nome, (jogo) => {
            if (jogo) {
                getId(jogo.id);
                setPlataforma(jogo.plataforma);
                setGenero(jogo.genero);
                setNota(jogo.nota.toString());
                setSobre(jogo.sobre);
            } else {
                alert('Jogo não encontrado.');
            }
        });
    };

    const handleAlterarJogo = () => {
        alterarJogo(id, nome, plataforma, genero, parseFloat(nota), sobre, (rowsAffected) => {
            if (rowsAffected > 0) {
                alert('Jogo alterado com sucesso.');
            } else {
                alert('Erro ao alterar o jogo. Tente novamente.');
            }
        });
        navigation.navigate('Home');
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Alterar Jogo</Text>
            <TextInput
                style={styles.input}
                placeholder="Nome"
                value={nome}
                onChangeText={setNome}
            />
            <Button title="Encontrar Jogo" onPress={handleEncontrarJogo} />
            <TextInput
                style={styles.input}
                placeholder="Plataforma"
                value={plataforma}
                onChangeText={setPlataforma}
            />
            <TextInput
                style={styles.input}
                placeholder="Gênero"
                value={genero}
                onChangeText={setGenero}
            />
            <TextInput
                style={styles.input}
                placeholder="Nota"
                value={nota}
                onChangeText={setNota}
                keyboardType="numeric"
            />
            <TextInput
                style={styles.input}
                placeholder="Sobre"
                value={sobre}
                onChangeText={setSobre}
                multiline
            />
            <Button title="Alterar Jogo" onPress={handleAlterarJogo} />
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
});

export default AlterarJogoScreen;