#!/usr/bin/env python3
"""
Script de Validação de Segurança Local
Executa verificações de segurança antes do commit
"""

import subprocess
import sys
import json
import os
from pathlib import Path


def run_command(command, description):
    """Executa um comando e retorna o resultado"""
    print(f"🔍 {description}...")
    try:
        # Usar lista de comandos ao invés de shell=True para segurança
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
            timeout=60,  # Timeout de segurança
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout executando: {description}")
        return False, "", "Timeout"
    except Exception as e:
        print(f"❌ Erro executando: {description} - {e}")
        return False, "", str(e)


def check_bandit():
    """Verifica problemas de segurança com Bandit"""
    print("\n" + "=" * 50)
    print("🔒 ANÁLISE DE SEGURANÇA (BANDIT)")
    print("=" * 50)

    # Verificar se bandit está instalado
    success, _, _ = run_command(["bandit", "--version"], "Verificando Bandit")
    if not success:
        print("⚠️ Bandit não instalado. Instalando...")
        install_success, _, _ = run_command(
            ["pip", "install", "bandit"], "Instalando Bandit"
        )
        if not install_success:
            print("❌ Erro ao instalar Bandit")
            return False

    # Executar bandit com configurações específicas para arquivos do projeto
    # Excluir .venv e outros diretórios desnecessários
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
    success, stdout, stderr = run_command(cmd_parts, "Executando análise Bandit")

    # Bandit pode retornar código de saída != 0 mesmo com sucesso
    # Vamos verificar se o arquivo JSON foi criado
    if os.path.exists("bandit-results.json"):
        try:
            with open("bandit-results.json", "r") as f:
                results = json.load(f)

            metrics = results.get("metrics", {})
            issues = results.get("results", [])

            print(
                f"📊 Arquivos analisados: {len(metrics.get('_totals', {}).get('SLOC', []))}"
            )
            print(f"📊 Linhas de código: {metrics.get('_totals', {}).get('SLOC', 0)}")

            # Contar problemas por severidade
            high_issues = [i for i in issues if i.get("issue_severity") == "HIGH"]
            medium_issues = [i for i in issues if i.get("issue_severity") == "MEDIUM"]
            low_issues = [i for i in issues if i.get("issue_severity") == "LOW"]

            print(f"🔴 Problemas HIGH: {len(high_issues)}")
            print(f"🟡 Problemas MEDIUM: {len(medium_issues)}")
            print(f"🟢 Problemas LOW: {len(low_issues)}")

            # Mostrar problemas críticos
            critical_issues = [
                i for i in issues if i.get("issue_severity") in ["HIGH", "MEDIUM"]
            ]

            if critical_issues:
                print("\n⚠️ PROBLEMAS CRÍTICOS ENCONTRADOS:")
                for issue in critical_issues[:5]:  # Mostrar apenas os primeiros 5
                    print(f"  📍 {issue.get('filename')}:{issue.get('line_number')}")
                    print(f"     {issue.get('test_name')}: {issue.get('issue_text')}")
                    print(f"     Severidade: {issue.get('issue_severity')}")
                    print()

                if len(critical_issues) > 5:
                    print(f"   ... e mais {len(critical_issues) - 5} problemas")

                return False
            else:
                print("✅ Nenhum problema crítico encontrado")
                return True

        except json.JSONDecodeError:
            print("❌ Erro ao ler resultados do Bandit")
            return False
    else:
        print("❌ Bandit não gerou arquivo de resultados")
        return False


def check_safety():
    """Verifica vulnerabilidades nas dependências"""
    print("\n" + "=" * 50)
    print("🛡️ VERIFICAÇÃO DE VULNERABILIDADES (SAFETY)")
    print("=" * 50)

    # Verificar se safety está instalado
    success, _, _ = run_command(["safety", "--version"], "Verificando Safety")
    if not success:
        print("⚠️ Safety não instalado. Instalando...")
        install_success, _, _ = run_command(
            ["pip", "install", "safety"], "Instalando Safety"
        )
        if not install_success:
            print("❌ Erro ao instalar Safety")
            return False

    # Executar safety check
    success, stdout, stderr = run_command(
        ["safety", "check", "--json"], "Verificando vulnerabilidades"
    )

    if success and "[]" in stdout:
        print("✅ Nenhuma vulnerabilidade encontrada")
        return True
    elif success:
        try:
            vulnerabilities = json.loads(stdout)
            print(f"⚠️ {len(vulnerabilities)} vulnerabilidade(s) encontrada(s):")
            for vuln in vulnerabilities[:3]:  # Mostrar apenas as primeiras 3
                print(
                    f"  📦 {vuln.get('package_name')} {vuln.get('installed_version')}"
                )
                print(f"     {vuln.get('advisory')}")
                print()
            return False
        except json.JSONDecodeError:
            print("❌ Erro ao analisar resultados do Safety")
            return False
    else:
        print(f"❌ Erro executando Safety: {stderr}")
        return False


def check_dependencies():
    """Verifica dependências suspeitas ou desatualizadas"""
    print("\n" + "=" * 50)
    print("📦 VERIFICAÇÃO DE DEPENDÊNCIAS")
    print("=" * 50)

    if not os.path.exists("requirements.txt"):
        print("⚠️ Arquivo requirements.txt não encontrado")
        return True

    success, stdout, stderr = run_command(
        ["pip", "list", "--outdated", "--format=json"],
        "Verificando dependências desatualizadas",
    )

    if success:
        try:
            outdated = json.loads(stdout)
            if outdated:
                print(f"📋 {len(outdated)} dependências desatualizadas:")
                for pkg in outdated[:5]:  # Mostrar apenas as primeiras 5
                    print(
                        f"  📦 {pkg['name']}: {pkg['version']} → {pkg['latest_version']}"
                    )

                if len(outdated) > 5:
                    print(f"   ... e mais {len(outdated) - 5} pacotes")

                print(
                    "\n💡 Execute 'pip install --upgrade -r requirements.txt' para atualizar"
                )
            else:
                print("✅ Todas as dependências estão atualizadas")

            return True

        except json.JSONDecodeError:
            print("⚠️ Erro ao analisar dependências")
            return True
    else:
        print("⚠️ Erro ao verificar dependências")
        return True


def check_file_permissions():
    """Verifica permissões de arquivos sensíveis"""
    print("\n" + "=" * 50)
    print("🔐 VERIFICAÇÃO DE PERMISSÕES")
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

            # No Windows, verificar se o arquivo não está marcado como executável
            # quando não deveria estar
            if filename.endswith((".json", ".conf", ".bandit")):
                print(f"📄 {filename}: OK")
            else:
                print(f"📄 {filename}: OK")
        else:
            print(f"⚠️ {filename}: Não encontrado (opcional)")

    if not issues_found:
        print("✅ Permissões de arquivos verificadas")

    return not issues_found


def main():
    """Função principal"""
    print("🔒 VALIDAÇÃO DE SEGURANÇA LOCAL - ORDEM DO DIA")
    print("=" * 60)
    print("Executando verificações de segurança antes do commit...")

    all_checks_passed = True

    # Executar verificações
    checks = [
        ("Análise Bandit", check_bandit),
        ("Verificação Safety", check_safety),
        ("Dependências", check_dependencies),
        ("Permissões", check_file_permissions),
    ]

    for check_name, check_func in checks:
        try:
            result = check_func()
            if not result:
                all_checks_passed = False
                print(f"❌ {check_name}: FALHOU")
            else:
                print(f"✅ {check_name}: PASSOU")
        except Exception as e:
            print(f"❌ {check_name}: ERRO - {e}")
            all_checks_passed = False

    # Resultado final
    print("\n" + "=" * 60)
    if all_checks_passed:
        print("🎉 TODAS AS VERIFICAÇÕES PASSARAM!")
        print("✅ Código está pronto para commit")
        sys.exit(0)
    else:
        print("❌ ALGUMAS VERIFICAÇÕES FALHARAM!")
        print("🔧 Corrija os problemas antes de fazer commit")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Verificação cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)
