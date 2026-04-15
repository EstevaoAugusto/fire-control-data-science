[Inicio](../README.md) | **<u>Data</u>** | [Features](../features/README.md) | [Notebooks](../notebooks/README.md) | [Scripts](../scripts/README.md) | [Reports](../reports/README.md) | [Interactive Reports](../interactive_reports/README.md) | [Dashboard](../dashboard/README.md) | [Models](../models/README.md) | [Metrics](../metrics/README.md) | [API](../api/README.md)

# Descrições de Dados e Informações

## Indice

- [Dados Estruturados](#dados-estruturados)
  - [Area Territoriais - IBGE](#areas-territoriais---ibge)
  - [Código de Múnicipios IBGE](#código-de-múnicipios-ibge)
  - [BDQUEIMADAS](#bdqueimadas)
  - [BDMEP - Base dos Dados](#bdmep---base-dos-dados)
  - [MapBiomas](#mapbiomas)
  - [TerraBrasilis INPE](#terrabrasilis-inpe)
- [Dados Não-Estruturados](#dados-não-estruturados)

## Datasets Utilizados

### Dados Estruturados

#### [Areas Territoriais - IBGE](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/15761-areas-dos-municipios.html?t=acesso-ao-produto&c=1)

O redimensionamento dos valores de áreas é próprio da evolução das geotecnologias aplicadas no monitoramento da dinâmica da divisão territorial brasileira, que implica na atualização periódica dos valores das áreas estaduais e municipais com a utilização continuada de melhores técnicas e de melhores insumos de produção, além de refletir as eventuais alterações nos limites político-administrativos por justificativas legais ou judiciais.

O cálculo da área territorial do Brasil em 2024, resultou no valor total de 8509379,576 km².

Considerando a vasta quantidade de dados que o dataset oferece, será focado apenas num grupo selecionado de atributos para o projeto, tendo em mente o foco á nível estadual e municipal.

<details>
  <summary>Clique para ver o 'Dicionário de Dados: Areas Territóriais - IBGE'</summary>
  <table border="1" cellspacing="0" cellpadding="5">
    <thead>
      <tr>
        <th>Coluna</th>
        <th>Tipo</th>
        <th>Descrição</th>
        <th>Unidade / Formato</th>
        <th>Classificação</th>
        <th>Valores possíveis / Exemplo</th>
        <th>Observações</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ID_UF</td>
        <td>Inteiro</td>
        <td>Identificador único de cada UF (Unidade Federal / Estado)</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>11, 12, 13, ...</td>
        <td>Identificador é composto de apenas dois caracteres.</td>
      </tr>
    </tbody>
  </table>
</details>

#### [Código de Múnicipios IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php)

A Tabela de Códigos de Municípios do IBGE apresenta a lista dos municípios brasileiros associados a um código composto de 7 dígitos, sendo os dois primeiros referentes ao código da Unidade da Federação.
O propósito dessa tabela é de integrar a vasta quantidade de dados a partir dos códigos identificadores dos UFs e Munícipios.

<details>
  <summary>Clique para ver o 'Dicionário de Dados - Código de Múnicipios IBGE'</summary>
  <table border="1" cellspacing="0" cellpadding="5">
    <thead>
      <tr>
        <th>Coluna</th>
        <th>Tipo</th>
        <th>Descrição</th>
        <th>Unidade / Formato</th>
        <th>Classificação</th>
        <th>Valores possíveis / Exemplo</th>
        <th>Observações</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ID_UF</td>
        <td>Inteiro</td>
        <td>Identificador único de cada UF (Unidade Federal / Estado)</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>11, 12, 13, ...</td>
        <td>Identificador é composto de apenas dois caracteres.</td>
      </tr>
      <tr>
        <td>Nome_UF</td>
        <td>String</td>
        <td>Nome do UF (Unidade Federal / Estado)</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>Tocantins, Minas Gerais, Acre, etc.</td>
        <td>Há 27 UFs (26 Estados e 1 Distrito Federal)</td>
      </tr>
      <tr>
        <td>ID_MUN</td>
        <td>Inteiro</td>
        <td>Latitude do ponto de ocorrência</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>1100346, 1100023, 1100601, entre outros.</td>
        <td>O identificador é composto de 7 caracteres. A qual os primeiros dois utiliza-se o ID_UF.</td>
      </tr>
      <tr>
        <td>Nome_MUN</td>
        <td>String</td>
        <td>Nome do Município.</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>Arame, Bacuri, Xambioá, etc.</td>
        <td>Existem 5.569 ou 5.570 municípios</td>
      </tr>
    </tbody>
  </table>
</details>

### [MapBiomas - Fogo](https://plataforma.brasil.mapbiomas.org/coverage/coverage_lclu)

#### [MonitorFogo - MapBiomas](https://plataforma.monitorfogo.mapbiomas.org/)

<details>
  <summary>Clique para ver o 'Dicionário de Dados - Estatísticas MonitorFogo'</summary>
  <table border="1" cellspacing="0" cellpadding="5">
    <thead>
      <tr>
        <th>Coluna</th>
        <th>Tipo</th>
        <th>Descrição</th>
        <th>Unidade / Formato</th>
        <th>Classificação</th>
        <th>Valores possíveis / Exemplo</th>
        <th>Observações</th>
      </tr>
    </thead>
    <tbody>
        <tr>
          <td>Ano</td>
          <td>Inteiro</td>
          <td>Ano do registro do dado</td>
          <td>YYYY</td>
          <td>Temporal</td>
          <td>2019, 2020</td>
          <td>Representa o ano em que a queimada foi monitorada</td>
        </tr>
        <tr>
          <td>Bioma</td>
          <td>Texto</td>
          <td>Bioma em que o dado foi registrado</td>
          <td>Texto</td>
          <td>Espacial</td>
          <td>Amazônia, Cerrado</td>
          <td>Identifica o bioma da área afetada</td>
        </tr>
        <tr>
          <td>Estado</td>
          <td>Texto</td>
          <td>Estado brasileiro correspondente</td>
          <td>Texto</td>
          <td>Espacial</td>
          <td>Acre, Pará</td>
          <td>Indica a unidade federativa da área afetada</td>
        </tr>
        <tr>
          <td>Mes_nome</td>
          <td>Texto</td>
          <td>Nome do mês do registro</td>
          <td>Texto</td>
          <td>Temporal</td>
          <td>Abril, Agosto</td>
          <td>Usado para análise sazonal de queimadas</td>
        </tr>
        <tr>
          <td>Mes_num</td>
          <td>Inteiro</td>
          <td>Número do mês do registro</td>
          <td>1–12</td>
          <td>Temporal</td>
          <td>4, 8</td>
          <td>Facilita cálculos e gráficos de séries temporais</td>
        </tr>
        <tr>
          <td>Categoria_principal</td>
          <td>Texto</td>
          <td>Classificação geral da área</td>
          <td>Texto</td>
          <td>Categórica</td>
          <td>Antrópico, Natural</td>
          <td>Indica se a área é alterada pelo homem ou preservada</td>
        </tr>
        <tr>
          <td>Tipo_uso</td>
          <td>Texto</td>
          <td>Categoria ampla de uso do solo ou vegetação</td>
          <td>Texto</td>
          <td>Categórica</td>
          <td>Agropecuária, Floresta</td>
          <td>Primeiro nível de detalhamento da área</td>
        </tr>
        <tr>
          <td>Subtipo_uso</td>
          <td>Texto</td>
          <td>Subcategoria detalhada do uso do solo ou vegetação</td>
          <td>Texto</td>
          <td>Categórica</td>
          <td>Pastagem, Formação Florestal, Agricultura</td>
          <td>Segundo nível de detalhamento</td>
        </tr>
        <tr>
          <td>Subclasse</td>
          <td>Texto</td>
          <td>Divisão mais específica do uso do solo ou vegetação</td>
          <td>Texto</td>
          <td>Categórica</td>
          <td>Pastagem, Lavoura Temporária</td>
          <td>Terceiro nível de detalhamento</td>
        </tr>
        <tr>
          <td>Classe_fina</td>
          <td>Texto</td>
          <td>Categoria ainda mais detalhada</td>
          <td>Texto</td>
          <td>Categórica</td>
          <td>Pastagem, Outras Lavouras Temporárias</td>
          <td>Quarto nível de detalhamento</td>
        </tr>
        <tr>
          <td>Classe_final</td>
          <td>Texto</td>
          <td>Último nível de detalhamento da classificação</td>
          <td>Texto</td>
          <td>Categórica</td>
          <td>Pastagem</td>
          <td>Permite análise precisa do tipo exato de área afetada</td>
        </tr>
        <tr>
          <td>Area_queimada_ha</td>
          <td>Decimal</td>
          <td>Área queimada no período registrado</td>
          <td>Hectares (ha)</td>
          <td>Quantitativa</td>
          <td>11.043, 66041.145</td>
          <td>Indica o tamanho da área afetada pelo fogo</td>
    </tbody>
  </table>
</details>


#### [TerraBrasilis INPE](https://terrabrasilis.dpi.inpe.br/queimadas/bdqueimadas/)

##### [TerraBrasilis INPE - Situação Atual](https://terrabrasilis.dpi.inpe.br/queimadas/situacao-atual/situacao_atual/)

<details>
  <summary>Clique para ver o 'Dicionário de Dados - Código de Múnicipios IBGE'</summary>
  <table border="1" cellspacing="0" cellpadding="5">
    <thead>
      <tr>
        <th>Coluna</th>
        <th>Tipo</th>
        <th>Descrição</th>
        <th>Unidade / Formato</th>
        <th>Classificação</th>
        <th>Valores possíveis / Exemplo</th>
        <th>Observações</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ID_UF</td>
        <td>Inteiro</td>
        <td>Identificador único de cada UF (Unidade Federal / Estado)</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>11, 12, 13, ...</td>
        <td>Identificador é composto de apenas dois caracteres.</td>
      </tr>
      <tr>
        <td>Nome_UF</td>
        <td>String</td>
        <td>Nome do UF (Unidade Federal / Estado)</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>Tocantins, Minas Gerais, Acre, etc.</td>
        <td>Há 27 UFs (26 Estados e 1 Distrito Federal)</td>
      </tr>
      <tr>
        <td>ID_MUN</td>
        <td>Inteiro</td>
        <td>Latitude do ponto de ocorrência</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>1100346, 1100023, 1100601, entre outros.</td>
        <td>O identificador é composto de 7 caracteres. A qual os primeiros dois utiliza-se o ID_UF.</td>
      </tr>
      <tr>
        <td>Nome_MUN</td>
        <td>String</td>
        <td>Nome do Município.</td>
        <td>N/A</td>
        <td>Dados Brutos</td>
        <td>Arame, Bacuri, Xambioá, etc.</td>
        <td>Existem 5.569 ou 5.570 municípios</td>
      </tr>
    </tbody>
  </table>
</details>

#### [Banco de Dados de Queimadas - BaseDosDados](https://basedosdados.org/dataset/f06f3cdc-b539-409b-b311-1ff8878fb8d9?table=a3696dc2-4dd1-4f7e-9769-6aa16a1556b8)

<details>
  <summary>Clique para ver o 'Dicionário de Dados - Código de Múnicipios IBGE'</summary>
  <table border="1" cellspacing="0" cellpadding="5">
    <thead>
      <tr>
        <th>Coluna</th>
        <th>Tipo</th>
        <th>Descrição</th>
        <th>Unidade / Formato</th>
        <th>Classificação</th>
        <th>Valores possíveis / Exemplo</th>
        <th>Observações</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ano</td>
        <td>Inteiro</td>
        <td>Ano de referência da passagem do satélite segundo o fuso horário de Greenwich (GMT).</td>
        <td>XXXX</td>
        <td>Dados Brutos</td>
        <td>2019, 2020, 2021, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>mes</td>
        <td>Inteiro</td>
        <td>Mês de referência da passagem do satélite segundo o fuso horário de Greenwich (GMT).</td>
        <td>XX</td>
        <td>Dados Brutos</td>
        <td>1, 2, 3 ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>data_hora</td>
        <td>DateTime</td>
        <td>Coluna agregada de data e hora da passagem do satélite o fuso horário de Greenwich (GMT).</td>
        <td>AAAA-MM-DD HH:MM:SS</td>
        <td>Dados Brutos</td>
        <td>2024-01-16 03:57:00</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>bioma</td>
        <td>String</td>
        <td>Nome do Bioma</td>
        <td>XXXX</td>
        <td>Dados Brutos</td>
        <td>Cerrado, Mata Atlântica, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>ano</td>
        <td>Inteiro</td>
        <td>Ano de referência da passagem do satélite segundo o fuso horário de Greenwich (GMT).</td>
        <td>XXXX</td>
        <td>Dados Brutos</td>
        <td>2019, 2020, 2021, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>ano</td>
        <td>Inteiro</td>
        <td>Ano de referência da passagem do satélite segundo o fuso horário de Greenwich (GMT).</td>
        <td>Qualitativo e Cardinal</td>
        <td>Dados Brutos</td>
        <td>2019, 2020, 2021, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>sigla_uf</td>
        <td>String</td>
        <td>Sigla da Unidade Federativa.</td>
        <td>Qualitativo e Cardinal</td>
        <td>Dados Brutos</td>
        <td>3100203, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>latitude</td>
        <td>Ponto Flutuante</td>
        <td>Latitude do centro do píxel de fogo ativo apresentada em unidade de graus decimais.</td>
        <td>Quantitativo e Continuo</td>
        <td>Dados Brutos</td>
        <td>-18.24325, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>longitude</td>
        <td>Ponto Flutuante</td>
        <td>Longitude do centro do píxel de fogo ativo apresentada em unidade de graus decimais</td>
        <td>Quantitativo e Continuo</td>
        <td>Dados Brutos</td>
        <td>-18.24325, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>satelite</td>
        <td>String</td>
        <td>Nome do algoritmo utilizado e referencia ao satélite provedor da imagem.</td>
        <td>Qualitativo e Cardinal</td>
        <td>Dados Brutos</td>
        <td>NOAA-21, NOAA-20, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>dias_sem_chuva</td>
        <td>Inteiro</td>
        <td>Número de dias sem chuva até a detecção do foco.</td>
        <td>Quantitativo e Discreto</td>
        <td>Dados Brutos</td>
        <td>0, 1, 2, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>precipitacao</td>
        <td>Ponto Flutuante</td>
        <td>Valor da precipitação acumulada no dia até o momento da detecção do foco..</td>
        <td>Quantitativo e Continuo</td>
        <td>Dados Brutos</td>
        <td>1.66, 3.3, 0.3, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>risco_fogo</td>
        <td>Ponto Flutuante</td>
        <td>Valor do Risco de Fogo previsto para o dia da detecção do foco.</td>
        <td>Quantitativo e Continuo</td>
        <td>Dados Brutos</td>
        <td>0, 0.2, ...</td>
        <td>N/A</td>
      </tr>
      <tr>
        <td>potencia_radiativa_fogo</td>
        <td>Ponto Flutuante</td>
        <td>Fire Radiative Power, MW (megawatts).</td>
        <td>Quantitativo e Continuo</td>
        <td>Dados Brutos</td>
        <td>2.1, 0, ...</td>
        <td>N/A</td>
      </tr>
    </tbody>
  </table>
</details>

#### Dicionário de Dados - BDMEP Processado
<details>
  <summary>Clique para ver o 'Dicionário de Dados - BDMEP Processado'</summary>
  <table border="1" cellspacing="0" cellpadding="5">
    <thead>
      <tr>
        <th>Coluna</th>
        <th>Tipo</th>
        <th>Descrição</th>
        <th>Unidade / Formato</th>
        <th>Classificação</th>
        <th>Valores possíveis / Exemplo</th>
        <th>Observações</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>data_hora</td>
        <td>DateTime</td>
        <td>Data e hora da observação do foco de queimadas.</td>
        <td>AAAA-MM-DD HH:MM:SS</td>
        <td>Temporal</td>
        <td>2024-01-16 03:57:00</td>
        <td>Usado para séries temporais e agregações por dia.</td>
      </tr>
      <tr>
        <td>bioma</td>
        <td>String</td>
        <td>Bioma onde o foco foi detectado.</td>
        <td>Texto</td>
        <td>Espacial</td>
        <td>Amazônia, Cerrado, Mata Atlântica</td>
        <td>Permite agrupar por bioma e estudar padrões regionais.</td>
      </tr>
      <tr>
        <td>sigla_uf</td>
        <td>String</td>
        <td>Sigla da Unidade Federativa onde o evento foi detectado.</td>
        <td>Texto</td>
        <td>Espacial</td>
        <td>MG, SP, AM</td>
        <td>Identifica o estado do evento.</td>
      </tr>
      <tr>
        <td>sigla_uf_nome</td>
        <td>String</td>
        <td>Nome do estado correspondente à sigla da UF.</td>
        <td>Texto</td>
        <td>Espacial</td>
        <td>Minas Gerais, São Paulo</td>
        <td>Usado para ordenação e exibição de informações geográficas.</td>
      </tr>
      <tr>
        <td>id_municipio</td>
        <td>Inteiro</td>
        <td>Código IBGE do município.</td>
        <td>Inteiro</td>
        <td>Espacial</td>
        <td>3100203, 5300108</td>
        <td>Referência única do município no Brasil.</td>
      </tr>
      <tr>
        <td>id_municipio_nome</td>
        <td>String</td>
        <td>Nome do município relacionado ao código IBGE.</td>
        <td>Texto</td>
        <td>Espacial</td>
        <td>Belo Horizonte, Brasília</td>
        <td>Usado para exibição e joins com outros datasets.</td>
      </tr>
      <tr>
        <td>latitude</td>
        <td>Ponto Flutuante</td>
        <td>Latitude do ponto de detecção do foco.</td>
        <td>Graus decimais</td>
        <td>Espacial</td>
        <td>-18.24325</td>
        <td>Usado em mapas e análises geoespaciais.</td>
      </tr>
      <tr>
        <td>longitude</td>
        <td>Ponto Flutuante</td>
        <td>Longitude do ponto de detecção do foco.</td>
        <td>Graus decimais</td>
        <td>Espacial</td>
        <td>-48.24325</td>
        <td>Usado em mapas e análises geoespaciais.</td>
      </tr>
      <tr>
        <td>satelite</td>
        <td>String</td>
        <td>Nome do satélite ou algoritmo que detectou o foco.</td>
        <td>Texto</td>
        <td>Origem</td>
        <td>NOAA-20, NOAA-21</td>
        <td>Permite comparar sensores distintos.</td>
      </tr>
      <tr>
        <td>dias_sem_chuva</td>
        <td>Inteiro</td>
        <td>Número de dias sem chuva antes da detecção do foco.</td>
        <td>Inteiro</td>
        <td>Climatológico</td>
        <td>0, 1, 2, ...</td>
        <td>Indicador de condição de secura do solo.</td>
      </tr>
      <tr>
        <td>precipitacao</td>
        <td>Ponto Flutuante</td>
        <td>Precipitação acumulada no dia da detecção do foco.</td>
        <td>mm</td>
        <td>Climatológico</td>
        <td>0.0, 1.66, 5.2</td>
        <td>Usado para inferir condicionantes meteorológicos.</td>
      </tr>
      <tr>
        <td>risco_fogo</td>
        <td>Ponto Flutuante</td>
        <td>Risco de fogo calculado para o ponto de detecção.</td>
        <td>Escala numérica</td>
        <td>Risco</td>
        <td>0.0, 0.2, 0.8</td>
        <td>Base para modelagem de risco e alertas.</td>
      </tr>
      <tr>
        <td>potencia_radiativa_fogo</td>
        <td>Ponto Flutuante</td>
        <td>Fire Radiative Power (FRP), energia radiativa do foco.</td>
        <td>MW</td>
        <td>Físico</td>
        <td>2.1, 15.7</td>
        <td>Usado como proxy de intensidade do incêndio.</td>
      </tr>
      <tr>
        <td>Data</td>
        <td>Data</td>
        <td>Data do registro extraída de data_hora.</td>
        <td>AAAA-MM-DD</td>
        <td>Temporal</td>
        <td>2025-03-15</td>
        <td>Útil para agregações diárias.</td>
      </tr>
      <tr>
        <td>Hora</td>
        <td>Tempo</td>
        <td>Hora do registro extraída de data_hora.</td>
        <td>HH:MM:SS</td>
        <td>Temporal</td>
        <td>03:49:00</td>
        <td>Usado para análise horária.</td>
      </tr>
      <tr>
        <td>Ano</td>
        <td>Inteiro</td>
        <td>Ano extraído de data_hora.</td>
        <td>YYYY</td>
        <td>Temporal</td>
        <td>2022, 2023, 2024</td>
        <td>Permite comparações anuais.</td>
      </tr>
      <tr>
        <td>Mes</td>
        <td>Inteiro</td>
        <td>Mês extraído de data_hora.</td>
        <td>1-12</td>
        <td>Temporal</td>
        <td>1, 12</td>
        <td>Permite análise sazonal.</td>
      </tr>
      <tr>
        <td>Dia</td>
        <td>Inteiro</td>
        <td>Dia do mês extraído de data_hora.</td>
        <td>1-31</td>
        <td>Temporal</td>
        <td>1, 31</td>
        <td>Auxilia em agregações diárias e inspeções de eventos.</td>
      </tr>
    </tbody>
  </table>
</details>

### [INMET (Instituto Nacional de Meteorologia)](https://bdmep.inmet.gov.br/)

<details>
  <summary>Clique para ver o 'Dicionário de Dados - INMET 2025'</summary>
  <table border="1" cellspacing="0" cellpadding="5">
    <thead>
      <tr>
        <th>Coluna</th>
        <th>Tipo</th>
        <th>Descrição</th>
        <th>Unidade / Formato</th>
        <th>Classificação</th>
        <th>Valores possíveis / Exemplo</th>
        <th>Observações</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>REGIAO</td>
        <td>String</td>
        <td>Região administrativa da estação meteorológica.</td>
        <td>Texto</td>
        <td>Geográfica</td>
        <td>Centro-Oeste, Sul</td>
        <td>Identifica a macrorregião de operação da estação.</td>
      </tr>
      <tr>
        <td>UF</td>
        <td>String</td>
        <td>Estado onde está localizada a estação.</td>
        <td>Texto</td>
        <td>Geográfica</td>
        <td>DF, GO, MG</td>
        <td>Permite cruzamento com dados de unidades federativas.</td>
      </tr>
      <tr>
        <td>ESTACAO</td>
        <td>String</td>
        <td>Nome da estação meteorológica.</td>
        <td>Texto</td>
        <td>Identificação</td>
        <td>Brasília, Goiânia</td>
        <td>Nome usado para referência de localização.</td>
      </tr>
      <tr>
        <td>CODIGO (WMO)</td>
        <td>String</td>
        <td>Código WMO da estação meteorológica.</td>
        <td>Texto</td>
        <td>Identificação</td>
        <td>82974, 83811</td>
        <td>Usado como identificador internacional da estação.</td>
      </tr>
      <tr>
        <td>LATITUDE</td>
        <td>Ponto Flutuante</td>
        <td>Latitude da estação meteorológica.</td>
        <td>Graus decimais</td>
        <td>Geográfica</td>
        <td>-15.786, -16.678</td>
        <td>Usado em mapas e georreferenciamento.</td>
      </tr>
      <tr>
        <td>LONGITUDE</td>
        <td>Ponto Flutuante</td>
        <td>Longitude da estação meteorológica.</td>
        <td>Graus decimais</td>
        <td>Geográfica</td>
        <td>-47.929, -49.264</td>
        <td>Usado em mapas e georreferenciamento.</td>
      </tr>
      <tr>
        <td>ALTITUDE</td>
        <td>Ponto Flutuante</td>
        <td>Altitude da estação sobre o nível do mar.</td>
        <td>Metros</td>
        <td>Geográfica</td>
        <td>1172.0, 710.0</td>
        <td>Importante para cálculos atmosféricos.</td>
      </tr>
      <tr>
        <td>DATA DE FUNDACAO</td>
        <td>String</td>
        <td>Data de inauguração da estação.</td>
        <td>Texto</td>
        <td>Metadado</td>
        <td>01/01/1990</td>
        <td>Facilita histórico da rede de estações.</td>
      </tr>
      <tr>
        <td>data</td>
        <td>Data</td>
        <td>Data da observação.</td>
        <td>AAAA-MM-DD</td>
        <td>Temporal</td>
        <td>2025-03-15</td>
        <td>Inclusa para facilitar agregações diárias.</td>
      </tr>
      <tr>
        <td>hora</td>
        <td>Texto</td>
        <td>Hora da observação.</td>
        <td>HHMM</td>
        <td>Temporal</td>
        <td>0300, 1200</td>
        <td>Representa o horário do registro.</td>
      </tr>
      <tr>
        <td>data_hora</td>
        <td>DateTime</td>
        <td>Data e hora combinadas em um só campo.</td>
        <td>AAAA-MM-DD HH:MM</td>
        <td>Temporal</td>
        <td>2025-03-15 03:00</td>
        <td>Útil para ordenação cronológica e análises temporais.</td>
      </tr>
      <tr>
        <td>precip_total_mm</td>
        <td>Ponto Flutuante</td>
        <td>Precipitação total no período em milímetros.</td>
        <td>mm</td>
        <td>Climatológico</td>
        <td>0.0, 12.5</td>
        <td>Usado para relacionar chuva e risco de fogo.</td>
      </tr>
      <tr>
        <td>pressao_atms_nivel_estacao_mB</td>
        <td>Ponto Flutuante</td>
        <td>Pressão atmosférica ao nível da estação.</td>
        <td>mB</td>
        <td>Climatológico</td>
        <td>1013.2</td>
        <td>Importante para análise de estabilidade atmosférica.</td>
      </tr>
      <tr>
        <td>pressao_atms_maximo_na_hora_mB</td>
        <td>Ponto Flutuante</td>
        <td>Maior pressão registrada na hora.</td>
        <td>mB</td>
        <td>Climatológico</td>
        <td>1018.5</td>
        <td>Auxilia na detecção de frentes frias e sistemas de alta pressão.</td>
      </tr>
      <tr>
        <td>pressao_atms_minimo_na_hora_mB</td>
        <td>Ponto Flutuante</td>
        <td>Menor pressão registrada na hora.</td>
        <td>mB</td>
        <td>Climatológico</td>
        <td>1008.6</td>
        <td>Útil para identificar cavados e baixa pressão.</td>
      </tr>
      <tr>
        <td>radiacao_global_kj_m</td>
        <td>Ponto Flutuante</td>
        <td>Radiação solar global acumulada.</td>
        <td>kJ/m²</td>
        <td>Físico</td>
        <td>1500.0</td>
        <td>Importante para análise de evaporação e secura do solo.</td>
      </tr>
      <tr>
        <td>temp_ar_bulbo_seco_C</td>
        <td>Ponto Flutuante</td>
        <td>Temperatura do ar medida com bulbo seco.</td>
        <td>°C</td>
        <td>Climatológico</td>
        <td>25.8</td>
        <td>Usado em diversos índices meteorológicos.</td>
      </tr>
      <tr>
        <td>tempo_ponto_orvarlho_C</td>
        <td>Ponto Flutuante</td>
        <td>Temperatura de ponto de orvalho.</td>
        <td>°C</td>
        <td>Climatológico</td>
        <td>18.5</td>
        <td>Indica a umidade mínima antes da condensação.</td>
      </tr>
      <tr>
        <td>temp_max_hora_C</td>
        <td>Ponto Flutuante</td>
        <td>Temperatura máxima dentro da hora.</td>
        <td>°C</td>
        <td>Climatológico</td>
        <td>27.9</td>
        <td>Usado para variação térmica e extremos.</td>
      </tr>
      <tr>
        <td>temp_min_hora_C</td>
        <td>Ponto Flutuante</td>
        <td>Temperatura mínima dentro da hora.</td>
        <td>°C</td>
        <td>Climatológico</td>
        <td>23.3</td>
        <td>Usado para análise de amplitude térmica.</td>
      </tr>
      <tr>
        <td>temp_orvalho_max_C</td>
        <td>Ponto Flutuante</td>
        <td>Maior temperatura de ponto de orvalho registrada na hora.</td>
        <td>°C</td>
        <td>Climatológico</td>
        <td>19.8</td>
        <td>Indica o nível máximo de vapor d'água no ar.</td>
      </tr>
      <tr>
        <td>temp_orvalho_min_C</td>
        <td>Ponto Flutuante</td>
        <td>Menor temperatura de ponto de orvalho registrada na hora.</td>
        <td>°C</td>
        <td>Climatológico</td>
        <td>16.1</td>
        <td>Indica a variação do ponto de orvalho.</td>
      </tr>
      <tr>
        <td>umidade_rel_max</td>
        <td>Ponto Flutuante</td>
        <td>Umidade relativa máxima no período.</td>
        <td>%</td>
        <td>Climatológico</td>
        <td>98.0</td>
        <td>Ajuda a avaliar a umidade disponível para combustão.</td>
      </tr>
      <tr>
        <td>umidade_rel_min</td>
        <td>Ponto Flutuante</td>
        <td>Umidade relativa mínima no período.</td>
        <td>%</td>
        <td>Climatológico</td>
        <td>42.5</td>
        <td>Importante para análises de risco de incêndios.</td>
      </tr>
      <tr>
        <td>umidade_relativa_ar</td>
        <td>Ponto Flutuante</td>
        <td>Umidade relativa do ar medida na estação.</td>
        <td>%</td>
        <td>Climatológico</td>
        <td>65.0</td>
        <td>Valor principal para índices de secura.</td>
      </tr>
      <tr>
        <td>vento_direcao_horaria</td>
        <td>Ponto Flutuante</td>
        <td>Direção do vento em graus.</td>
        <td>Graus</td>
        <td>Dinâmico</td>
        <td>90.0, 180.0</td>
        <td>Importante para dispersão e propagação de fogo.</td>
      </tr>
      <tr>
        <td>vento_rajada_max</td>
        <td>Ponto Flutuante</td>
        <td>Velocidade máxima de rajada de vento.</td>
        <td>m/s</td>
        <td>Dinâmico</td>
        <td>10.5, 18.2</td>
        <td>Maior influência em propagação de incêndios.</td>
      </tr>
      <tr>
        <td>vento_velocidade_horaria</td>
        <td>Ponto Flutuante</td>
        <td>Velocidade média do vento na hora.</td>
        <td>m/s</td>
        <td>Dinâmico</td>
        <td>2.4, 5.7</td>
        <td>Útil para modelagem de transporte de fumaça.</td>
      </tr>
    </tbody>
  </table>
</details>


### [BDQUEIMADAS](https://terrabrasilis.dpi.inpe.br/queimadas/bdqueimadas/#exportar-dados)

<details>
  <summary>Clique para ver o 'Dicionário de Dados - BDQUEIMADAS'</summary>
    <table border="1" cellspacing="0" cellpadding="5">
      <thead>
        <tr>
        <th>Coluna</th>
        <th>Tipo</th>
        <th>Descrição</th>
        <th>Unidade / Formato</th>
        <th>Classificação</th>
        <th>Valores possíveis / Exemplo</th>
        <th>Observações</th>
        </tr>
        </thead>
<tbody>
<tr>
<td><b>DataHora</b></td>
<td>datetime64</td>
<td>Instante exato da detecção do foco pelo satélite.</td>
<td>AAAA/MM/DD HH:MM:SS</td>
<td>Temporal</td>
<td>2024/08/15 13:30:00</td>
<td>Coluna "mãe" das colunas Data, Hora, Mes, etc.</td>
</tr>
<tr>
<td><b>Satelite</b></td>
<td>object/cat</td>
<td>Identificação do satélite sensor que captou o foco.</td>
<td>Texto</td>
<td>Categórica</td>
<td>AQUA_M-T, TERRA_M-T, NOAA-20</td>
<td>Essencial para o modelo saber a fonte do dado.</td>
</tr>
<tr>
<td><b>Pais</b></td>
<td>object</td>
<td>País onde o foco foi detectado.</td>
<td>Texto</td>
<td>Geográfica</td>
<td>Brasil</td>
<td>Geralmente constante no seu dataset.</td>
</tr>
<tr>
<td><b>Nome_UF</b></td>
<td>object</td>
<td>Nome da Unidade da Federação.</td>
<td>Texto</td>
<td>Geográfica</td>
<td>Minas Gerais</td>
<td>Filtro principal do seu estudo.</td>
</tr>
<tr>
<td><b>Nome_Município</b></td>
<td>object/cat</td>
<td>Nome do município da ocorrência.</td>
<td>Texto</td>
<td>Geográfica</td>
<td>Belo Horizonte, Uberlândia</td>
<td>Alta cardinalidade (muitos valores únicos).</td>
</tr>
<tr>
<td><b>Bioma</b></td>
<td>object/cat</td>
<td>Ecossistema predominante no local do foco.</td>
<td>Texto</td>
<td>Ambiental</td>
<td>Cerrado, Mata Atlântica</td>
<td>Crucial para entender o comportamento do fogo.</td>
</tr>
<tr>
<td><b>DiaSemChuva</b></td>
<td>float/int</td>
<td>Número de dias consecutivos sem precipitação.</td>
<td>Dias</td>
<td>Numérica</td>
<td>0 a 120</td>
<td>Principal indicador de seca acumulada.</td>
</tr>
<tr>
<td><b>Precipitacao</b></td>
<td>float</td>
<td>Volume de chuva acumulado no período.</td>
<td>mm</td>
<td>Numérica</td>
<td>0.0 a 150.0</td>
<td>Influencia diretamente o RiscoFogo.</td>
</tr>
<tr>
<td><b>RiscoFogo</b></td>
<td>float</td>
<td>Probabilidade estimada de ignição da vegetação.</td>
<td>0.0 a 1.0</td>
<td>Numérica</td>
<td>0.1, 0.95, 1.0</td>
<td>Frequentemente usado como Target.</td>
</tr>
<tr>
<td><b>FRP</b></td>
<td>float</td>
<td>Potência Radiativa do Fogo (Intensidade).</td>
<td>Megawatts (MW)</td>
<td>Numérica</td>
<td>1.0 a 3694.8</td>
<td>Usaremos para classificar em Baixo, Médio e Alto.</td>
</tr>
<tr>
<td><b>Latitude</b></td>
<td>float32</td>
<td>Coordenada geográfica (Eixo Y).</td>
<td>Graus Decimais</td>
<td>Geográfica</td>
<td>-18.123456</td>
<td>Manter precisão decimal para mapas.</td>
</tr>
<tr>
<td><b>Longitude</b></td>
<td>float32</td>
<td>Coordenada geográfica (Eixo X).</td>
<td>Graus Decimais</td>
<td>Geográfica</td>
<td>-44.123456</td>
<td>Manter precisão decimal para mapas.</td>
</tr>
<tr>
<td><b>Data</b></td>
<td>object/date</td>
<td>Data da ocorrência (sem a hora).</td>
<td>AAAA-MM-DD</td>
<td>Temporal</td>
<td>2024-09-01</td>
<td>Extraído da DataHora.</td>
</tr>
<tr>
<td><b>Hora</b></td>
<td>object/time</td>
<td>Hora da ocorrência.</td>
<td>HH:MM:SS</td>
<td>Temporal</td>
<td>15:45:00</td>
<td>Importante para ciclos diários (dia/noite).</td>
</tr>
<tr>
<td><b>Ano</b></td>
<td>int16</td>
<td>Ano da ocorrência.</td>
<td>Ano</td>
<td>Temporal</td>
<td>2022, 2023, 2024, 2025</td>
<td>Usado para a divisão Treino/Teste.</td>
</tr>
<tr>
<td><b>Mes</b></td>
<td>int8</td>
<td>Mês da ocorrência.</td>
<td>1 a 12</td>
<td>Temporal</td>
<td>8 (Agosto), 9 (Setembro)</td>
<td>Sua feature de maior importância.</td>
</tr>
<tr>
<td><b>Dia</b></td>
<td>int8</td>
<td>Dia do mês.</td>
<td>1 a 31</td>
<td>Temporal</td>
<td>1, 15, 30</td>
<td>Útil para análises de curto prazo.</td>
</tr>
<tr>
<td><b>Hora_decimal</b></td>
<td>float16</td>
<td>Conversão da hora para formato numérico.</td>
<td>0.0 a 23.99</td>
<td>Temporal</td>
<td>14.5 (equivale a 14:30)</td>
<td>Facilita o cálculo matemático do modelo.</td>
</tr>
<tr>
<td><b>ID_UF</b></td>
<td>int8</td>
<td>Código identificador do Estado.</td>
<td>Código IBGE</td>
<td>Geográfica</td>
<td>31 (Minas Gerais)</td>
<td>Geralmente redundante se for apenas MG.</td>
</tr>
<tr>
<td><b>ID_Município</b></td>
<td>int32</td>
<td>Código identificador do Município.</td>
<td>Código IBGE</td>
<td>Geográfica</td>
    <td>3106200 (BH)</td>
    <td>Melhor que o nome para o LightGBM.</td>
    </tr>
    </tbody>
    <tr>
<td><b>Risco_Classe</b></td>
<td>int8 (0 ou 1)</td>
<td>Classificação binária de ocorrência.</td>
<td>Binário</td>
<td>Target (Binário)</td>
<td><b>0:</b> Sem Fogo / <b>1:</b> Fogo (Risco &gt; 0.5)</td>
</tr>
<tr>
<td><b>Intensidade_Fogo</b></td>
<td>int8 (0, 1, 2)</td>
<td>Nível de energia e destruição do foco.</td>
<td>Multiclasse</td>
<td>Target (Ordinal)</td>
<td>
<b>0 (Baixo):</b> FRP &lt; 15MW

<b>1 (Médio):</b> FRP 15-80MW

<b>2 (Alto):</b> FRP &gt; 80MW
  </table>
</details>