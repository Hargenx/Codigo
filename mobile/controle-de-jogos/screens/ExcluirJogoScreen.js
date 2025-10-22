import { useState } from 'react';
import { View, Text, TextInput, Button, FlatList, StyleSheet, Alert } from 'react-native';
import { listarJogos, excluirJogo } from '../database/BaseDados';

const ExcluirJogoScreen = ({ navigation }) => {
    const [jogos, setJogos] = useState([]);
    const [termoPesquisado, setTermoPesquisado] = useState('');

    const handlePesquisa = () => {
        listarJogos((jogos) => {
            const filteredJogos = jogos.filter((jogo) =>
                jogo.nome.toLowerCase().includes(termoPesquisado.toLowerCase())
            );
            setJogos(filteredJogos);
        });
    };

    const handleExcluir = (id, nome) => {
        Alert.alert(
            'Confirmar exclusão',
            `Deseja excluir o jogo "${nome}"?`,
            [
                {
                    text: 'Cancelar',
                    style: 'cancel',
                },
                {
                    text: 'Excluir',
                    onPress: () => {
                        excluirJogo(id, (rowsAffected) => {
                            if (rowsAffected > 0) {
                                alert('Jogo excluído com sucesso.');
                                handlePesquisa(); // Atualize a lista após a exclusão
                            } else {
                                alert('Erro ao excluir o jogo. Tente novamente.');
                            }
                        });
                        navigation.navigate('Home');
                    },
                },
            ],
            { cancelable: false }
        );
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Excluir Jogo</Text>
            <TextInput
                style={styles.input}
                placeholder="Pesquisar por nome"
                value={termoPesquisado}
                onChangeText={setTermoPesquisado}
            />
            <Button title="Pesquisar" onPress={handlePesquisa} />
            <FlatList
                data={jogos}
                keyExtractor={(item) => item.id.toString()}
                renderItem={({ item }) => (
                    <View style={styles.item}>
                        <Text>Nome: {item.nome}</Text>
                        <Text>Plataforma: {item.plataforma}</Text>
                        <Text>Gênero: {item.genero}</Text>
                        <Text>Nota: {item.nota}</Text>
                        <Text>Sobre: {item.sobre}</Text>
                        <Button
                            title="Excluir"
                            onPress={() => handleExcluir(item.id, item.nome)}
                            color="#D9534F"
                        />
                    </View>
                )}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16,
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
    item: {
        marginVertical: 10,
        borderWidth: 1,
        borderColor: '#ccc',
        padding: 10,
    },
});

export default ExcluirJogoScreen;