# Instruções para GitHub Copilot - Ordem do Dia

## 🎯 Contexto do Projeto

Este é o **Ordem do Dia**, um sistema profissional para geração automática de planilhas organizacionais para produções audiovisuais. O projeto possui interface gráfica moderna, executável standalone e pipeline de CI/CD completo.

## 🏗️ Arquitetura do Sistema

### Componentes Principais

1. **`gerador_od_completo.py`**: Core engine para processamento
   - Extração de dados de PDF usando pdfplumber
   - Processamento de CSV com pandas
   - Geração de Excel com openpyxl
   - Lógica de negócio principal

2. **`gerar_od_gui.py`**: Interface gráfica moderna
   - CustomTkinter para design moderno
   - Sistema de toast notifications
   - Acessibilidade WCAG 2.1
   - Threading para operações assíncronas

3. **`gerar_od.py`**: Entry point com detecção automática
   - Auto-detecção GUI vs CLI
   - Parsing de argumentos de linha de comando
   - Fallback inteligente

4. **`build_exe.py`**: Sistema de build e distribuição
   - PyInstaller para executável standalone
   - Estrutura completa de distribuição
   - Assets e configurações incluídas

### Tecnologias e Dependências

- **Python 3.11+**: Base do sistema
- **CustomTkinter**: Interface gráfica moderna
- **pandas + openpyxl**: Manipulação de Excel
- **pdfplumber**: Extração de dados de PDF
- **PyInstaller**: Geração de executável
- **pytest**: Framework de testes

## 🎨 Padrões de Design

### Interface Gráfica (UX/UI)

```python
# Paleta de cores acessível
CORES = {
    "primario": "#007bff",      # Azul principal
    "sucesso": "#28a745",       # Verde sucesso
    "erro": "#dc3545",          # Vermelho erro
    "aviso": "#ffc107",         # Amarelo aviso
    "texto": "#212529",         # Preto texto
    "fundo": "#f8f9fa",         # Cinza claro fundo
    "neutro": "#6c757d"         # Cinza neutro
}

# Contrastes obrigatórios (WCAG 2.1)
# - Texto normal: mínimo 4.5:1
# - Texto grande: mínimo 3:1
# - Elementos UI: mínimo 3:1
```

### Sistema de Toast

```python
# Implementação de notificações
class ToastNotification:
    def __init__(self, parent, message, tipo="info", duration=3000):
        # Tipos: "success", "error", "warning", "info"
        # Posição: Canto superior direito
        # Auto-fechamento: Sim
```

### Threading para Responsividade

```python
# Sempre usar threading para operações longas
def operacao_longa(self):
    thread = threading.Thread(
        target=self.executar_operacao,
        daemon=True
    )
    thread.start()
```

## 🔧 Padrões de Código

### Estrutura de Classes

```python
class MinhaClasse:
    """Docstring obrigatória explicando a classe"""
    
    def __init__(self):
        """Inicialização clara e documentada"""
        self.configurar_componentes()
        
    def metodo_publico(self, param: str) -> bool:
        """
        Método público com type hints e docstring
        
        Args:
            param: Descrição do parâmetro
            
        Returns:
            bool: Descrição do retorno
        """
        return self._metodo_privado(param)
        
    def _metodo_privado(self, param: str) -> bool:
        """Métodos privados com underscore"""
        pass
```

### Tratamento de Erros

```python
# Sempre usar try/except específicos
try:
    resultado = operacao_perigosa()
except SpecificException as e:
    self.log(f"❌ Erro específico: {str(e)}")
    return False
except Exception as e:
    self.log(f"❌ Erro inesperado: {str(e)}")
    return False
```

### Logging Consistente

```python
# Padrão de logging com emojis
self.log("🚀 Iniciando operação...")
self.log("✅ Operação concluída com sucesso")
self.log("❌ Erro durante operação")
self.log("⚠️ Aviso importante")
self.log("📊 Resultado: 5 sucessos, 1 falha")
```

## 🧪 Padrões de Teste

### Estrutura de Testes

```python
# tests/test_component.py
import pytest
from unittest.mock import Mock, patch
from component import Component

class TestComponent:
    def setup_method(self):
        """Setup antes de cada teste"""
        self.component = Component()
        
    def test_metodo_sucesso(self):
        """Teste de caso de sucesso"""
        resultado = self.component.metodo("input_valido")
        assert resultado is True
        
    def test_metodo_erro(self):
        """Teste de caso de erro"""
        with pytest.raises(ValueError):
            self.component.metodo("input_invalido")
            
    @patch('component.external_dependency')
    def test_com_mock(self, mock_dep):
        """Teste com mocking de dependências"""
        mock_dep.return_value = "mocked_value"
        resultado = self.component.metodo_com_dependencia()
        assert resultado == "expected_result"
```

### Cobertura de Testes

- **Mínimo 80%** de cobertura geral
- **100%** para módulos críticos (core engine)
- **Testes de integração** obrigatórios
- **Mocks** para dependências externas

## 🚀 Pipeline CI/CD

### GitHub Actions

1. **Testes automáticos**: Cada push/PR
2. **Linting**: Black, flake8, mypy
3. **Build executável**: Tags/releases
4. **Cobertura**: Coverage report
5. **Segurança**: Safety, bandit

### Git Hooks

```bash
# Pre-commit: Testes rápidos
pytest tests/test_simple.py

# Pre-push: Testes completos
pytest --cov=. --cov-fail-under=80
```

## 📦 Build e Distribuição

### Executável Standalone

```python
# build_exe.py - Configuração PyInstaller
pyinstaller_args = [
    '--onefile',                    # Arquivo único
    '--windowed',                   # Sem console
    '--name=GeradorOD',            # Nome do executável
    '--icon=icon.ico',             # Ícone (se houver)
    '--hidden-import=customtkinter', # Imports ocultos
    '--hidden-import=PIL',
    'gerar_od.py'                  # Entry point
]
```

### Estrutura de Distribuição

```
distribuicao_completa/
├── GeradorOD.exe              # Executável principal
├── config_dias_filmagem.json  # Configuração
├── README.txt                 # Instruções básicas
├── MANUAL_USUARIO.md          # Manual completo
└── arquivos/                  # Pasta de trabalho
    ├── DECUPAGEM.csv          # Exemplo
    ├── PLANO_FINAL.pdf        # Exemplo
    └── ODs/                   # Saída
```

## 🔍 Debugging e Troubleshooting

### Logs Estruturados

```python
# Sempre logar operações importantes
self.log(f"📅 Processando {len(dias)} dias de filmagem")
self.log(f"📄 PDF: {pdf_path} ({pdf_size} MB)")
self.log(f"📊 CSV: {csv_rows} linhas encontradas")
```

### Estados da Interface

```python
# Sempre atualizar estados visuais
self.btn_gerar.configure(state="disabled")
self.progress_bar.set(progress_value)
self.status_label.configure(text="Processando...", text_color="#007bff")
```

### Validações Robustas

```python
# Sempre validar inputs e arquivos
if not os.path.exists(arquivo_necessario):
    self.mostrar_erro(f"Arquivo não encontrado: {arquivo_necessario}")
    return False
    
if not self.validar_csv(csv_path):
    self.mostrar_erro("CSV inválido: colunas obrigatórias ausentes")
    return False
```

## 🎯 Melhores Práticas

### Performance

- **Threading** para operações I/O longas
- **Lazy loading** de dados grandes
- **Cache** de resultados quando apropriado
- **Progressbar** para feedback visual

### Acessibilidade

- **Contraste mínimo** 4.5:1 (WCAG AA)
- **Textos descritivos** em todos os elementos
- **Estados visuais** claros (hover, disabled, active)
- **Keyboard navigation** onde aplicável

### Manutenibilidade

- **Docstrings** em todas as funções públicas
- **Type hints** consistentes
- **Configuração externa** (JSON)
- **Logs estruturados** com níveis apropriados

### Distribuição

- **Executável autocontido** sem dependências
- **Documentação completa** incluída
- **Exemplos de arquivos** fornecidos
- **Versionamento semântico** (MAJOR.MINOR.PATCH)

## 🔄 Workflow de Desenvolvimento

1. **Feature branch**: `git checkout -b feature/nova-funcionalidade`
2. **Desenvolvimento**: Seguir padrões estabelecidos
3. **Testes**: Garantir cobertura adequada
4. **Commit**: Conventional commits
5. **PR**: Code review obrigatório
6. **Merge**: Após aprovação e testes passando
7. **Release**: Tag semântica trigger CI/CD

## 📚 Recursos Adicionais

- **Documentação técnica**: `.github/technical-specs.md`
- **Checklist desenvolvimento**: `.github/development-checklist.md`
- **Troubleshooting**: `.github/troubleshooting.md`
- **Padrões de código**: `.github/code-patterns.md`
