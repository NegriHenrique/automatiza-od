# 📋 Ordem do Dia - Sistema de Geração Automática

[![Build Status](https://github.com/seu-usuario/automatiza-od/workflows/CI/CD/badge.svg)](https://github.com/seu-usuario/automatiza-od/actions)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)](htmlcov/index.html)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🎯 Visão Geral

O **Ordem do Dia** é um sistema moderno e profissional para geração automática de Ordens de Dia (ODs) para produções audiovisuais. Com interface gráfica intuitiva e design acessível, automatiza completamente o processo de criação de planilhas organizacionais a partir de PDFs de planos de filmagem.

## ✨ Principais Funcionalidades

### 🎨 Interface Gráfica Moderna
- **Design acessível** seguindo padrões WCAG 2.1
- **Contraste otimizado** para melhor legibilidade
- **Toast notifications** para feedback imediato
- **Barra de progresso** em tempo real
- **Log detalhado** de todas as operações

### 🔄 Processamento Automático
- **Leitura de PDFs** com extração inteligente de dados
- **Processamento de CSV** com dados de decupagem
- **Geração de Excel** formatado profissionalmente
- **Múltiplos dias** de filmagem em lote
- **Validação automática** de arquivos necessários

### 📦 Distribuição Standalone
- **Executável Windows** (.exe) autocontido
- **Sem dependências** externas necessárias
- **Instalação zero** - apenas execute
- **Compatibilidade** Windows 10/11 (64-bit)

## 🚀 Como Usar

### Interface Gráfica (Recomendado)

1. **Execute**: `GeradorOD.exe`
2. **Verificação**: Sistema verifica automaticamente os arquivos necessários
3. **Seleção**: Escolha quais dias processar
4. **Geração**: Clique em "Gerar ODs" e acompanhe o progresso
5. **Resultado**: ODs salvas em `arquivos/ODs/`

### Linha de Comando (Avançado)

```bash
# Gerar todas as ODs
GeradorOD.exe all

# Gerar OD específica
GeradorOD.exe 1

# Ver ajuda
GeradorOD.exe --help
```

## 📁 Estrutura de Arquivos

```
ordem-do-dia/
├── 📋 GeradorOD.exe              # Executável principal
├── ⚙️ config_dias_filmagem.json  # Configuração
├── 📁 arquivos/
│   ├── 📊 DECUPAGEM.csv          # Dados das cenas
│   ├── 📄 PLANO_FINAL.pdf        # Cronograma
│   └── 📁 ODs/                   # Saída das planilhas
│       ├── OD_Dia_1.xlsx
│       ├── OD_Dia_2.xlsx
│       └── ...
└── 📖 README.txt                 # Instruções básicas
```

## 🛠️ Desenvolvimento

### Pré-requisitos

- Python 3.11+
- pip e venv
- Git

### Configuração do Ambiente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/automatiza-od.git
cd automatiza-od

# Crie ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instale dependências
pip install -r requirements.txt
```

### Executar em Desenvolvimento

```bash
# Interface gráfica
python gerar_od.py

# Linha de comando
python gerar_od.py all
python gerar_od.py 1
```

### Testes

```bash
# Executar todos os testes
python -m pytest

# Com coverage
python -m pytest --cov=. --cov-report=html

# Testes específicos
python -m pytest tests/test_integration.py
```

### Build do Executável

```bash
# Gerar executável distribuível
python build_exe.py
```

O executável será criado em `distribuicao_completa/GeradorOD.exe`

## 🎨 Design e Acessibilidade

### Princípios de Design
- **Contraste WCAG AA/AAA**: Mínimo 4.5:1 para textos normais
- **Tipografia clara**: Segoe UI com tamanhos consistentes
- **Cores semânticas**: Verde (sucesso), vermelho (erro), azul (ação)
- **Feedback visual**: Estados hover, disabled e loading

### Paleta de Cores
- **Primário**: #007bff (azul)
- **Sucesso**: #28a745 (verde)
- **Erro**: #dc3545 (vermelho)
- **Aviso**: #ffc107 (amarelo)
- **Neutro**: #f8f9fa (cinza claro)
- **Texto**: #212529 (preto)

### Sistema de Toast
- **Posição**: Canto superior direito
- **Duração**: 3 segundos (configurável)
- **Tipos**: Sucesso, erro, aviso, informação
- **Auto-fechamento**: Sim

## 🔧 Configuração

### Arquivo `config_dias_filmagem.json`

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
  ]
}
```

### Variáveis de Ambiente

```bash
# Opcional: Customizar comportamento
export OD_DEBUG=true
export OD_LOG_LEVEL=DEBUG
export OD_OUTPUT_DIR=./custom_output
```

## 📊 CI/CD Pipeline

### GitHub Actions

O projeto possui automação completa:

1. **Testes automáticos** em cada push/PR
2. **Build do executável** em releases
3. **Cobertura de código** reportada
4. **Linting** e verificação de qualidade

### Hooks de Git

```bash
# Instalar hooks (opcional)
pre-commit install
```

- **Pre-commit**: Executa testes e linting
- **Pre-push**: Verifica build do executável

## 🚨 Solução de Problemas

### Arquivo não encontrado
- Verifique se `DECUPAGEM.csv` e `PLANO_FINAL.pdf` estão na pasta `arquivos/`
- Use o botão "📂 Abrir Pasta" para navegar até o local correto

### Erro ao processar PDF
- Certifique-se de que o PDF não está protegido por senha
- Verifique se o arquivo não está corrompido
- Tente recriar o PDF a partir do original

### Interface não abre
- Execute como administrador
- Verifique se o antivírus está bloqueando
- Baixe a versão mais recente

### Erro na planilha CSV
- Verifique se o arquivo está em UTF-8
- Confirme se todas as colunas obrigatórias estão presentes
- Use Excel para verificar a integridade dos dados

## 📈 Roadmap

### Versão Atual (2.0)
- ✅ Interface gráfica moderna
- ✅ Acessibilidade WCAG 2.1
- ✅ Toast notifications
- ✅ Executável standalone
- ✅ Testes automatizados

### Próximas Versões (2.1+)
- 🔄 Suporte a múltiplos idiomas
- 🔄 Temas escuro/claro
- 🔄 Templates customizáveis
- 🔄 API REST para integração
- 🔄 Sincronização com Google Sheets

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Padrões de Código

- **Python**: PEP 8 com black formatter
- **Commits**: Conventional Commits
- **Testes**: Cobertura mínima 80%
- **Documentação**: Docstrings obrigatórias

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Autores

- **Desenvolvedor Principal** - [Seu Nome](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- Equipe de produção audiovisual pelo feedback
- Comunidade Python pelas bibliotecas
- Contributors do projeto

---

**Ordem do Dia v2.0** | Sistema profissional para produção audiovisual  
📧 Contato: [seu-email@exemplo.com](mailto:seu-email@exemplo.com)
