[Inicio](../README.md) | [Data](../data/README.md) | **<u>Features</u>** | [Notebooks](../notebooks/README.md) | [Scripts](../scripts/README.md) | [Reports](../reports/README.md) | [Interactive Reports](../interactive_reports/README.md) | [Dashboard](../dashboard/README.md) | [Models](../models/README.md) | [Metrics](../metrics/README.md) | [API](../api/README.md)

# Features

A pasta 'features' guarda todos os dados que são utilizados para treinamento e teste de modelos de machine learning. Contém datasets de features derivadas através de engenharia de variáveis (feature engineering), processamento de dados brutos e agregação de informações meteorológicas e geográficas.

## Índice

- [Visão Geral](#visão-geral)
- [Arquivos Disponíveis](#arquivos-disponíveis)
- [Features Principais](#features-principais)
- [Origem dos Dados](#origem-dos-dados)
- [Engenharia de Features](#engenharia-de-features)
- [Tipos de Dados](#tipos-de-dados)

---

## Visão Geral

As features são as variáveis independentes (preditoras) utilizadas pelos modelos de Machine Learning para realizar previsões sobre:
- **Intensidade de Queimadas**: Classificação em 3 níveis (Baixo, Médio, Alto)
- **Risco de Fogo**: Previsão de ocorrência (Sim/Não)

O processo de feature engineering transforma dados brutos em variáveis significativas que capturam padrões relevantes para os modelos. Cada feature foi selecionada por sua correlação com fenômenos de queimadas ou por sua relevância geográfica/temporal.

---

## Arquivos Disponíveis

| Arquivo | Descrição | Volume |
|---------|-----------|--------|
| `df_monitor_fogo_features.csv` | Dataset consolidado com todas as features derivadas para análise de focos de fogo em Minas Gerais | ~GB |

---

## Features Principais

As seguintes features são utilizadas nos modelos de Machine Learning:

### 1. **Satelite** (Categórico)
- **Descrição**: Identificação do satélite que detectou o foco de queimada
- **Valores Possíveis**: NOAA-18, NOAA-20, Aqua, Terra, etc.
- **Origem**: [Sistema de Queimadas - INPE](http://www.inpe.br/)
- **Importância**: Diferentes satélites têm sensores com características distintas que influenciam a detecção de intensidade
- **Uso**: Classificação de Intensidade, Classificação de Risco

### 2. **Nome_Município** (Categórico)
- **Descrição**: Nome do município onde o foco foi detectado
- **Valores Possíveis**: Belo Horizonte, Montes Claros, Diamantina, etc. (centenas de municípios em MG)
- **Origem**: [Dados Geográficos do IBGE](https://www.ibge.gov.br/)
- **Importância**: Diferentes regiões têm características climáticas, econômicas e vegetativas distintas que afetam o padrão de incêndios
- **Uso**: Classificação de Intensidade, Classificação de Risco
- **Nota**: Convertido para categoria para otimização de memória

### 3. **ID_Município** (Numérico)
- **Descrição**: Código numérico único do município (código IBGE)
- **Range**: 6 dígitos (ex: 310380 para Belo Horizonte)
- **Origem**: [IBGE - Geocódigos](https://www.ibge.gov.br/)
- **Importância**: Identificação única de municípios para análise agregada e integração com outros datasets
- **Uso**: Junção com dados de área municipal, códigos de região

### 4. **Bioma** (Categórico)
- **Descrição**: Tipo de bioma onde ocorreu o foco
- **Valores Possíveis**: Cerrado, Mata Atlântica, Caatinga, Amazônia, etc.
- **Origem**: [Mapa de Biomas do Brasil - IBAMA](https://www.ibama.gov.br/)
- **Importância**: Biomas diferentes têm vegetação, umidade e inflamabilidade distintas
  - **Cerrado**: Altamente inflamável, seco, muitos focos
  - **Mata Atlântica**: Mais úmida, menos focos, mas intensos quando ocorrem
- **Uso**: Classificação de Intensidade, Classificação de Risco
- **Nota**: Convertido para categoria para otimização de memória

### 5. **Latitude** (Numérico - Float32)
- **Descrição**: Coordenada de latitude do foco (Sistema WGS84)
- **Range**: -23.0° a -14.0° (Minas Gerais)
- **Precisão**: Float32 (6 casas decimais = ~10 metros de precisão GPS)
- **Origem**: [Sistema de Queimadas - INPE](http://www.inpe.br/)
- **Importância**: Localização geográfica precisa permite análise espacial de padrões de fogo
- **Uso**: Análise de distribuição geográfica, clustering espacial, visualização em mapas

### 6. **Longitude** (Numérico - Float32)
- **Descrição**: Coordenada de longitude do foco (Sistema WGS84)
- **Range**: -51.0° a -41.0° (Minas Gerais)
- **Precisão**: Float32 (6 casas decimais = ~10 metros de precisão GPS)
- **Origem**: [Sistema de Queimadas - INPE](http://www.inpe.br/)
- **Importância**: Complementa latitude para precisão de localização
- **Uso**: Análise de distribuição geográfica, clustering, geolocalização

### 7. **Mes** (Numérico)
- **Descrição**: Mês em que o foco foi detectado
- **Range**: 1 a 12
- **Origem**: Data de detecção do foco
- **Importância**: Captura padrões sazonais de queimadas
  - **Meses secos (Agosto-Outubro)**: Pico de incêndios
  - **Meses úmidos (Novembro-Maio)**: Menos incêndios
- **Uso**: Classificação de Intensidade, Classificação de Risco

### 8. **Hora_decimal** (Numérico)
- **Descrição**: Hora de detecção em formato decimal (0.0 a 23.99)
- **Exemplos**: 14.5 = 14h30min, 08.0 = 08h00min
- **Origem**: Timestamp de detecção do satélite
- **Importância**: Padrão horário influencia detectabilidade e intensidade aparente
  - **Horários quentes (13h-15h)**: Melhor detecção de infravermelho
  - **Noites frias**: Detecções menos confiáveis
- **Uso**: Classificação de Intensidade, Classificação de Risco

### 9. **DiaSemChuva** (Numérico)
- **Descrição**: Número de dias consecutivos sem precipitação antes do foco
- **Range**: 0 a 365+ dias
- **Origem**: Dados meteorológicos INMET
- **Importância**: Seca prolongada aumenta risco e intensidade de incêndios
  - **0-7 dias**: Vegetação mais úmida, focos menos intensos
  - **30+ dias**: Seca severa, focos intensos e propagação rápida
- **Uso**: Classificação de Intensidade, Classificação de Risco
- **Impacto Alto**: Uma das features mais correlacionadas com risco

### 10. **Precipitacao** (Numérico - Float16)
- **Descrição**: Volume de precipitação acumulada (mm) no período precedente
- **Range**: 0.0 a 500+ mm
- **Origem**: [Dados Meteorológicos INMET](https://www.inmet.gov.br/)
- **Importância**: Chuva recente reduz risco e intensidade de incêndios
- **Correlação Inversa**: Mais chuva = Menos risco
- **Uso**: Classificação de Intensidade, Classificação de Risco
- **Nota**: Float16 para economizar memória, suficiente para este caso de uso

---

## Origem dos Dados

### Dados de Queimadas
- **Fonte**: [INPE - Sistema de Queimadas do Brasil](http://queimadas.dgi.inpe.br/)
- **Cobertura**: 2022, 2023, 2024, 2025
- **Satélites**: NOAA-18, NOAA-20, Aqua, Terra
- **Formato Bruto**: CSV com coordenadas, horários e FRP

### Dados Meteorológicos
- **Fonte**: [INMET - Instituto Nacional de Meteorologia](https://www.inmet.gov.br/)
- **Variáveis**: Precipitação diária, temperatura, umidade
- **Estações**: Distribuídas por Minas Gerais
- **Processamento**: Dados agregados e interpolados espacialmente para cada foco

### Dados Geográficos
- **Fonte**: [IBGE - Instituto Brasileiro de Geografia e Estatística](https://www.ibge.gov.br/)
- **Informações**: Códigos municipais, limites geográficos, biomas
- **Integração**: Merge entre focos de queimada e limites municipais/biomas

---

## Engenharia de Features

O notebook [3_feature_engineering.ipynb](../notebooks/3_feature_engineering.ipynb) é responsável pela criação de variáveis derivadas:

### Transformações Aplicadas

1. **Categorização de Intensidade**
   - Baseada no FRP (Fire Radiative Power)
   - Cortes: Baixo (<15), Médio (15-80), Alto (>80)
   - Target para classificação multiclasse

2. **Binarização de Risco**
   - Baseada em RiscoFogo (variável contínua)
   - Limiar: > 0.5
   - Target para classificação binária

3. **Conversão de Tipos de Dados**
   - Strings/Categorias comprimidas para category dtype
   - Floats para float16/float32 conforme precisão necessária
   - Inteiros comprimidos com downcast

4. **Agregação Temporal**
   - Dias sem chuva calculados com base em séries temporais meteorológicas
   - Precipitação acumulada para períodos precedentes

### Otimização de Memória

As features são otimizadas para reduzir uso de RAM:
- **Categorias**: String → Category (redução de 10-20x)
- **Floats**: Float64 → Float32/Float16 (redução de 50-75%)
- **Inteiros**: Downcast automático para menor tipo compatível

---

## Tipos de Dados

| Feature | Tipo Original | Tipo Otimizado | Tamanho | Motivo |
|---------|---------------|----------------|--------|--------|
| Satelite | String | Category | ~2 bytes | Poucos valores únicos |
| Nome_Município | String | Category | ~4 bytes | ~850 valores únicos |
| Bioma | String | Category | ~1 byte | 6 biomas principais |
| ID_Município | Int | Int16/Int32 | 2-4 bytes | Código numérico compacto |
| Latitude | Float64 | Float32 | 4 bytes | 6 decimais suficientes para GPS |
| Longitude | Float64 | Float32 | 4 bytes | 6 decimais suficientes para GPS |
| Mes | Int | Int8 | 1 byte | 1-12 apenas |
| Hora_decimal | Float64 | Float32 | 4 bytes | 0.0-23.99 |
| DiaSemChuva | Int | Int16 | 2 bytes | 0-365+ dias |
| Precipitacao | Float64 | Float16 | 2 bytes | Precisão moderada suficiente |

---

## Processo de Carregamento e Uso

### No Notebook
```python
# Otimizar dataset
df = pd.read_parquet('caminho/arquivo.parquet')
df = otimizar_dataset(df)  # Reduz memória em ~70%

# Selecionar features para modelo
features = ['Satelite', 'Nome_Município', 'Bioma', 'DiaSemChuva', 
            'Precipitacao', 'Latitude', 'Longitude', 'Mes', 'Hora_decimal', 'ID_Município']

X_train = df_train[features]
y_train = df_train['target_intensidade']
```

### Na API
```python
# Predição com feature preprocessing
features_dict = {
    'Satelite': 'NOAA-20',
    'Nome_Município': 'Montes Claros',
    'Bioma': 'Cerrado',
    'DiaSemChuva': 45,
    'Precipitacao': 2.5,
    'Latitude': -16.728,
    'Longitude': -43.857,
    'Mes': 9,
    'Hora_decimal': 14.5,
    'ID_Município': 313270
}

predicao = modelo.predict([features_dict])
```

---

## Referências e Documentação

- [Notebook 3 - Feature Engineering](../notebooks/3_feature_engineering.ipynb): Detalhes técnicos de transformação
- [Scripts - features.py](../scripts/features.py): Funções de engenharia de features
- [Models](../models/README.md): Como as features são usadas pelos modelos
- [Data](../data/README.md): Fonte e processamento dos dados brutos