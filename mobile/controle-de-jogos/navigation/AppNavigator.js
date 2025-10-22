import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/HomeScreen';
import CadastroScreen from '../screens/CadastroScreen';
import VisualizarTodosScreen from '../screens/VisualizarTodosScreen';
import AlterarJogoScreen from '../screens/AlterarJogoScreen';
import ExcluirJogoScreen from '../screens/ExcluirJogoScreen';
import VisualizarJogoEspecificoScreen from '../screens/VisualizarJogoEspecificoScreen';
{/* */ }
const Stack = createStackNavigator();

const AppNavigator = () => {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen
                    name="Home"
                    component={HomeScreen}
                    options={{ title: 'Tela Inicial' }}
                />
                <Stack.Screen
                    name="Cadastro" // Defina o nome da rota para CadastroScreen
                    component={CadastroScreen} // Use CadastroScreen como o componente da rota
                    options={{ title: 'Cadastro de Jogo' }} // Opções da tela de cadastro
                />
                <Stack.Screen
                    name="VisualizarTodos" // Defina o nome da rota para VisualizarTodosScreen
                    component={VisualizarTodosScreen} // Use VisualizarTodosScreen como o componente da rota
                    options={{ title: 'Visualizar Todos' }} // Opções da tela "Visualizar Todos"
                />
                <Stack.Screen
                    name="AlterarJogo" // Defina o nome da rota para AlterarJogoScreen
                    component={AlterarJogoScreen} // Use AlterarJogoScreen como o componente da rota
                    options={{ title: 'Alterar Jogo' }} // Opções da tela "Alterar Jogo"
                />
                <Stack.Screen
                    name="ExcluirJogo" // Defina o nome da rota para ExcluirJogoScreen
                    component={ExcluirJogoScreen} // Use ExcluirJogoScreen como o componente da rota
                    options={{ title: 'Excluir Jogo' }} // Opções da tela "Excluir Jogo"
                />{/**/}
                <Stack.Screen
                    name="VisualizarJogoEspecifico" // Defina o nome da rota para VisualizarJogoEspecificoScreen
                    component={VisualizarJogoEspecificoScreen} // Use VisualizarJogoEspecificoScreen como o componente da rota
                    options={{ title: 'Visualizar Jogo Específico' }} // Opções da tela "Visualizar Jogo Específico"
                />
                {/* Adicione outras telas conforme necessário */}
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default AppNavigator;