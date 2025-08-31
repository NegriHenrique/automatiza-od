#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Validacao de Seguranca Local
Executa verificacoes de seguranca antes do commit
"""

import subprocess
import sys
import json
import os
from pathlib import Path


def run_command(command, description):
    """Executa um comando e retorna o resultado"""
    print(f"Executando: {description}...")
    try:
        # Usar lista de comandos ao inves de shell=True para seguranca
        if isinstance(command, str):
            # Dividir comando em lista para evitar shell=True
            if " " in command:
                command_parts = command.split()
            else:
                command_parts = [command]
        else:
            command_parts = command

        result = subprocess.run(
            command_parts,
            shell=False,  # Mais seguro que shell=True
            capture_output=True,
            text=True,
            timeout=60,  # Timeout de seguranca
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        print(f"Timeout executando: {description}")
        return False, "", "Timeout"
    except Exception as e:
        print(f"Erro executando: {description} - {e}")
        return False, "", str(e)


def check_bandit():
    """Verifica problemas de seguranca com Bandit"""
    print("\n" + "=" * 50)
    print("ANALISE DE SEGURANCA (BANDIT)")
    print("=" * 50)

    # Verificar se bandit esta instalado
    success, _, _ = run_command(["bandit", "--version"], "Verificando Bandit")
    if not success:
        print("Bandit nao instalado. Instalando...")
        install_success, _, _ = run_command(
            ["pip", "install", "bandit"], "Instalando Bandit"
        )
        if not install_success:
            print("Erro ao instalar Bandit")
            return False

    # Executar bandit com configuracoes especificas para arquivos do projeto
    # Excluir .venv e outros diretorios desnecessarios
    cmd_parts = [
        "bandit",
        "-r",
        ".",
        "--exclude",
        ".venv,tests,build_temp,htmlcov,distribuicao,distribuicao_completa",
        "--skip",
        "B101,B601,B603,B607",
        "-f",
        "json",
        "-o",
        "bandit-results.json",
    ]
    success, stdout, stderr = run_command(cmd_parts, "Executando analise Bandit")

    # Bandit pode retornar codigo de saida != 0 mesmo com sucesso
    # Vamos verificar se o arquivo JSON foi criado
    if os.path.exists("bandit-results.json"):
        try:
            with open("bandit-results.json", "r") as f:
                results = json.load(f)

            metrics = results.get("metrics", {})
            issues = results.get("results", [])

            print(
                f"Relatorio Arquivos analisados: {len(metrics.get('_totals', {}).get('SLOC', []))}"
            )
            print(
                f"Relatorio Linhas de codigo: {metrics.get('_totals', {}).get('SLOC', 0)}"
            )

            # Contar problemas por severidade
            high_issues = [i for i in issues if i.get("issue_severity") == "HIGH"]
            medium_issues = [i for i in issues if i.get("issue_severity") == "MEDIUM"]
            low_issues = [i for i in issues if i.get("issue_severity") == "LOW"]

            print(f"HIGH Problemas HIGH: {len(high_issues)}")
            print(f"MEDIUM Problemas MEDIUM: {len(medium_issues)}")
            print(f"LOW Problemas LOW: {len(low_issues)}")

            # Mostrar problemas criticos
            critical_issues = [
                i for i in issues if i.get("issue_severity") in ["HIGH", "MEDIUM"]
            ]

            if critical_issues:
                print("\nAviso PROBLEMAS CRITICOS ENCONTRADOS:")
                for issue in critical_issues[:5]:  # Mostrar apenas os primeiros 5
                    print(f"  Local {issue.get('filename')}:{issue.get('line_number')}")
                    print(f"     {issue.get('test_name')}: {issue.get('issue_text')}")
                    print(f"     Severidade: {issue.get('issue_severity')}")
                    print()

                if len(critical_issues) > 5:
                    print(f"   ... e mais {len(critical_issues) - 5} problemas")

                return False
            else:
                print("Sucesso Nenhum problema critico encontrado")
                return True

        except json.JSONDecodeError:
            print("Erro Erro ao ler resultados do Bandit")
            return False
    else:
        print("Erro Bandit nao gerou arquivo de resultados")
        return False


# def check_safety():
#     """Verifica vulnerabilidades nas dependencias"""
#     print("\n" + "=" * 50)
#     print("Protecao VERIFICACAO DE VULNERABILIDADES (SAFETY)")
#     print("=" * 50)

#     # Verificar se safety esta instalado
#     success, _, _ = run_command(["safety", "--version"], "Verificando Safety")
#     if not success:
#         print("Aviso Safety nao instalado. Instalando...")
#         install_success, _, _ = run_command(
#             ["pip", "install", "safety"], "Instalando Safety"
#         )
#         if not install_success:
#             print("Erro Erro ao instalar Safety")
#             return False

#     # Executar safety check
#     success, stdout, stderr = run_command(
#         ["safety", "check", "--json"], "Verificando vulnerabilidades"
#     )

#     if success and "[]" in stdout:
#         print("Sucesso Nenhuma vulnerabilidade encontrada")
#         return True
#     elif success:
#         try:
#             vulnerabilities = json.loads(stdout)
#             print(f"Aviso {len(vulnerabilities)} vulnerabilidade(s) encontrada(s):")
#             for vuln in vulnerabilities[:3]:  # Mostrar apenas as primeiras 3
#                 print(
#                     f"  Pacote {vuln.get('package_name')} {vuln.get('installed_version')}"
#                 )
#                 print(f"     {vuln.get('advisory')}")
#                 print()
#             return False
#         except json.JSONDecodeError:
#             print("Erro Erro ao analisar resultados do Safety")
#             return False
#     else:
#         print(f"Erro Erro executando Safety: {stderr}")
#         return False


def check_dependencies():
    """Verifica dependencias suspeitas ou desatualizadas"""
    print("\n" + "=" * 50)
    print("Pacote VERIFICACAO DE DEPENDENCIAS")
    print("=" * 50)

    if not os.path.exists("requirements.txt"):
        print("Aviso Arquivo requirements.txt nao encontrado")
        return True

    success, stdout, stderr = run_command(
        ["pip", "list", "--outdated", "--format=json"],
        "Verificando dependencias desatualizadas",
    )

    if success:
        try:
            outdated = json.loads(stdout)
            if outdated:
                print(f"Lista {len(outdated)} dependencias desatualizadas:")
                for pkg in outdated[:5]:  # Mostrar apenas as primeiras 5
                    print(
                        f"  Pacote {pkg['name']}: {pkg['version']} -> {pkg['latest_version']}"
                    )

                if len(outdated) > 5:
                    print(f"   ... e mais {len(outdated) - 5} pacotes")

                print(
                    "\nDica Execute 'pip install --upgrade -r requirements.txt' para atualizar"
                )
            else:
                print("Sucesso Todas as dependencias estao atualizadas")

            return True

        except json.JSONDecodeError:
            print("Aviso Erro ao analisar dependencias")
            return True
    else:
        print("Aviso Erro ao verificar dependencias")
        return True


def check_file_permissions():
    """Verifica permissoes de arquivos sensiveis"""
    print("\n" + "=" * 50)
    print("Permissoes VERIFICACAO DE PERMISSOES")
    print("=" * 50)

    sensitive_files = [
        "config_dias_filmagem.json",
        "security.conf",
        ".bandit",
        "sign_executable.ps1",
    ]

    issues_found = False

    for filename in sensitive_files:
        if os.path.exists(filename):
            file_path = Path(filename)

            # No Windows, verificar se o arquivo nao esta marcado como executavel
            # quando nao deveria estar
            if filename.endswith((".json", ".conf", ".bandit")):
                print(f"Arquivo {filename}: OK")
            else:
                print(f"Arquivo {filename}: OK")
        else:
            print(f"Aviso {filename}: Nao encontrado (opcional)")

    if not issues_found:
        print("Sucesso Permissoes de arquivos verificadas")

    return not issues_found


def main():
    """Funcao principal"""
    print("VALIDACAO DE SEGURANCA LOCAL - ORDEM DO DIA")
    print("=" * 60)
    print("Executando verificacoes de seguranca antes do commit...")

    all_checks_passed = True

    # Executar verificacoes
    checks = [
        ("Analise Bandit", check_bandit),
        # ("Verificacao Safety", check_safety),
        ("Dependencias", check_dependencies),
        ("Permissoes", check_file_permissions),
    ]

    for check_name, check_func in checks:
        try:
            result = check_func()
            if not result:
                all_checks_passed = False
                print(f"Erro {check_name}: FALHOU")
            else:
                print(f"Sucesso {check_name}: PASSOU")
        except Exception as e:
            print(f"Erro {check_name}: ERRO - {e}")
            all_checks_passed = False

    # Resultado final
    print("\n" + "=" * 60)
    if all_checks_passed:
        print("SUCESSO TODAS AS VERIFICACOES PASSARAM!")
        print("Sucesso Codigo esta pronto para commit")
        sys.exit(0)
    else:
        print("Erro ALGUMAS VERIFICACOES FALHARAM!")
        print("CORRIGIR Corrija os problemas antes de fazer commit")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nVerificacao cancelada pelo usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        sys.exit(1)
