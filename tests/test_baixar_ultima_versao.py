#!/usr/bin/env python3
"""
Testes básicos para o módulo baixar_ultima_versao
"""

import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import baixar_ultima_versao


class TestBaixarUltimaVersao:
    """Testes básicos para o script de download da última versão"""

    def test_module_importable(self):
        """Testa se o módulo pode ser importado"""
        assert baixar_ultima_versao is not None

    def test_verificar_imports(self):
        """Testa se todos os imports necessários estão disponíveis"""
        try:
            import requests
            import os
            import json

            # Se chegou até aqui, os imports estão OK
            assert True
        except ImportError:
            pytest.fail("Imports necessários não estão disponíveis")

    def test_file_exists(self):
        """Testa se o arquivo do módulo existe"""
        module_file = baixar_ultima_versao.__file__
        assert os.path.exists(module_file)

    def test_module_has_main_code(self):
        """Testa se o módulo tem código principal"""
        # Lê o arquivo e verifica se tem código
        with open(baixar_ultima_versao.__file__, "r", encoding="utf-8") as f:
            content = f.read()

        # Verifica se tem imports básicos e função main ou código
        assert "import" in content
        assert "requests" in content
        assert "timeout" in content  # Verifica se a correção de segurança está presente

    def test_security_fix_present(self):
        """Testa se a correção de segurança (timeout) está presente"""
        with open(baixar_ultima_versao.__file__, "r", encoding="utf-8") as f:
            content = f.read()

        # Verifica se timeout=30 está presente (correção B113)
        assert "timeout=30" in content or "timeout = 30" in content
