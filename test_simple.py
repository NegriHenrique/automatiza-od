"""
Testes simples e rápidos para verificação pre-commit
"""

import pytest
import os
from pathlib import Path


def test_projeto_estrutura():
    """Testa se a estrutura básica do projeto está correta."""
    arquivos_obrigatorios = [
        "gerar_od.py",
        "gerar_od_gui.py",
        "gerador_od_completo.py",
        "build_exe.py",
        "requirements.txt",
        "config_dias_filmagem.json",
    ]

    for arquivo in arquivos_obrigatorios:
        assert os.path.exists(arquivo), f"Arquivo obrigatório não encontrado: {arquivo}"


def test_imports_principais():
    """Testa se os imports principais funcionam."""
    try:
        import gerador_od_completo

        # Teste básico - apenas verifica se o módulo core existe
        assert hasattr(gerador_od_completo, "GeradorODCompleto")
        assert True
    except ImportError as e:
        pytest.fail(f"Erro ao importar módulo core: {e}")


def test_config_valida():
    """Testa se o arquivo de configuração é válido JSON."""
    import json

    try:
        with open("config_dias_filmagem.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        # Testa se é um JSON válido - estrutura pode variar
        assert isinstance(config, dict)
        assert len(config) > 0
    except Exception as e:
        pytest.fail(f"Erro ao ler configuração: {e}")


def test_pasta_arquivos_existe():
    """Testa se a pasta arquivos existe."""
    pasta_arquivos = Path("arquivos")
    assert pasta_arquivos.exists(), "Pasta 'arquivos' não encontrada"

    pasta_ods = pasta_arquivos / "ODs"
    assert pasta_ods.exists(), "Pasta 'arquivos/ODs' não encontrada"
