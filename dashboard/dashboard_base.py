import dash
from dash import dcc, html, Input, Output, callback
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
#  App Setup
# ─────────────────────────────────────────────
app = dash.Dash(
    __name__,
    title="Dashboard Integrado Queimadas MG",
    suppress_callback_exceptions=True,
)

# ─────────────────────────────────────────────
#  Dados Consolidados (Baseados no README.md)
# ─────────────────────────────────────────────

# 1. EDA - Sazonalidade (Hectares por Mês em MG)
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
hectares_mg = [8667, 10440, 16615, 20476, 23796, 55146, 116210, 338856, 583494, 304183, 68204, 16871]

# 2. EDA - Uso do Solo
df_uso = pd.DataFrame({
    "categoria": ["Agropecuária", "Floresta", "Formação Natural", "Outros"],
    "valor": [32.4, 32.2, 29.6, 5.8] # Em milhões de hectares
})

# 3. ML Regressão - Importância de Atributos (Foco em Predição de Risco)
df_features = pd.DataFrame({
    "feature": ["Latitude", "Longitude", "ID_Município", "DiaSemChuva", "Hora_decimal", "Bioma"],
    "importancia": [3800, 3350, 1650, 1350, 1200, 450]
}).sort_values(by="importancia", ascending=True)

# 4. ML Classificação - Evolução da Intensidade
# % de focos Médio/Alto ao longo do ano
prop_intensidade_alta = [15, 10, 12, 8, 5, 15, 25, 40, 65, 35, 15, 10]

# ─────────────────────────────────────────────
#  Estilo Visual (Paleta Dark & Fire)
# ─────────────────────────────────────────────
COLORS = {
    "bg":      "#0d1117",
    "card":    "#161b22",
    "border":  "#30363d",
    "accent":  "#ff5f1f",  # Neon Orange
    "red":     "#f85149",
    "blue":    "#58a6ff",
    "text":    "#8b949e",
    "bright":  "#c9d1d9"
}

CHART_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color=COLORS["bright"], size=11),
    margin=dict(l=40, r=20, t=40, b=40),
)

# ─────────────────────────────────────────────
#  Componentes de Interface
# ─────────────────────────────────────────────
def kpi_card(label, value, subtext, color=COLORS["accent"]):
    return html.Div(
        style={
            "background": COLORS["card"],
            "border": f"1px solid {COLORS['border']}",
            "padding": "15px 20px",
            "borderRadius": "8px",
            "flex": "1"
        },
        children=[
            html.P(label, style={"margin": "0", "fontSize": "11px", "color": COLORS["text"], "textTransform": "uppercase"}),
            html.H3(value, style={"margin": "5px 0", "color": COLORS["bright"], "fontSize": "24px"}),
            html.Span(subtext, style={"fontSize": "11px", "color": color, "fontWeight": "600"})
        ]
    )

def section_title(title):
    return html.H3(title, style={
        "color": COLORS["accent"], 
        "fontSize": "16px", 
        "borderBottom": f"1px solid {COLORS['border']}",
        "paddingBottom": "10px",
        "marginTop": "25px"
    })

def insight_item(bold_text, normal_text):
    return html.Div(style={"marginBottom": "12px"}, children=[
        html.B(f"• {bold_text}: ", style={"color": COLORS["bright"], "fontSize": "13px"}),
        html.Span(normal_text, style={"color": COLORS["text"], "fontSize": "13px"})
    ])

# ─────────────────────────────────────────────
#  Gráficos
# ─────────────────────────────────────────────
def fig_sazonalidade():
    fig = go.Figure(go.Bar(
        x=meses, y=hectares_mg,
        marker_color=[COLORS["accent"] if x > 400000 else COLORS["blue"] for x in hectares_mg]
    ))
    fig.update_layout(**CHART_LAYOUT, title="Área Queimada Mensal (MG)")
    return fig

def fig_features():
    fig = go.Figure(go.Bar(
        x=df_features["importancia"], y=df_features["feature"],
        orientation='h', marker_color=COLORS["accent"]
    ))
    fig.update_layout(**CHART_LAYOUT, title="Principais Gatilhos de Risco (ML)")
    return fig

def fig_uso_solo():
    fig = go.Figure(go.Pie(
        labels=df_uso["categoria"], values=df_uso["valor"],
        hole=0.5, marker=dict(colors=[COLORS["accent"], COLORS["blue"], COLORS["text"], "#333"])
    ))
    fig.update_layout(**CHART_LAYOUT, title="Uso do Solo Afetado")
    return fig

# ─────────────────────────────────────────────
#  Layout Principal
# ─────────────────────────────────────────────
app.layout = html.Div(
    style={"background": COLORS["bg"], "minHeight": "100vh", "fontFamily": "Inter, sans-serif", "padding": "30px"},
    children=[
        # Header
        html.Div(style={"display": "flex", "justifyContent": "space-between", "alignItems": "center", "marginBottom": "30px"}, children=[
            html.Div([
                html.H1("🔥 MG Fire Intelligence Dashboard", style={"color": COLORS["bright"], "margin": "0"}),
                html.P("Análise Preditiva de Incêndios Florestais com LightGBM", style={"color": COLORS["text"], "margin": "5px 0 0 0"})
            ]),
            html.Div(style={"textAlign": "right"}, children=[
                html.Span("Status do Modelo: ", style={"color": COLORS["text"]}),
                html.Span("● ONLINE", style={"color": "#3fb950", "fontWeight": "bold"})
            ])
        ]),

        # KPIs de Performance e Negócio
        html.Div(style={"display": "flex", "gap": "15px", "marginBottom": "25px"}, children=[
            kpi_card("Acurácia Predição (R²)", "0.65", "Correlação Sólida", COLORS["blue"]),
            kpi_card("Erro Médio (MAE)", "0.10", "Margem de 10%"),
            kpi_card("Pico Crítico", "Setembro", "Sazonalidade Máxima", COLORS["red"]),
            kpi_card("Bioma Foco", "Cerrado", "> 1M Hectares", COLORS["accent"]),
        ]),

        # Grid de Conteúdo
        html.Div(style={"display": "grid", "gridTemplateColumns": "2.2fr 1fr", "gap": "20px"}, children=[
            
            # Lado Esquerdo: Visualizações
            html.Div(children=[
                html.Div(style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "20px", "marginBottom": "20px"}, children=[
                    html.Div(style={"background": COLORS["card"], "padding": "15px", "borderRadius": "8px"}, children=[dcc.Graph(figure=fig_sazonalidade())]),
                    html.Div(style={"background": COLORS["card"], "padding": "15px", "borderRadius": "8px"}, children=[dcc.Graph(figure=fig_uso_solo())]),
                ]),
                html.Div(style={"background": COLORS["card"], "padding": "15px", "borderRadius": "8px"}, children=[
                    dcc.Graph(figure=fig_features())
                ]),
            ]),

            # Lado Direito: Central de Insights (README)
            html.Div(
                style={
                    "background": COLORS["card"], 
                    "padding": "25px", 
                    "borderRadius": "8px", 
                    "border": f"1px solid {COLORS['border']}",
                    "maxHeight": "850px",
                    "overflowY": "auto"
                },
                children=[
                    html.H2("📄 Insights do Relatório", style={"color": COLORS["bright"], "marginTop": "0"}),
                    
                    section_title("🔍 Diagnóstico EDA"),
                    insight_item("Conflito de Solo", "Empate técnico entre Agropecuária e Floresta (~32M ha cada), sugerindo origem humana no fogo."),
                    insight_item("Anomalia MG 2021", "O estado concentrou 25.1% de suas queimadas históricas em 2021, divergindo da média nacional."),
                    insight_item("Setembro Vermelho", "Mês com maior volume de área queimada e intensificação do risco climático."),

                    section_title("🤖 Inteligência de Risco (Regressor)"),
                    insight_item("Geografia como Destino", "Latitude e Longitude são os preditores mais fortes, indicando hotspots históricos."),
                    insight_item("Confiabilidade", "80% das previsões têm erro inferior a 0.15, permitindo alertas seguros."),
                    insight_item("Fragilidade do Cerrado", "Risco mediano superior à Mata Atlântica devido à variabilidade climática."),

                    section_title("🔥 Intensidade do Fogo (Classifier)"),
                    insight_item("Tendência Conservadora", "O modelo identifica bem o nível Baixo (81%), mas tende a classificar Alto como Médio."),
                    insight_item("Agressividade Sazonal", "Em Setembro, a proporção de fogos de alta intensidade cresce exponencialmente."),
                    
                    html.Div(style={"marginTop": "30px", "padding": "15px", "background": "rgba(88, 166, 255, 0.1)", "borderRadius": "8px"}, children=[
                        html.P("📢 Recomendação Defesa Civil:", style={"color": COLORS["blue"], "fontWeight": "bold", "margin": "0"}),
                        html.P("Priorizar patrulhamento em Setembro em áreas do Cerrado com Risco > 0.75.", style={"fontSize": "12px", "marginTop": "5px"})
                    ])
                ]
            )
        ])
    ]
)

if __name__ == "__main__":
    app.run(debug=True)