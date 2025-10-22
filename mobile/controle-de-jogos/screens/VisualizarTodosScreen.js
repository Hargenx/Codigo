import { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import { listarJogos } from '../database/BaseDados';

const VisualizarTodosScreen = () => {
    const [jogos, setJogos] = useState([]);
    useEffect(() => {
        listarJogos((jogos) => {
            setJogos(jogos);
        });
    }, []);

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Visualizar Todos</Text>
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
    item: {
        marginVertical: 10,
        borderWidth: 1,
        borderColor: '#ccc',
        padding: 10,
    },
});

export default VisualizarTodosScreen;