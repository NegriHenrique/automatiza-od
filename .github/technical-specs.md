# Especificações Técnicas - Ordem do Dia

## 🏗️ Arquitetura do Sistema

### Visão Geral
```
┌─────────────────────────────────────────────────────────────┐
│                    ORDEM DO DIA v2.0                       │
├─────────────────────────────────────────────────────────────┤
│  Entry Point: gerar_od.py                                  │
│  ├── GUI Mode: gerar_od_gui.py (CustomTkinter)            │
│  └── CLI Mode: Direct call to gerador_od_completo.py      │
│                                                             │
│  Core Engine: gerador_od_completo.py                       │
│  ├── PDF Processing (pdfplumber)                           │
│  ├── CSV Processing (pandas)                               │
│  ├── Excel Generation (openpyxl)                           │
│  └── Data Validation & Business Logic                      │
│                                                             │
│  Build System: build_exe.py                                │
│  ├── PyInstaller Configuration                             │
│  ├── Asset Bundling                                        │
│  └── Distribution Package Creation                         │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Componentes Técnicos

### 1. Core Engine (`gerador_od_completo.py`)

**Responsabilidades:**
- Processamento de arquivos PDF e CSV
- Lógica de negócio para geração de ODs
- Validação de dados e integridade
- Formatação e estilização de planilhas Excel

**APIs Principais:**
```python
class GeradorODCompleto:
    def _carregar_dados(self) -> bool
    def gerar_od_dia(self, dia: int) -> bool
    def gerar_todas_ods(self) -> dict
    def _processar_pdf(self, caminho_pdf: str) -> dict
    def _processar_csv(self, caminho_csv: str) -> pd.DataFrame
    def _gerar_excel(self, dados: dict, dia: int) -> str
```

**Dependências:**
- `pandas>=1.5.0`: Manipulação de dados
- `openpyxl>=3.0.0`: Geração de Excel
- `pdfplumber>=0.7.0`: Extração de PDF
- `pathlib`: Manipulação de caminhos

### 2. Interface Gráfica (`gerar_od_gui.py`)

**Responsabilidades:**
- Interface de usuário moderna e acessível
- Sistema de notificações toast
- Threading para operações assíncronas
- Validação visual de arquivos

**Componentes UI:**
```python
class GeradorODGUI:
    # Layout Components
    def criar_cabecalho(self) -> None
    def criar_area_principal(self) -> None
    def criar_status_arquivos(self) -> None
    def criar_selecao_dias(self) -> None
    def criar_botoes_acao(self) -> None
    def criar_area_progresso(self) -> None
    def criar_rodape(self) -> None
    
    # Business Logic
    def verificar_arquivos_com_toast(self) -> None
    def gerar_ods(self) -> None
    def executar_geracao(self, dias: list) -> None
    
    # Utilities
    def log(self, mensagem: str) -> None
    def run(self) -> None

class ToastNotification:
    def __init__(self, parent, message, tipo, duration)
    def close(self) -> None
```

**Dependências:**
- `customtkinter>=5.0.0`: Framework GUI moderno
- `tkinter`: Base GUI (built-in Python)
- `threading`: Operações assíncronas
- `pathlib`: Manipulação de arquivos

### 3. Entry Point (`gerar_od.py`)

**Responsabilidades:**
- Detecção automática de modo (GUI vs CLI)
- Parsing de argumentos de linha de comando
- Fallback inteligente entre modos

**Fluxo de Execução:**
```python
def main():
    # 1. Parse command line arguments
    # 2. Try to import GUI
    # 3. If GUI available and no CLI args: Launch GUI
    # 4. Else: Execute CLI mode
    # 5. Handle errors gracefully
```

### 4. Build System (`build_exe.py`)

**Responsabilidades:**
- Configuração do PyInstaller
- Bundling de assets e dependências
- Criação de estrutura de distribuição
- Validação do build

**Processo de Build:**
```python
def main():
    # 1. Cleanup previous builds
    # 2. Run PyInstaller with optimized config
    # 3. Create distribution structure
    # 4. Copy assets and configs
    # 5. Validate executable
    # 6. Create documentation
```

## 💾 Estrutura de Dados

### Configuração (`config_dias_filmagem.json`)
```json
{
  "dias_filmagem": [1, 2, 3, 4, 5],
  "formato_data": "dd/mm/aaaa",
  "encoding_csv": "utf-8",
  "colunas_obrigatorias": [
    "Cena",
    "Locação", 
    "Personagens",
    "Observações"
  ],
  "formatacao_excel": {
    "fonte": "Calibri",
    "tamanho_fonte": 11,
    "auto_ajuste_largura": true,
    "congelar_paineis": true
  }
}
```

### Estrutura de Dados Processados
```python
# Dados extraídos do PDF
pdf_data = {
    "dia_1": {
        "data": "24/08/2025",
        "locacoes": ["Estúdio A", "Externa - Parque"],
        "horarios": {
            "inicio": "08:00",
            "fim": "18:00",
            "almoco": "12:00-13:00"
        },
        "observacoes": ["Chuva prevista", "Equipamento extra"]
    }
}

# DataFrame do CSV
csv_data = pd.DataFrame({
    "Cena": [1, 2, 3],
    "Locação": ["Estúdio A", "Estúdio A", "Externa"],
    "Personagens": ["João, Maria", "Pedro", "João"],
    "Observações": ["Close-up", "Plano geral", "Drone"]
})
```

## 🎨 Design System

### Paleta de Cores (Hex)
```python
COLORS = {
    # Primary Colors
    "primary": "#007bff",        # Blue
    "primary_hover": "#0056b3",  # Dark Blue
    
    # Semantic Colors  
    "success": "#28a745",        # Green
    "success_hover": "#218838",  # Dark Green
    "error": "#dc3545",          # Red
    "error_hover": "#c82333",    # Dark Red
    "warning": "#ffc107",        # Yellow
    "warning_text": "#856404",   # Dark Yellow
    "info": "#17a2b8",           # Teal
    
    # Neutral Colors
    "background": "#f8f9fa",     # Light Gray
    "surface": "#ffffff",        # White
    "text_primary": "#212529",   # Near Black
    "text_secondary": "#6c757d", # Medium Gray
    "border": "#dee2e6",         # Light Border
    
    # Toast Colors
    "toast_success_bg": "#28a745",
    "toast_success_text": "#ffffff",
    "toast_error_bg": "#dc3545", 
    "toast_error_text": "#ffffff",
    "toast_warning_bg": "#ffc107",
    "toast_warning_text": "#212529",
    "toast_info_bg": "#17a2b8",
    "toast_info_text": "#ffffff"
}
```

### Contraste WCAG 2.1
```python
CONTRAST_RATIOS = {
    "text_primary_on_background": 16.0,    # AAA
    "text_secondary_on_background": 7.0,   # AAA  
    "primary_button_text": 10.5,          # AAA
    "error_text": 5.5,                    # AA
    "success_text": 4.5,                  # AA
    "warning_text": 8.0,                  # AAA
}
```

### Tipografia
```python
TYPOGRAPHY = {
    "font_family": "Segoe UI",
    "sizes": {
        "title": 32,      # Título principal
        "subtitle": 14,   # Subtítulo
        "heading": 16,    # Seções
        "body": 12,       # Texto padrão
        "button": 12,     # Botões
        "caption": 10     # Rodapé
    },
    "weights": {
        "normal": "normal",
        "bold": "bold"
    }
}
```

## 🔧 Configurações Técnicas

### PyInstaller Configuration
```python
PYINSTALLER_CONFIG = {
    "mode": "onefile",           # Arquivo único
    "windowed": True,            # Sem console
    "name": "GeradorOD",         # Nome do executável
    "hidden_imports": [
        "customtkinter",         # GUI framework
        "PIL",                   # Image processing
        "openpyxl.styles",       # Excel formatting
        "pdfplumber.utils"       # PDF utilities
    ],
    "datas": [
        ("config_dias_filmagem.json", "."),
        ("arquivos/", "arquivos/")
    ],
    "optimize": 2,               # Bytecode optimization
    "strip": True,               # Strip symbols
    "upx": False                 # Disable UPX compression
}
```

### Threading Configuration
```python
THREADING_CONFIG = {
    "gui_operations": {
        "daemon": True,          # Daemon threads
        "timeout": 30,           # 30 second timeout
        "queue_size": 10         # Max queued operations
    },
    "file_operations": {
        "chunk_size": 8192,      # File read chunk size
        "max_workers": 2,        # Concurrent file operations
        "timeout": 60            # File operation timeout
    }
}
```

### Logging Configuration
```python
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "handlers": {
        "console": True,         # Console output
        "file": False,           # File logging disabled in GUI
        "gui": True              # GUI log widget
    },
    "max_lines": 1000,          # Max lines in GUI log
    "auto_scroll": True         # Auto scroll to bottom
}
```

## 📊 Performance Specifications

### Memory Usage
- **Startup**: ~50MB
- **Peak (processing)**: ~200MB
- **Executable size**: ~45-50MB
- **Memory leaks**: Zero tolerance

### Execution Times
- **Startup time**: <3 seconds
- **File validation**: <1 second
- **Single day processing**: <10 seconds
- **All days processing**: <30 seconds (5 days)
- **Build time**: ~60 seconds

### File Size Limits
- **PDF files**: Up to 50MB
- **CSV files**: Up to 10MB / 10,000 rows
- **Output Excel**: ~1-5MB per file

## 🔒 Security Considerations

### Input Validation
```python
VALIDATION_RULES = {
    "pdf_files": {
        "max_size": 50 * 1024 * 1024,    # 50MB
        "allowed_extensions": [".pdf"],
        "scan_for_malware": False         # Basic validation only
    },
    "csv_files": {
        "max_size": 10 * 1024 * 1024,    # 10MB  
        "encoding": "utf-8",
        "required_columns": ["Cena", "Locação", "Personagens"]
    },
    "user_input": {
        "sanitize_strings": True,
        "max_length": 1000,
        "forbidden_chars": ["<", ">", "&", "\"", "'"]
    }
}
```

### File System Access
```python
ACCESS_PERMISSIONS = {
    "read_access": [
        "./arquivos/",           # Input files
        "./config_dias_filmagem.json"
    ],
    "write_access": [
        "./arquivos/ODs/",       # Output directory
        "./logs/" if os.getenv("OD_DEBUG") else None
    ],
    "no_access": [
        "C:/Windows/",           # System directories
        "C:/Program Files/",     # Program files
        "~/.ssh/",               # SSH keys
        "/etc/" if os.name != "nt" else None
    ]
}
```

## 🧪 Testing Strategy

### Unit Tests Coverage
```python
TEST_COVERAGE_TARGETS = {
    "gerador_od_completo.py": 95,    # Core logic
    "gerar_od_gui.py": 85,           # GUI components
    "gerar_od.py": 90,               # Entry point
    "build_exe.py": 70,              # Build script
    "overall": 85                    # Overall target
}
```

### Test Categories
```python
TEST_TYPES = {
    "unit": {
        "description": "Individual component testing",
        "framework": "pytest",
        "mocking": "unittest.mock",
        "coverage": "pytest-cov"
    },
    "integration": {
        "description": "Component interaction testing", 
        "files": ["test_integration.py"],
        "external_deps": ["PDF files", "CSV files"]
    },
    "gui": {
        "description": "GUI interaction testing",
        "framework": "pytest + tkinter testing",
        "automated": False,           # Manual testing required
        "accessibility": True         # WCAG compliance testing
    },
    "performance": {
        "description": "Performance benchmarking",
        "tools": ["time", "memory_profiler"],
        "benchmarks": ["startup_time", "processing_time", "memory_usage"]
    }
}
```

## 🚀 Deployment Pipeline

### CI/CD Stages
```yaml
pipeline_stages:
  1_code_quality:
    - linting: [black, flake8, mypy]
    - security: [bandit, safety] 
    - complexity: [mccabe]
  
  2_testing:
    - unit_tests: pytest
    - integration_tests: pytest integration/
    - coverage: pytest-cov (min 85%)
  
  3_build:
    - executable: python build_exe.py
    - validation: Test executable startup
    - packaging: Create distribution ZIP
  
  4_release:
    - versioning: Semantic versioning
    - artifacts: Upload executables
    - documentation: Update README
    - notifications: Teams/Slack alerts
```

### Environment Specifications
```python
ENVIRONMENTS = {
    "development": {
        "python_version": "3.11+",
        "os_support": ["Windows 10+", "Windows 11"],
        "dependencies": "requirements.txt",
        "debugging": True
    },
    "testing": {
        "python_version": "3.11+", 
        "os_support": ["Windows 10", "Windows 11"],
        "test_data": "tests/fixtures/",
        "coverage_required": 85
    },
    "production": {
        "executable": "GeradorOD.exe",
        "os_support": ["Windows 10 (64-bit)", "Windows 11 (64-bit)"],
        "dependencies": "None (standalone)",
        "min_ram": "4GB",
        "min_storage": "100MB"
    }
}
```
