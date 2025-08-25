# 🎨 Padrões de Código - Ordem do Dia

## 🎯 Filosofia de Desenvolvimento

### Princípios Fundamentais
1. **Clareza sobre Brevidade**: Código deve ser legível, não necessariamente conciso
2. **Acessibilidade First**: Toda interface deve seguir WCAG 2.1
3. **Feedback Imediato**: Usuário sempre deve saber o que está acontecendo
4. **Robustez**: Sistema deve falhar graciosamente
5. **Manutenibilidade**: Código deve ser fácil de modificar

## 🏗️ Estrutura de Arquivos

### Organização do Projeto
```
ordem-do-dia/
├── 📄 gerar_od.py              # Entry point principal
├── 🖥️ gerar_od_gui.py          # Interface gráfica  
├── ⚙️ gerador_od_completo.py    # Core business logic
├── 🔨 build_exe.py             # Sistema de build
├── 📋 requirements.txt         # Dependências
├── ⚙️ config_dias_filmagem.json # Configuração
├── 🧪 pytest.ini              # Configuração de testes
├── 📁 tests/                   # Testes automatizados
├── 📁 arquivos/                # Dados de entrada/saída
├── 📁 .github/                 # Documentação e CI/CD
└── 📄 README.md               # Documentação principal
```

### Convenções de Nomenclatura

#### Arquivos e Diretórios
```python
# ✅ Bom
gerar_od_gui.py
gerador_od_completo.py
test_integration.py
config_dias_filmagem.json

# ❌ Evitar
geradorOD.py
Gerador-OD.py
testIntegration.py
config.json
```

#### Variáveis e Funções
```python
# ✅ Bom - Snake case, descritivo
def verificar_arquivos_necessarios():
    dias_disponiveis = []
    caminho_arquivo_pdf = "arquivos/PLANO_FINAL.pdf"
    
# ❌ Evitar - CamelCase, nomes genéricos
def checkFiles():
    data = []
    path = "file.pdf"
```

#### Classes
```python
# ✅ Bom - PascalCase, substantivos descritivos
class GeradorODCompleto:
class ToastNotification:
class ProcessadorPDF:

# ❌ Evitar - Nomes genéricos ou verbos
class Generator:
class ProcessFile:
class Data:
```

#### Constantes
```python
# ✅ Bom - UPPER_SNAKE_CASE
MAX_FILE_SIZE = 50 * 1024 * 1024
DEFAULT_ENCODING = "utf-8"
TOAST_DURATION = 3000

# Cores em hexadecimal
COLOR_PRIMARY = "#007bff"
COLOR_SUCCESS = "#28a745"
COLOR_ERROR = "#dc3545"
```

## 🎨 Padrões de Interface (GUI)

### Paleta de Cores Acessível

```python
# Design System - Bootstrap inspired
COLORS = {
    # Primary Brand Colors
    "primary": "#007bff",           # Blue - Ações principais
    "primary_hover": "#0056b3",     # Blue hover
    
    # Semantic Colors
    "success": "#28a745",           # Green - Sucesso
    "success_hover": "#218838",
    "error": "#dc3545",             # Red - Erro  
    "error_hover": "#c82333",
    "warning": "#ffc107",           # Yellow - Aviso
    "warning_text": "#856404",      # Dark yellow para contraste
    "info": "#17a2b8",              # Teal - Informação
    
    # Neutral Colors
    "background": "#f8f9fa",        # Light gray - Fundo principal
    "surface": "#ffffff",           # White - Cards e modais
    "text_primary": "#212529",      # Near black - Texto principal
    "text_secondary": "#6c757d",    # Medium gray - Texto secundário
    "border": "#dee2e6",            # Light border
    "disabled": "#e9ecef",          # Disabled states
}

# Verificação de contraste (WCAG 2.1)
CONTRAST_REQUIREMENTS = {
    "text_normal": 4.5,      # AA compliance
    "text_large": 3.0,       # AA compliance  
    "text_enhanced": 7.0,    # AAA compliance
    "ui_components": 3.0     # AA compliance
}
```

### Tipografia

```python
TYPOGRAPHY = {
    "font_family": "Segoe UI",      # Native Windows font
    "fallbacks": "Tahoma, Arial, sans-serif",
    
    "sizes": {
        "display": 32,              # Título principal
        "h1": 24,                   # Títulos de seção
        "h2": 20,                   # Subtítulos
        "h3": 16,                   # Labels importantes
        "body": 12,                 # Texto padrão
        "small": 10,                # Texto pequeno/rodapé
        "button": 12,               # Texto de botões
    },
    
    "weights": {
        "normal": "normal",
        "medium": "bold",           # CustomTkinter só suporta normal/bold
        "bold": "bold"
    },
    
    "line_height": 1.4,             # Para boa legibilidade
}
```

### Componentes UI

#### Botões
```python
# Botão Primário - Ações principais
btn_primary = ctk.CTkButton(
    parent,
    text="🚀 Ação Principal",
    font=ctk.CTkFont(size=12, weight="bold"),
    fg_color="#007bff",             # Azul
    hover_color="#0056b3",          # Azul escuro
    text_color="#ffffff",           # Branco
    height=40,
    corner_radius=8
)

# Botão Sucesso - Confirmações
btn_success = ctk.CTkButton(
    parent,
    text="✅ Confirmar",
    fg_color="#28a745",             # Verde
    hover_color="#218838",
    text_color="#ffffff"
)

# Botão Perigo - Ações destrutivas  
btn_danger = ctk.CTkButton(
    parent,
    text="🗑️ Excluir",
    fg_color="#dc3545",             # Vermelho
    hover_color="#c82333",
    text_color="#ffffff"
)

# Botão Secundário - Ações auxiliares
btn_secondary = ctk.CTkButton(
    parent,
    text="📂 Auxiliar",
    fg_color="#6c757d",             # Cinza
    hover_color="#5a6268",
    text_color="#ffffff"
)
```

#### Labels e Textos
```python
# Título de Seção
section_title = ctk.CTkLabel(
    parent,
    text="📊 Título da Seção",
    font=ctk.CTkFont(size=16, weight="bold"),
    text_color="#212529"            # Preto para máximo contraste
)

# Texto de Status - Sucesso
status_success = ctk.CTkLabel(
    parent,
    text="✅ Operação bem-sucedida",
    text_color="#28a745",           # Verde
    font=ctk.CTkFont(size=12)
)

# Texto de Status - Erro
status_error = ctk.CTkLabel(
    parent,
    text="❌ Erro encontrado",
    text_color="#dc3545",           # Vermelho
    font=ctk.CTkFont(size=12)
)

# Texto Secundário
subtitle = ctk.CTkLabel(
    parent,
    text="Informação adicional",
    text_color="#6c757d",           # Cinza médio
    font=ctk.CTkFont(size=11)
)
```

#### Frames e Containers
```python
# Card/Container Principal
main_card = ctk.CTkFrame(
    parent,
    fg_color="#ffffff",             # Fundo branco
    corner_radius=10,
    border_width=1,
    border_color="#dee2e6"          # Borda sutil
)

# Container de Aviso
warning_container = ctk.CTkFrame(
    parent,
    fg_color="#fff3cd",             # Amarelo claro
    corner_radius=8,
    border_width=1,
    border_color="#ffeaa7"
)

# Container Transparente (grouping)
transparent_group = ctk.CTkFrame(
    parent,
    fg_color="transparent"
)
```

### Sistema de Toast Notifications

```python
class ToastNotification:
    """
    Sistema de notificações não-intrusivas
    Padrão: canto superior direito, 3 segundos, auto-close
    """
    
    TYPES = {
        "success": {
            "bg_color": "#28a745",
            "text_color": "#ffffff",
            "icon": "✅",
            "duration": 3000
        },
        "error": {
            "bg_color": "#dc3545", 
            "text_color": "#ffffff",
            "icon": "❌",
            "duration": 5000        # Erros ficam mais tempo
        },
        "warning": {
            "bg_color": "#ffc107",
            "text_color": "#212529", # Preto para melhor contraste
            "icon": "⚠️",
            "duration": 4000
        },
        "info": {
            "bg_color": "#17a2b8",
            "text_color": "#ffffff",
            "icon": "ℹ️",
            "duration": 3000
        }
    }
    
    def __init__(self, parent, message, tipo="info", duration=None):
        """
        Cria toast notification
        
        Args:
            parent: Widget pai (janela principal)
            message: Texto da mensagem
            tipo: "success", "error", "warning", "info"
            duration: Duração em ms (opcional)
        """
        self.config = self.TYPES.get(tipo, self.TYPES["info"])
        self.duration = duration or self.config["duration"]
        self._create_toast(parent, message)
    
    def _create_toast(self, parent, message):
        """Cria a janela do toast"""
        # Implementação do toast...
```

## 🔧 Padrões de Código Backend

### Estrutura de Classes

```python
class ProcessadorDados:
    """
    Classe para processamento de dados com padrões estabelecidos
    
    Attributes:
        config: Configuração carregada
        logger: Sistema de logging
        
    Example:
        processor = ProcessadorDados()
        result = processor.processar_arquivo("caminho/arquivo.csv")
    """
    
    def __init__(self, config_path: str = "config_dias_filmagem.json"):
        """
        Inicializa processador
        
        Args:
            config_path: Caminho para arquivo de configuração
            
        Raises:
            FileNotFoundError: Se config não for encontrado
            ValueError: Se config for inválido
        """
        self.config = self._carregar_config(config_path)
        self.logger = self._setup_logging()
        self._validar_dependencias()
    
    def processar_arquivo(self, caminho: str) -> bool:
        """
        Processa arquivo de entrada
        
        Args:
            caminho: Caminho para o arquivo
            
        Returns:
            True se processamento foi bem-sucedido, False caso contrário
            
        Raises:
            FileNotFoundError: Se arquivo não existe
            PermissionError: Se não há permissão de leitura
        """
        try:
            self._validar_arquivo(caminho)
            dados = self._extrair_dados(caminho)
            resultado = self._processar_dados(dados)
            self._salvar_resultado(resultado)
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao processar {caminho}: {str(e)}")
            return False
    
    def _validar_arquivo(self, caminho: str) -> None:
        """Valida arquivo de entrada (método privado)"""
        if not os.path.exists(caminho):
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
            
        if not os.access(caminho, os.R_OK):
            raise PermissionError(f"Sem permissão de leitura: {caminho}")
```

### Tratamento de Erros

```python
# ✅ Padrão recomendado - Específico e informativo
def processar_csv(caminho_csv: str) -> pd.DataFrame:
    """Processa arquivo CSV com tratamento robusto de erros"""
    try:
        # Verificações preliminares
        if not os.path.exists(caminho_csv):
            raise FileNotFoundError(f"CSV não encontrado: {caminho_csv}")
            
        if os.path.getsize(caminho_csv) == 0:
            raise ValueError("Arquivo CSV está vazio")
            
        # Processamento principal
        df = pd.read_csv(caminho_csv, encoding="utf-8")
        
        # Validações de dados
        colunas_obrigatorias = ["Cena", "Locação", "Personagens"]
        colunas_faltando = [col for col in colunas_obrigatorias if col not in df.columns]
        
        if colunas_faltando:
            raise ValueError(f"Colunas obrigatórias ausentes: {colunas_faltando}")
            
        return df
        
    except pd.errors.EmptyDataError:
        raise ValueError("CSV está vazio ou malformado")
    except pd.errors.ParserError as e:
        raise ValueError(f"Erro ao analisar CSV: {str(e)}")
    except UnicodeDecodeError:
        # Tentar encoding alternativo
        try:
            df = pd.read_csv(caminho_csv, encoding="latin-1")
            logging.warning("CSV lido com encoding latin-1")
            return df
        except Exception:
            raise ValueError("Erro de encoding - salve CSV como UTF-8")
    except Exception as e:
        raise RuntimeError(f"Erro inesperado ao processar CSV: {str(e)}")

# ❌ Evitar - Muito genérico
def processar_csv_ruim(caminho):
    try:
        return pd.read_csv(caminho)
    except Exception as e:
        print(f"Erro: {e}")
        return None
```

### Logging Consistente

```python
import logging
import sys

def configurar_logging(nivel: str = "INFO") -> logging.Logger:
    """Configura sistema de logging padronizado"""
    
    # Formato com emojis para melhor UX
    formato = "%(asctime)s | %(levelname)s | %(message)s"
    
    logging.basicConfig(
        level=getattr(logging, nivel.upper()),
        format=formato,
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            # logging.FileHandler("app.log")  # Opcional para debug
        ]
    )
    
    return logging.getLogger(__name__)

# Uso nos métodos
class MinhaClasse:
    def __init__(self):
        self.logger = configurar_logging()
    
    def operacao_importante(self):
        self.logger.info("🚀 Iniciando operação importante...")
        
        try:
            # Código da operação
            self.logger.info("✅ Operação concluída com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na operação: {str(e)}")
            return False
            
        finally:
            self.logger.info("🔄 Limpeza finalizada")

# Para GUI, usar método log customizado
def log_gui(self, mensagem: str, nivel: str = "info"):
    """Log customizado para GUI com emojis"""
    
    # Mapear emojis por nível
    emojis = {
        "info": "ℹ️",
        "success": "✅", 
        "warning": "⚠️",
        "error": "❌",
        "debug": "🔧"
    }
    
    emoji = emojis.get(nivel, "ℹ️")
    mensagem_formatada = f"{emoji} {mensagem}"
    
    # Adicionar ao widget de log
    self.log_text.insert("end", f"{mensagem_formatada}\n")
    self.log_text.see("end")
    self.root.update_idletasks()
    
    # Também logar no sistema
    getattr(self.logger, nivel, self.logger.info)(mensagem)
```

### Validação de Dados

```python
from typing import Optional, List, Dict, Any
from pathlib import Path

def validar_configuracao(config: Dict[str, Any]) -> bool:
    """
    Valida estrutura da configuração
    
    Args:
        config: Dicionário de configuração
        
    Returns:
        True se válido, False caso contrário
        
    Raises:
        ValueError: Se configuração é inválida
    """
    campos_obrigatorios = [
        "dias_filmagem",
        "formato_data", 
        "encoding_csv"
    ]
    
    # Verificar campos obrigatórios
    for campo in campos_obrigatorios:
        if campo not in config:
            raise ValueError(f"Campo obrigatório ausente: {campo}")
    
    # Validar tipos específicos
    if not isinstance(config["dias_filmagem"], list):
        raise ValueError("dias_filmagem deve ser uma lista")
        
    if not all(isinstance(dia, int) for dia in config["dias_filmagem"]):
        raise ValueError("dias_filmagem deve conter apenas números inteiros")
        
    if not isinstance(config["formato_data"], str):
        raise ValueError("formato_data deve ser string")
        
    return True

def validar_arquivo_pdf(caminho: str) -> bool:
    """Valida arquivo PDF"""
    path = Path(caminho)
    
    # Verificações básicas
    if not path.exists():
        raise FileNotFoundError(f"PDF não encontrado: {caminho}")
        
    if path.suffix.lower() != '.pdf':
        raise ValueError("Arquivo deve ter extensão .pdf")
        
    if path.stat().st_size == 0:
        raise ValueError("Arquivo PDF está vazio")
        
    # Verificar se não é muito grande (50MB)
    max_size = 50 * 1024 * 1024
    if path.stat().st_size > max_size:
        raise ValueError(f"PDF muito grande (máximo {max_size//1024//1024}MB)")
        
    return True

def sanitizar_string(texto: str) -> str:
    """Remove caracteres problemáticos de strings"""
    import re
    
    if not isinstance(texto, str):
        return str(texto)
        
    # Remover caracteres de controle
    texto = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', texto)
    
    # Remover HTML/XML tags
    texto = re.sub(r'<[^>]+>', '', texto)
    
    # Normalizar espaços
    texto = re.sub(r'\s+', ' ', texto).strip()
    
    return texto
```

## 🧪 Padrões de Teste

### Estrutura de Testes

```python
# tests/test_gerador_od.py
import pytest
import pandas as pd
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import tempfile
import os

from gerador_od_completo import GeradorODCompleto

class TestGeradorODCompleto:
    """Testes para classe principal do gerador"""
    
    def setup_method(self):
        """Setup executado antes de cada teste"""
        self.gerador = GeradorODCompleto()
        self.temp_dir = tempfile.mkdtemp()
        
    def teardown_method(self):
        """Cleanup executado após cada teste"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_carregar_dados_sucesso(self):
        """Teste de carregamento bem-sucedido"""
        # Arrange
        with patch.object(self.gerador, '_processar_pdf') as mock_pdf:
            with patch.object(self.gerador, '_processar_csv') as mock_csv:
                mock_pdf.return_value = {"dia_1": {"data": "24/08/2025"}}
                mock_csv.return_value = pd.DataFrame({"Cena": [1], "Locação": ["Studio"]})
                
                # Act
                resultado = self.gerador._carregar_dados()
                
                # Assert
                assert resultado is True
                mock_pdf.assert_called_once()
                mock_csv.assert_called_once()
    
    def test_carregar_dados_arquivo_inexistente(self):
        """Teste com arquivo inexistente"""
        # Arrange
        with patch('os.path.exists') as mock_exists:
            mock_exists.return_value = False
            
            # Act & Assert
            resultado = self.gerador._carregar_dados()
            assert resultado is False
    
    @pytest.mark.parametrize("dia,esperado", [
        (1, True),
        (5, True), 
        (10, False),  # Dia não existe
        (-1, False),  # Dia inválido
    ])
    def test_gerar_od_dia(self, dia, esperado):
        """Teste parametrizado para geração de dias"""
        # Arrange
        self.gerador.dados_pdf = {"dia_1": {}, "dia_5": {}}
        self.gerador.dados_csv = pd.DataFrame({"Cena": [1]})
        
        # Act
        resultado = self.gerador.gerar_od_dia(dia)
        
        # Assert
        assert resultado == esperado
    
    def test_gerar_todas_ods(self):
        """Teste de geração em lote"""
        # Arrange
        self.gerador.dados_pdf = {
            "dia_1": {"data": "24/08/2025"},
            "dia_2": {"data": "25/08/2025"}
        }
        self.gerador.dados_csv = pd.DataFrame({"Cena": [1, 2]})
        
        with patch.object(self.gerador, 'gerar_od_dia') as mock_gerar:
            mock_gerar.side_effect = [True, False]  # Primeiro sucesso, segundo falha
            
            # Act
            resultado = self.gerador.gerar_todas_ods()
            
            # Assert
            assert resultado["total"] == 2
            assert resultado["sucessos"] == 1
            assert resultado["falhas"] == 1
```

### Mocking e Fixtures

```python
# tests/conftest.py
import pytest
import pandas as pd
from pathlib import Path
import tempfile

@pytest.fixture
def csv_valido():
    """Fixture com CSV válido para testes"""
    return pd.DataFrame({
        "Cena": [1, 2, 3],
        "Locação": ["Estúdio A", "Estúdio B", "Externa"],
        "Personagens": ["João", "Maria", "Pedro"],
        "Observações": ["Close", "Plano geral", "Drone"]
    })

@pytest.fixture
def config_teste():
    """Fixture com configuração de teste"""
    return {
        "dias_filmagem": [1, 2, 3],
        "formato_data": "dd/mm/aaaa",
        "encoding_csv": "utf-8"
    }

@pytest.fixture
def arquivos_temporarios():
    """Fixture que cria arquivos temporários para teste"""
    temp_dir = tempfile.mkdtemp()
    
    # Criar estrutura de diretórios
    arquivos_dir = Path(temp_dir) / "arquivos"
    arquivos_dir.mkdir()
    
    ods_dir = arquivos_dir / "ODs"
    ods_dir.mkdir()
    
    yield temp_dir
    
    # Cleanup
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)

# Uso nas classes de teste
class TestIntegracao:
    def test_fluxo_completo(self, csv_valido, config_teste, arquivos_temporarios):
        """Teste de integração completo"""
        # Setup dos arquivos temporários
        csv_path = Path(arquivos_temporarios) / "arquivos" / "DECUPAGEM.csv"
        csv_valido.to_csv(csv_path, index=False, encoding="utf-8")
        
        # Criar PDF mock
        pdf_path = Path(arquivos_temporarios) / "arquivos" / "PLANO_FINAL.pdf"
        pdf_path.write_bytes(b"Mock PDF content")
        
        # Executar teste...
```

### Testes de GUI

```python
# tests/test_gui.py
import pytest
import customtkinter as ctk
from unittest.mock import Mock, patch
import threading
import time

from gerar_od_gui import GeradorODGUI, ToastNotification

class TestGeradorODGUI:
    """Testes para interface gráfica"""
    
    def setup_method(self):
        """Setup para testes de GUI"""
        # Configurar modo de teste do CustomTkinter
        ctk.set_appearance_mode("light")
        
    def test_inicializacao_gui(self):
        """Teste de inicialização da interface"""
        # Arrange & Act
        with patch('gerar_od_gui.GeradorODCompleto'):
            gui = GeradorODGUI()
            
            # Assert
            assert gui.root is not None
            assert gui.gerador is not None
            assert gui.dias_disponiveis == []
    
    def test_verificar_arquivos_com_toast_sucesso(self):
        """Teste de verificação com toast de sucesso"""
        # Arrange
        with patch('gerar_od_gui.GeradorODCompleto'):
            with patch('os.path.exists') as mock_exists:
                mock_exists.return_value = True
                
                gui = GeradorODGUI()
                
                # Act
                with patch.object(gui, 'carregar_dias_disponiveis'):
                    with patch('gerar_od_gui.ToastNotification') as mock_toast:
                        gui.verificar_arquivos_com_toast()
                        
                        # Assert
                        mock_toast.assert_called_once()
                        args = mock_toast.call_args[0]
                        assert "Todos os arquivos foram encontrados" in args[1]
                        assert args[2] == "success"
    
    def test_toast_notification(self):
        """Teste do sistema de toast"""
        # Arrange
        root = ctk.CTk()
        root.geometry("400x300")
        
        # Act
        toast = ToastNotification(root, "Teste de mensagem", "success", 1000)
        
        # Simular espera
        root.after(1500, root.quit)  # Fechar após toast expirar
        root.mainloop()
        
        # Assert - Toast deve ter sido criado e fechado automaticamente
        # (teste visual - verificação manual necessária)
    
    @pytest.mark.parametrize("tipo,cor_esperada", [
        ("success", "#28a745"),
        ("error", "#dc3545"),
        ("warning", "#ffc107"),
        ("info", "#17a2b8")
    ])
    def test_cores_toast(self, tipo, cor_esperada):
        """Teste parametrizado das cores do toast"""
        root = ctk.CTk()
        toast = ToastNotification(root, "Teste", tipo)
        
        # Verificar se cor está correta (implementação depende da estrutura)
        # Este teste seria mais detalhado com acesso aos componentes internos
        assert toast is not None
```

## 📦 Padrões de Build e Deploy

### Build Script

```python
# build_exe.py - Padrões estabelecidos
import os
import shutil
import subprocess
import sys
from pathlib import Path

def limpar_build_anterior():
    """Remove builds anteriores"""
    diretorios_limpar = [
        "build", "dist", "__pycache__", 
        "build_temp", "distribuicao"
    ]
    
    for diretorio in diretorios_limpar:
        if Path(diretorio).exists():
            shutil.rmtree(diretorio)
            print(f"✅ Removido: {diretorio}")

def configurar_pyinstaller():
    """Configuração padronizada do PyInstaller"""
    return [
        "pyinstaller",
        "--onefile",                    # Arquivo único
        "--windowed",                   # Sem console 
        "--name=GeradorOD",            # Nome específico
        "--distpath=distribuicao",      # Pasta de saída
        "--workpath=build_temp",        # Pasta temporária
        "--clean",                      # Limpar cache
        "--hidden-import=customtkinter", # GUI framework
        "--hidden-import=PIL",          # Imagens
        "--hidden-import=PIL._tkinter_finder",
        "--hidden-import=openpyxl.styles", # Excel formatting
        "--add-data=config_dias_filmagem.json;.", # Config
        "gerar_od.py"                   # Entry point
    ]

def validar_build(executavel_path: Path) -> bool:
    """Valida se build foi bem-sucedido"""
    if not executavel_path.exists():
        print("❌ Executável não foi criado")
        return False
        
    size_mb = executavel_path.stat().st_size / (1024 * 1024)
    print(f"📊 Tamanho do executável: {size_mb:.1f}MB")
    
    if size_mb > 100:  # Limite razoável
        print("⚠️ Executável muito grande")
        
    return True

def main():
    """Processo principal de build"""
    print("🚀 Iniciando build do executável...")
    
    try:
        # 1. Limpeza
        limpar_build_anterior()
        
        # 2. Build
        cmd = configurar_pyinstaller()
        resultado = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        # 3. Validação
        exe_path = Path("distribuicao/GeradorOD.exe")
        if validar_build(exe_path):
            print("✅ Build concluído com sucesso!")
            return True
        else:
            print("❌ Build falhou na validação")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro no PyInstaller: {e}")
        print(f"Saída: {e.stdout}")
        print(f"Erro: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    sucesso = main()
    sys.exit(0 if sucesso else 1)
```

## 🔄 Conventional Commits

### Padrão de Mensagens

```bash
# Formato: <tipo>(<escopo>): <descrição>
# <tipo>: feat, fix, docs, style, refactor, test, chore
# <escopo>: gui, core, build, tests (opcional)
# <descrição>: Imperativo, minúsculo, sem ponto final

# ✅ Exemplos corretos
feat(gui): adiciona sistema de toast notifications
fix(core): corrige erro de encoding em CSV UTF-8
docs: atualiza README com instruções de instalação
test(gui): adiciona testes para verificação de arquivos
refactor(core): melhora estrutura de validação de dados
style(gui): ajusta cores para melhor acessibilidade
chore(build): atualiza dependências do PyInstaller

# ❌ Evitar
Add toast notifications
Fixed bug
Update docs
```

### Breaking Changes

```bash
# Para mudanças que quebram compatibilidade
feat(core)!: altera estrutura do config JSON

BREAKING CHANGE: 
- config_dias_filmagem.json agora requer campo "versao"
- Remover configurações antigas antes de atualizar
- Ver migration guide em docs/migration.md
```

---

## 📚 Recursos Adicionais

### Ferramentas Recomendadas

```bash
# Formatação e Linting
pip install black flake8 mypy

# Uso
black .                    # Formatar código
flake8 .                   # Verificar style guide
mypy gerador_od_completo.py # Type checking
```

### VSCode Settings

```json
// .vscode/settings.json
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=88"],
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "editor.formatOnSave": true
}
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3.11
        
  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
        
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: python
        pass_filenames: false
        always_run: true
```
