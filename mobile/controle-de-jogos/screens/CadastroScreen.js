import { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import { adicionarJogo } from '../database/BaseDados';


const CadastroScreen = ({ navigation }) => {
    const [nome, setNome] = useState('');
    const [plataforma, setPlataforma] = useState('');
    const [genero, setGenero] = useState('');
    const [nota, setNota] = useState('');
    const [sobre, setSobre] = useState('');

    const handleCadastro = () => {
        // Verifique se todos os campos estão preenchidos
        if (!nome || !plataforma || !genero || !nota || !sobre) {
            alert('Preencha todos os campos antes de cadastrar.');
            return;
        }

        // Chame a função adicionarJogo para inserir o jogo no banco de dados
        adicionarJogo(nome, plataforma, genero, parseFloat(nota), sobre, (id) => {
            if (id) {
                // Redirecione o usuário de volta à tela inicial após o cadastro
                alert('Jogo cadastrado com sucesso.');
                navigation.navigate('Home');
            } else {
                alert('Erro ao cadastrar o jogo. Tente novamente.');
            }
        });
        navigation.navigate('Home');
    };

    return (
        <View style={styles.container}>
            <Text>Cadastro de Jogo</Text>
            <TextInput
                style={styles.input}
                placeholder="Nome"
                value={nome}
                onChangeText={setNome}
            />
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
            <Button title="Cadastrar" onPress={handleCadastro} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16,
        justifyContent: 'center',
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 10,
        paddingHorizontal: 10,
    },
});

export default CadastroScreen;