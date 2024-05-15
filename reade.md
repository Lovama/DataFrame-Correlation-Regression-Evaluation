# DataFrame AUTO-FINDER for corr()

## Descrição

Este módulo permite analisar correlações de dados e realizar avaliações de modelagem de regressão. Ele foi projetado para identificar as correlações mais altas e mais baixas entre as variáveis de um DataFrame e avaliar modelos de regressão polinomial.

## Requisitos

Antes de começar, certifique-se de ter as seguintes bibliotecas Python instaladas:

- `pandas`
- `scikit-learn`
- `colorama`

Você pode instalar essas dependências usando o seguinte comando:

```bash
pip install pandas scikit-learn colorama
```

## Como Usar

### 1. Carregar e Analisar Correlações

O script inicialmente carrega um DataFrame a partir de um arquivo CSV e calcula as correlações mais altas e mais baixas entre as variáveis.

#### Exibindo as Maiores e Menores Correlações

O código abaixo mostra como calcular e exibir as maiores e menores correlações no DataFrame:

```python
# Configurações de exibição do pandas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Carregando o DataFrame
DF = pd.read_csv(FILE_PATH, header=0)

# Calculando e exibindo as correlações mais altas e mais baixas
HIGHEST, LOWEST, HIGHEST_COMBINATIONS, LOWEST_COMBINATIONS = highest_lowest_correlations(DF, 99)

# Limpando o terminal e exibindo os resultados
clear_terminal()
print_colored_title('DataFrame AUTO-FINDER for corr()')

print(f"\n\n{Fore.GREEN}Highest correlations (different from 1 and -1):{Style.RESET_ALL}")
print(HIGHEST)

print(f"\n\n{Fore.RED}Lowest correlations (different from 1 and -1):{Style.RESET_ALL}")
print(LOWEST)

print(f"\n\n{Fore.CYAN}List of Highest Combinations:{Style.RESET_ALL}")
print(HIGHEST_COMBINATIONS)

print(f"\n\n{Fore.MAGENTA}List of Lowest Combinations:{Style.RESET_ALL}")
print(LOWEST_COMBINATIONS)
```

### 2. Avaliação de Modelos de Regressão

Você pode realizar avaliações de modelos de regressão usando a função `regression_model_evaluation`. Esta função avalia modelos de regressão linear simples ou múltipla e modelos de regressão polinomial.

#### Avaliando um Modelo de Regressão

Para avaliar um modelo de regressão, descomente e ajuste o código abaixo conforme necessário:

```python
# Avaliando um modelo de regressão
regression_model_evaluation(
    DF[['engine-size']], DF['price'], polynomial_degree=3
)
```

### Funções Principais

#### `highest_lowest_correlations`

Calcula as correlações mais altas e mais baixas diferentes de 1 e -1 em um DataFrame.

**Argumentos:**
- `source (pd.DataFrame)`: O DataFrame de origem.
- `top_n (int)`: Número de maiores e menores correlações a serem retornadas.

**Retornos:**
- `pd.DataFrame`: DataFrame com as correlações mais altas.
- `pd.DataFrame`: DataFrame com as correlações mais baixas.
- `list`: Lista de listas com as combinações mais altas.
- `list`: Lista de listas com as combinações mais baixas.

#### `regression_model_evaluation`

Executa a modelagem de regressão e avalia o modelo.

**Argumentos:**
- `predictor_variable (pd.DataFrame)`: A variável preditora.
- `predicted_variable (pd.Series)`: A variável a ser prevista.
- `polynomial_degree (int)`: Grau dos recursos polinomiais.

**Retornos:**
- Nenhum

## Licença

Este projeto é licenciado sob os termos da licença MIT.

## Autor

Criador: Lorenzo Vaz Marzari

- [GitHub](https://github.com/HappyCoderBr)
