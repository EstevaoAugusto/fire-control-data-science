from __future__ import annotations

import pandas as pd
from fastapi import HTTPException
import os
import sys
from pathlib import Path



sys.path.append('./../../..')  # Ajuste para garantir acesso ao config_path

from config_path import RAW_DATA_DIRECTORY_PATH, PROCESSED_DATA_DIRECTORY_PATH
from schemas.schemas import InfoDataset, AmostraDataset, FiltrosDataset

# ──────────────────────────────────────────────
#  Dataset fixo
# ──────────────────────────────────────────────
NOME_DATASET       = "bdqueimadas_completo.parquet"
_CAMINHO_PROCESSED = PROCESSED_DATA_DIRECTORY_PATH / NOME_DATASET
_CAMINHO_RAW       = RAW_DATA_DIRECTORY_PATH       / NOME_DATASET


def _caminho_dataset():
    """Prioriza processed/, cai em raw/ se não encontrar."""
    if _CAMINHO_PROCESSED.exists():
        return _CAMINHO_PROCESSED
    if _CAMINHO_RAW.exists():
        return _CAMINHO_RAW
    raise HTTPException(
        status_code=404,
        detail=(
            f"Dataset '{NOME_DATASET}' não encontrado. Esperado em:\n"
            f"  {_CAMINHO_PROCESSED}\n  {_CAMINHO_RAW}"
        ),
    )


# ──────────────────────────────────────────────
#  Cache do DataFrame
# ──────────────────────────────────────────────
_df_cache: pd.DataFrame | None = None


def _carregar_df() -> pd.DataFrame:
    """Carrega o Parquet uma única vez e mantém em cache."""
    global _df_cache
    if _df_cache is None:
        caminho = _caminho_dataset()
        try:
            _df_cache = pd.read_parquet(caminho)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao ler o Parquet: {str(e)}")
    return _df_cache


def invalidar_cache() -> dict:
    global _df_cache
    _df_cache = None
    return {"mensagem": "Cache do dataset liberado com sucesso."}


# ──────────────────────────────────────────────
#  Funções públicas
# ──────────────────────────────────────────────
def obter_info() -> InfoDataset:
    caminho = _caminho_dataset()
    df      = _carregar_df()

    tamanho_mb     = round(caminho.stat().st_size / (1024 * 1024), 3)
    periodo_inicio = periodo_fim = None

    if "DataHora" in df.columns:
        try:
            periodo_inicio = str(df["DataHora"].min())
            periodo_fim    = str(df["DataHora"].max())
        except Exception:
            pass

    biomas = sorted(df["Bioma"].dropna().unique().tolist())   if "Bioma"   in df.columns else None
    ufs    = sorted(df["Nome_UF"].dropna().unique().tolist()) if "Nome_UF" in df.columns else None

    return InfoDataset(
        nome             = NOME_DATASET,
        caminho          = str(caminho),
        linhas           = len(df),
        colunas          = len(df.columns),
        tamanho_mb       = tamanho_mb,
        colunas_nomes    = df.columns.tolist(),
        nulos_por_coluna = df.isnull().sum().to_dict(),
        periodo_inicio   = periodo_inicio,
        periodo_fim      = periodo_fim,
        biomas_presentes = biomas,
        ufs_presentes    = ufs,
    )


def obter_amostra(n_linhas: int = 10) -> AmostraDataset:
    df = _carregar_df()
    return AmostraDataset(
        colunas      = df.columns.tolist(),
        dados        = df.head(n_linhas).fillna("null").to_dict(orient="records"),
        total_linhas = len(df),
    )


def obter_dados_filtrados(filtros: FiltrosDataset) -> AmostraDataset:
    df = _carregar_df().copy()

    if filtros.ano      is not None and "Ano"      in df.columns:
        df = df[df["Ano"] == filtros.ano]
    if filtros.mes      is not None and "Mes"      in df.columns:
        df = df[df["Mes"] == filtros.mes]
    if filtros.bioma    and "Bioma"    in df.columns:
        df = df[df["Bioma"].str.contains(filtros.bioma, case=False, na=False)]
    if filtros.nome_uf  and "Nome_UF"  in df.columns:
        df = df[df["Nome_UF"].str.contains(filtros.nome_uf, case=False, na=False)]
    if filtros.risco_fogo_min is not None and "RiscoFogo" in df.columns:
        df = df[df["RiscoFogo"] >= filtros.risco_fogo_min]
    if filtros.risco_fogo_max is not None and "RiscoFogo" in df.columns:
        df = df[df["RiscoFogo"] <= filtros.risco_fogo_max]

    if df.empty:
        raise HTTPException(status_code=404, detail="Nenhum registro encontrado com os filtros informados.")

    return AmostraDataset(
        colunas      = df.columns.tolist(),
        dados        = df.head(filtros.n_linhas).fillna("null").to_dict(orient="records"),
        total_linhas = len(df),
    )


def obter_estatisticas() -> dict:
    df = _carregar_df()
    return df.describe(include="number").round(4).to_dict()


def obter_valores_unicos(coluna: str) -> dict:
    df = _carregar_df()
    if coluna not in df.columns:
        raise HTTPException(
            status_code=404,
            detail=f"Coluna '{coluna}' não existe. Disponíveis: {df.columns.tolist()}",
        )
    valores = sorted(df[coluna].dropna().unique().tolist())
    return {"coluna": coluna, "total": len(valores), "valores": valores}