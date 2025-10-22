import { View, Text, Button, StyleSheet } from 'react-native';

const HomeScreen = ({ navigation }) => {
    const handleCadastro = () => {
        navigation.navigate('Cadastro');
    };
    const handleVisualizarTodos = () => {
        navigation.navigate('VisualizarTodos');
    };
    const handleAlterar = () => {
        navigation.navigate('AlterarJogo');
    };
    const handleExcluir = () => {
        navigation.navigate("ExcluirJogo");
    };
    const handleEncontrarJogo = () => {
        navigation.navigate("VisualizarJogoEspecifico")
    };
    return (
        <View style={styles.container}>
            <Text style={styles.title}>Sua Coleção</Text>
            <View style={styles.buttonContainer}>
                <Button title="Cadastrar" color="#007BFF" onPress={handleCadastro} />
                <Button title="Atualizar" color="#5BC0DE" onPress={handleAlterar} />
                <Button title="Visualizar Jogo Específico" color="#5BC0DE" onPress={handleEncontrarJogo} />
                <Button title="Visualizar Todos" color="#5BC0DE" onPress={handleVisualizarTodos} />
                <Button title="Excluir" color="#D9534F" onPress={handleExcluir} />
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
    },
    buttonContainer: {
        marginTop: 20,
    },
});

export default HomeScreen;