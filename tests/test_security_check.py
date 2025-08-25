#!/usr/bin/env python3
"""
Testes básicos para o módulo security_check
"""

import os
import pytest
import subprocess
from unittest.mock import patch, MagicMock
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import security_check


class TestSecurityCheck:
    """Testes básicos para o script de verificação de segurança"""

    def test_module_importable(self):
        """Testa se o módulo pode ser importado"""
        assert security_check is not None

    def test_run_command_sucesso(self):
        """Testa execução bem-sucedida de comando"""
        success, stdout, stderr = security_check.run_command(
            ["python", "--version"], "Teste versão Python"
        )
        assert success is True
        assert "Python" in stdout
        assert stderr == ""

    def test_run_command_erro(self):
        """Testa comando que falha"""
        success, stdout, stderr = security_check.run_command(
            ["comando_inexistente_123"], "Comando inexistente"
        )
        assert success is False

    def test_run_command_timeout(self):
        """Testa timeout de comando"""
        # Simular comando longo em sistemas Windows
        with patch("security_check.subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.TimeoutExpired("cmd", 60)
            success, stdout, stderr = security_check.run_command(
                ["sleep", "10"], "Comando longo"
            )
            assert success is False
            assert stderr == "Timeout"

    def test_run_command_string_input(self):
        """Testa comando passado como string"""
        success, stdout, stderr = security_check.run_command(
            "python --version", "Teste string"
        )
        assert success is True
        assert "Python" in stdout

    def test_check_file_permissions(self):
        """Testa verificação de permissões"""
        result = security_check.check_file_permissions()
        assert result is True

    def test_security_fix_present(self):
        """Testa se o código tem chamadas seguras de subprocess"""
        with open(security_check.__file__, "r", encoding="utf-8") as f:
            content = f.read()

        # Verifica se usa shell=False (mais seguro)
        assert "shell=False" in content
        # Verifica se o timeout de segurança está presente
        assert "timeout=60" in content

    def test_file_exists(self):
        """Testa se o arquivo do módulo existe"""
        module_file = security_check.__file__
        assert os.path.exists(module_file)

    def test_module_has_main_code(self):
        """Testa se o módulo tem código principal"""
        # Lê o arquivo e verifica se tem código
        with open(security_check.__file__, "r", encoding="utf-8") as f:
            content = f.read()

        # Verifica se tem imports básicos e função main
        assert "import" in content
        assert "def main(" in content
        assert "def run_command(" in content
