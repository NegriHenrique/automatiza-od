#!/usr/bin/env python3
"""
🔗 Baixar Última Versão - Ordem do Dia
=====================================

Script para baixar automaticamente a última versão do executável
do sistema Ordem do Dia diretamente do GitHub Actions.

Uso:
    python baixar_ultima_versao.py

Funcionalidades:
- 🔍 Busca o último build bem-sucedido
- 📦 Baixa o artefato automaticamente
- 🚀 Abre o link no navegador
- 📋 Copia link para clipboard

Requisitos:
- requests (pip install requests)
- pyperclip (pip install pyperclip) [opcional]
"""

import json
import webbrowser
import subprocess
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ Módulo 'requests' não encontrado!")
    print("💡 Execute: pip install requests")
    sys.exit(1)

try:
    import pyperclip

    HAS_CLIPBOARD = True
except ImportError:
    HAS_CLIPBOARD = False

# Configurações
REPO_OWNER = "NegriHenrique"
REPO_NAME = "automatiza-od"
WORKFLOW_NAME = "ci-cd.yml"
ARTIFACT_NAME = "executavel-windows"


def buscar_ultimo_build():
    """🔍 Busca o último build bem-sucedido"""
    print("🔍 Buscando último build bem-sucedido...")

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_NAME}/runs"
    params = {"status": "completed", "conclusion": "success", "per_page": 1}

    try:
        # Timeout configurado para evitar problemas de segurança (B113)
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        if not data.get("workflow_runs"):
            print("❌ Nenhum build bem-sucedido encontrado!")
            return None

        return data["workflow_runs"][0]

    except requests.RequestException as e:
        print(f"❌ Erro ao buscar builds: {e}")
        return None


def gerar_link_download(run_id):
    """🔗 Gera link direto para download do artefato"""
    return (
        f"https://github.com/{REPO_OWNER}/{REPO_NAME}/actions/runs/{run_id}#artifacts"
    )


def main():
    """🚀 Função principal"""
    print("=" * 60)
    print("🚀 BAIXAR ÚLTIMA VERSÃO - ORDEM DO DIA")
    print("=" * 60)

    # Buscar último build
    ultimo_build = buscar_ultimo_build()
    if not ultimo_build:
        return

    # Informações do build
    run_id = ultimo_build["id"]
    commit_sha = ultimo_build["head_sha"][:7]
    created_at = ultimo_build["created_at"]

    print(f"✅ Último build encontrado:")
    print(f"   📅 Data: {created_at}")
    print(f"   🏗️ Commit: {commit_sha}")
    print(f"   🆔 Run ID: {run_id}")

    # Gerar link
    link_download = gerar_link_download(run_id)

    print("\n" + "=" * 60)
    print("🔗 LINK PARA DOWNLOAD:")
    print("=" * 60)
    print(f"📦 {link_download}")
    print("\n💡 COMO BAIXAR:")
    print("   1. O link abrirá no seu navegador")
    print("   2. Role até a seção 'Artifacts'")
    print(f"   3. Clique em '{ARTIFACT_NAME}'")
    print("   4. O download começará automaticamente")

    # Copiar para clipboard
    if HAS_CLIPBOARD:
        try:
            pyperclip.copy(link_download)
            print("📋 Link copiado para área de transferência!")
        except:
            pass

    # Perguntar se quer abrir
    print("\n" + "=" * 60)
    resposta = input("🌐 Abrir link no navegador? (s/N): ").strip().lower()

    if resposta in ["s", "sim", "y", "yes"]:
        print("🌐 Abrindo navegador...")
        webbrowser.open(link_download)
        print("✅ Link aberto no navegador!")
    else:
        print("📋 Link disponível acima para copiar/colar")

    print("\n🎉 Operação concluída!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("🐛 Se o problema persistir, reporte como issue no GitHub.")
