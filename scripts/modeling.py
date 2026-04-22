"""
modeling.py
---------------
Módulo de manipulação e criação de modelos de Machine Learning/IA
Inclui: 
    - Salvamento e Carregamento de objetos via Pickle e Joblib.
    - Entre outros.
"""

import os
import pickle
import joblib
from pathlib import Path
import sys
from typing import Any, Dict
from api.schemas.schemas import TipoModelo, InfoModelo, ListaModelos, MetricasClassificacao, MetricasRegressao

current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
    
import config_path          # Módulo que salva todos os caminhos de diretórios utilizados no projeto

# -----------------------------
#  Salvamento e Carregamentode Modelos de Machine Learning expandido
# -----------------------------
def salvar_metricas_classificacao(dados: Dict[str, Any], nome_modelo: str):
    """
    Salva métricas de classificação. 
    'dados' deve conter as chaves: acuracia, precisao, recall, f1_score, 
    matriz_confusao e relatorio_classes.
    
    Args:
        - dados (Dict[str, Any]): Dicionário com as métricas de classificação.
        - nome_modelo (str): Nome do modelo para identificar o arquivo de métricas.
        
    Returns:
        None (salva o arquivo no disco)
    """
    caminho = config_path.METRICS_DIRECTORY_PATH / f"metrics_clf_{nome_modelo}"
    
    # Tratamento de tipos Numpy (comum em matrizes de confusão e reports)
    if hasattr(dados.get("matriz_confusao"), "tolist"):
        dados["matriz_confusao"] = dados["matriz_confusao"].tolist()
    
    # Validação com o Schema
    metricas = MetricasClassificacao(**dados)
    
    joblib.dump(metricas.model_dump(), caminho)
    print(f"✅ Métricas de classificação salvas: {caminho}")

def carregar_metricas_classificacao(nome_modelo: str) -> MetricasClassificacao:
    """Carrega e retorna o objeto MetricasClassificacao."""
    caminho = config_path.METRICS_DIRECTORY_PATH / f"metrics_clf_{nome_modelo}"
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    
    dados = joblib.load(caminho)
    return MetricasClassificacao(**dados)

def salvar_metricas_regressao(dados: Dict[str, Any], nome_modelo: str):
    """
    Salva métricas de regressão.
    'dados' deve conter: mae, mse, rmse, r2 e opcionalmente mape.
    
    Args:
        - dados (Dict[str, Any]): Dicionário com as métricas de regressão.
        - nome_modelo (str): Nome do modelo para identificar o arquivo de métricas.
        
    Returns:
        None (salva o arquivo no disco)
    """
    caminho = config_path.METRICS_DIRECTORY_PATH / f"metrics_reg_{nome_modelo}"
    
    # Conversão de segurança para floats nativos (evita erro de float64 do numpy)
    for chave in ["mae", "mse", "rmse", "r2", "mape"]:
        if chave in dados and dados[chave] is not None:
            dados[chave] = float(dados[chave])

    # Validação com o Schema
    metricas = MetricasRegressao(**dados)
    
    joblib.dump(metricas.model_dump(), caminho)
    print(f"✅ Métricas de regressão salvas: {caminho}")

def carregar_metricas_regressao(nome_modelo: str) -> MetricasRegressao:
    """
    Carrega e retorna o objeto MetricasRegressao.
    
    Args:
        - nome_modelo (str): Nome do modelo para identificar o arquivo de métricas.
    
    Returns:
        - MetricasRegressao: Objeto contendo as métricas de regressão.
    """
    caminho = config_path.METRICS_DIRECTORY_PATH / f"metrics_reg_{nome_modelo}"
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    
    dados = joblib.load(caminho)
    return MetricasRegressao(**dados)

def salvar_modelo_com_metadados(
    modelo_treinado, 
    nome_arquivo: str, 
    tipo: TipoModelo,
    feature_names: list
):
    """
    Salva o modelo e os metadados validados pelo Pydantic em um único arquivo .joblib
    
    Args:
        - modelo_treinado: O objeto do modelo treinado (ex: RandomForestClassifier).
        - nome_arquivo (str): Nome do arquivo .joblib (ex: 'lgbm_classificacao.joblib').
        - tipo (TipoModelo): Enum indicando se é classificação ou regressão.
        - feature_names (list): Lista de nomes das features utilizadas no modelo.
    
    Returns:
        None (salva o arquivo no disco)
    """
    caminho_final = config_path.MODELS_DIRECTORY_PATH / nome_arquivo
    
    # 1. Preparar os dados para o Schema InfoModelo
    # Nota: Alguns dados como tamanho_mb só saberemos após salvar, 
    # então colocamos valores iniciais.
    info = InfoModelo(
        nome=nome_arquivo,
        tipo=tipo,
        caminho=caminho_final,
        tamanho_mb=0.0,  # Atualizado após o dump
        num_features=len(feature_names),
        feature_names=feature_names,
        num_classes=len(modelo_treinado.classes_) if tipo == TipoModelo.classificacao else None,
        classes=list(modelo_treinado.classes_) if tipo == TipoModelo.classificacao else None
    )

    # 2. Criar o pacote (Payload)
    # Usamos o .model_dump() do Pydantic v2 para garantir a serialização
    payload = {
        "modelo": modelo_treinado,
        "metadata": info.model_dump() 
    }

    # 3. Salvar temporariamente para medir o tamanho
    joblib.dump(payload, caminho_final)
    
    # 4. Atualizar o tamanho em MB no metadata (opcional, para precisão)
    tamanho = os.path.getsize(caminho_final) / (1024 * 1024)
    payload["metadata"]["tamanho_mb"] = round(tamanho, 2)
    joblib.dump(payload, caminho_final) # Salva novamente com o tamanho correto

    print(f"✅ Modelo salvo com sucesso em: {caminho_final}")


def carregar_modelo_e_info(caminho_arquivo):
    """
    Carrega o arquivo e retorna o modelo e o objeto InfoModelo validado
    
    Args:
        - caminho_arquivo (Path): Caminho completo do arquivo .joblib a ser carregado.
        
    Returns:
        - modelo: O objeto do modelo treinado.
        - info: Objeto InfoModelo com os metadados do modelo.
    """
    
    pacote = joblib.load(caminho_arquivo)
    
    modelo = pacote["modelo"]
    # Reconstrói o objeto Pydantic a partir do dicionário salvo
    info = InfoModelo(**pacote["metadata"])
    
    return modelo, info

# -----------------------------
# Auxiliadores de escrita e carregamento de arquivos
# -----------------------------
def save_pickle(obj, file_name: str):
    """
    Salvando objeto Python num arquivo atráves do Pickle.
    
    Parameters:
        obj: Python Object
        file_name: Nome do arquivo, deve incluir o tipo '.pkl'.
    Returns:
        None
    """
    if not file_name.endswith('.pkl'):
        raise SyntaxError(f"ERRO: Arquivo {file_name} não possui no final o tipo '.pkl'")
    
    caminho_completo = os.path.join(config_path.MODELS_DIRECTORY_PATH, file_name)
    with open(caminho_completo, 'wb') as f:
        pickle.dump(obj, f)
    
    print(f"Pickle salvou o modelo em '{config_path.MODELS_DIRECTORY_PATH}/{file_name}'")

def load_pickle(file_name: str):
    """
    Carrega um objeto Python de um arquivo pickle.
    
    args:
        file_name (str): Nome do arquivo '.pkl'.
    
    returns
        model: Objeto Python
    """
    
    if not file_name.endswith('pkl'):
        raise SyntaxError(f"ERRO: Arquivo {file_name} não possui no final o tipo '.pkl'")
    
    if not os.path.exists(f"{config_path.MODELS_DIRECTORY_PATH}/{file_name}"):
        raise FileNotFoundError(f"Arquivo não encontrado: {config_path.MODELS_DIRECTORY_PATH}/{file_name}")
    
    try:
        caminho_completo = os.path.join(config_path.MODELS_DIRECTORY_PATH, file_name)
        with open(caminho_completo, 'rb') as f:
            model = pickle.load(f)
            print(f"Pickle carregou o modelo em '{config_path.MODELS_DIRECTORY_PATH}/{file_name}'")
            return model
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_name}: {e}")

def save_joblib(modelo, nome_arquivo: str):
    """
    Salva um modelo de Machine Learning (Scikit-Learn/Joblib) no disco.

    Args:
        modelo: O objeto do modelo treinado.
        nome_arquivo (str): Nome do arquivo.

    Returns:
        bool: True se salvo com sucesso, False se houver erro.
    """
    if not nome_arquivo.endswith('.joblib'):
        raise SyntaxError(f"ERRO: Arquivo {nome_arquivo} não possui no final o tipo '.joblib'")
    
    if not os.path.exists(f"{config_path.MODELS_DIRECTORY_PATH}"):
        raise FileNotFoundError(f"Caminho de diretório não existe: {config_path.MODELS_DIRECTORY_PATH}")
    
    caminho_completo = os.path.join(config_path.MODELS_DIRECTORY_PATH, nome_arquivo)
    joblib.dump(modelo, caminho_completo)
    print(f"Joblib salvou o modelo em: {nome_arquivo}")

def load_joblib(nome_arquivo: str):
    """
    Carrega um modelo a partir de um arquivo .joblib.
    
    args:
        nome_arquivo (str): Nome do arquivo
    """
    if not nome_arquivo.endswith('.joblib'):
        raise SyntaxError(f"ERRO: Arquivo {nome_arquivo} não possui no final o tipo '.joblib'")
    
    if not os.path.exists(f"{config_path.MODELS_DIRECTORY_PATH}/{nome_arquivo}"):
        raise FileNotFoundError(f"Arquivo {nome_arquivo} não existe no diretório 'models'")
    
    try:
        caminho_completo = os.path.join(config_path.MODELS_DIRECTORY_PATH, nome_arquivo)
        modelo = joblib.load(caminho_completo)
        print(f"Modelo carregado de: {nome_arquivo}")
        return modelo
    except Exception as e:
        print(f"Erro inesperado ocorreu: {e}")

def ensure_dir(path: Path | str):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)