[Inicio](../README.md) | [Data](../data/README.md) | [Features](../features/README.md) | [Notebooks](../notebooks/README.md) | [Scripts](../scripts/README.md) | [Reports](../reports/README.md) | **<u>Interactive Reports</u>** | [Dashboard](../dashboard/README.md) | [Models](../models/README.md) | [Metrics](../metrics/README.md) | [API](../api/README.md)

# Interactive Reports

Nesse diretório, serão armazenados todos os gráficos interativos do projeto. Diferentemente dos relatórios estáticos em PNG/PDF, os relatórios interativos permitem exploração dinâmica de dados através de filtros, zoom, hover info e navegação interativa.

## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Tipos de Relatórios Interativos](#tipos-de-relatórios-interativos)
- [Arquivos Disponíveis](#arquivos-disponíveis)
- [Como Gerar Relatórios](#como-gerar-relatórios)
- [Como Visualizar Relatórios](#como-visualizar-relatórios)
- [Exemplos de Uso](#exemplos-de-uso)
- [Integração com Dashboard](#integração-com-dashboard)

---

## Visão Geral

Relatórios interativos são visualizações dinâmicas que possibilitam:
- **Exploração de Dados**: Zoom, pan, seleção e filtragem em tempo real
- **Identificação de Padrões**: Visualização de tendências, outliers e correlações
- **Tomada de Decisão**: Análise exploratória rápida de informações complexas
- **Compartilhamento**: Exportação e embedding em dashboards e websites

No contexto do projeto de monitoramento de queimadas em Minas Gerais, os relatórios interativos fornecem:
- Análise geoespacial de focos com mapas interativos
- Séries temporais exploratórias de intensidade e risco
- Distribuição geográfica com filtros por período, município e bioma
- Análise de sazonalidade com heatmaps interativos

---

## Tecnologias Utilizadas

### Plotly (Principal)
- **Biblioteca**: `plotly.express` e `plotly.graph_objects`
- **Formato**: HTML interativo
- **Características**:
  - Gráficos 2D e 3D
  - Mapas geográficos com scatter plots
  - Box plots, histogramas, gráficos de barras
  - Hover info customizável
  - Controles de zoom e pan
  - Lendas interativas (click para mostrar/esconder)

### Folium (Mapas)
- **Biblioteca**: `folium` para mapas de base (OpenStreetMap)
- **Integração**: Pode ser combinada com Plotly para mapas avançados
- **Características**:
  - Tiles de diferentes provedores (OpenStreetMap, CartoDB, Mapbox)
  - Marcadores e popups customizáveis
  - Heatmaps espaciais
  - Cluster marcadores para grandes volumes

### Dash (Dashboards Interativos)
- **Framework**: `dash` para aplicações web interativas
- **Integração**: Integra gráficos Plotly em layout responsivo
- **Recursos**: Callbacks para interatividade, filtros, dropdowns

---

## Tipos de Relatórios Interativos

### 1. **Mapas de Intensidade de Queimadas**
- **Tipo**: Scatter plot geográfico
- **Dados**: Latitude, Longitude, Intensidade prevista
- **Cores**: Amarelo (Baixo) → Laranja (Médio) → Vermelho (Alto)
- **Interação**: Hover mostra detalhes do foco (coordenadas, município, intensidade)
- **Filtros**: Por mês, bioma, satélite
- **Uso**: Identificar hotspots geográficos e regiões de risco elevado

### 2. **Gráficos de Série Temporal**
- **Tipo**: Line chart interativo
- **Dados**: Evolução diária/semanal/mensal de focos, intensidade média
- **Interação**: 
  - Zoom para períodos específicos
  - Hover para valores exatos
  - Comparação lado-a-lado (realidade vs previsão)
- **Uso**: Análise de tendências sazonais e validação de modelos

### 3. **Heatmaps de Sazonalidade**
- **Tipo**: 2D heatmap
- **Dados**: Mês × Hora do dia × Frequência de focos
- **Cores**: Gradiente de intensidade de cores
- **Interação**: Hover mostra frequência exata, zoom em áreas específicas
- **Uso**: Identificar picos horários e mensais de ocorrência

### 4. **Distribuição Geográfica por Município**
- **Tipo**: Choropleth map (mapa temático)
- **Dados**: Contagem de focos ou intensidade média por município
- **Cores**: Gradiente refletindo densidade/intensidade
- **Interação**: Click em município para detalhes, hover mostra valores
- **Uso**: Identificar municípios mais afetados

### 5. **Box Plots e Distribuições**
- **Tipo**: Box plots, violins, histogramas
- **Dados**: Distribuição de FRP, precipitação, dias sem chuva por categoria
- **Interação**: Hover mostra quartis, outliers, estatísticas
- **Filtros**: Groupby bioma, município, satélite
- **Uso**: Análise exploratória de variáveis contínuas

### 6. **Scatter Plots de Correlação**
- **Tipo**: Scatter interativo com regressão opcional
- **Dados**: Ex. DiaSemChuva vs Intensidade, Precipitação vs Risco
- **Cores**: Por categoria (bioma, satélite, etc.)
- **Tamanho**: Proporcional a outra variável (ex: FRP)
- **Uso**: Investigar relações entre features

### 7. **Gráficos de Importância de Features**
- **Tipo**: Bar chart interativo
- **Dados**: Feature importance do modelo (gain, split, cover)
- **Interação**: Hover mostra valor exato, scroll para muitas features
- **Uso**: Entender quais variáveis mais influenciam as previsões

---

## Arquivos Disponíveis

Este diretório está configurado para armazenar:

| Tipo | Extensão | Descrição |
|------|----------|-----------|
| Gráficos Plotly | `.html` | Relatórios standalone interativos (recomendado) |
| Aplicações Dash | `.html` ou `app.py` | Dashboards completos com múltiplos componentes |
| Mapas Folium | `.html` | Mapas interativos com base geográfica |
| Notebooks | `.ipynb` | Jupyter notebooks com visualizações interativas |

---

## Como Gerar Relatórios

### Exemplo 1: Mapa de Intensidade com Plotly
```python
import plotly.express as px
import pandas as pd

# Carregar dados com previsões
df = pd.read_csv('dados_previsoes.csv')

# Criar mapa
fig = px.scatter_geo(df, 
    lat='Latitude', 
    lon='Longitude',
    color='Intensidade_Prevista',
    color_discrete_map={0: '#ffcc00', 1: '#ff6600', 2: '#cc0000'},
    hover_data=['Nome_Município', 'Bioma', 'Mes'],
    title='Intensidade de Queimadas - MG 2025',
    size_max=8,
    zoom=6,
    center=dict(lat=-16.8, lon=-44.3)
)

fig.update_geos(
    scope='south america',
    projection_type='mercator'
)

fig.write_html('mapa_intensidade_interativo.html')
fig.show()
```

### Exemplo 2: Série Temporal com Filtro
```python
import plotly.graph_objects as go

# Agregação diária
df_diario = df.groupby('Data').agg({
    'Focos_Reais': 'sum',
    'Focos_Previstos': 'sum'
}).reset_index()

# Gráfico com duas séries
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_diario['Data'],
    y=df_diario['Focos_Reais'],
    mode='lines',
    name='Focos Reais',
    line=dict(color='black', width=2)
))

fig.add_trace(go.Scatter(
    x=df_diario['Data'],
    y=df_diario['Focos_Previstos'],
    mode='lines',
    name='Focos Previstos',
    line=dict(color='red', width=2, dash='dash')
))

fig.update_layout(
    title='Comparação: Focos Reais vs Previstos (2025)',
    xaxis_title='Data',
    yaxis_title='Número de Focos',
    hovermode='x unified',
    template='plotly_white'
)

fig.write_html('serie_temporal_interativa.html')
fig.show()
```

### Exemplo 3: Heatmap de Sazonalidade
```python
import plotly.express as px

# Criar tabela de frequência: Mês × Hora
df_heatmap = df.groupby(['Mes', 'Hora_Decimal']).size().reset_index(name='Frequencia')
df_heatmap = df_heatmap.pivot(index='Mes', columns='Hora_Decimal', values='Frequencia')

fig = px.imshow(
    df_heatmap,
    title='Sazonalidade de Focos: Mês × Hora do Dia',
    labels=dict(x='Hora do Dia', y='Mês', color='Frequência'),
    color_continuous_scale='YlOrRd',
    aspect='auto'
)

fig.write_html('heatmap_sazonalidade_interativo.html')
fig.show()
```

---

## Integração com Dashboard

Os relatórios interativos podem ser integrados no [Dashboard](../dashboard/README.md):

---

## Ferramentas Recomendadas

- **Plotly**: Visualizações rápidas e interativas
- **Folium**: Mapas geográficos com styling avançado
- **Dash**: Aplicações web interativas com múltiplos componentes
- **Streamlit**: Alternativa mais simples para prototipagem rápida
- **Altair**: Visualização declarativa com suporte a seleção interativa

---

## Referências

- [Documentação Plotly](https://plotly.com/python/)
- [Documentação Dash](https://dash.plotly.com/)
- [Documentação Folium](https://python-visualization.github.io/folium/)
- [Dashboard do Projeto](../dashboard/README.md)
- [Reports Estáticos](../reports/README.md)