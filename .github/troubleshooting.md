# 🔧 Solução de Problemas - Ordem do Dia

## 🚨 Problemas Comuns e Soluções

### 1. 📁 Arquivos Não Encontrados

#### Problema
```
❌ DECUPAGEM.csv não encontrado
❌ PLANO_FINAL.pdf não encontrado
```

#### Causas Possíveis
- Arquivos não estão na pasta `arquivos/`
- Nomes dos arquivos estão incorretos
- Arquivos estão em subpastas

#### Soluções
1. **Verificar localização:**
   ```
   pasta_do_programa/
   └── arquivos/
       ├── DECUPAGEM.csv    ← Deve estar aqui
       └── PLANO_FINAL.pdf  ← Deve estar aqui
   ```

2. **Usar botão "📂 Abrir Pasta"** na interface para navegar até o local correto

3. **Verificar nomes exatos:**
   - Deve ser exatamente `DECUPAGEM.csv` (maiúsculas)
   - Deve ser exatamente `PLANO_FINAL.pdf` (maiúsculas)

4. **Verificar extensões:**
   - CSV deve ter extensão `.csv`
   - PDF deve ter extensão `.pdf`

### 2. 🔒 Erro ao Processar PDF

#### Problema
```
❌ Erro ao processar PDF: [Erro específico]
❌ PDF protegido por senha
❌ PDF corrompido
```

#### Soluções
1. **PDF protegido por senha:**
   - Remover senha do PDF usando Adobe Acrobat
   - Ou salvar uma cópia sem proteção

2. **PDF corrompido:**
   - Abrir PDF em leitor para verificar integridade
   - Recriar PDF a partir do arquivo original
   - Tentar com PDF menor para teste

3. **Formato não suportado:**
   - Garantir que é PDF real (não imagem renomeada)
   - Converter para PDF padrão se necessário

### 3. 📊 Erro na Planilha CSV

#### Problema
```
❌ Erro ao processar CSV: encoding
❌ Colunas obrigatórias ausentes
❌ Dados inválidos no CSV
```

#### Soluções
1. **Problema de encoding:**
   ```python
   # Salvar CSV como UTF-8 no Excel:
   # Arquivo > Salvar Como > Mais opções > Codificação: UTF-8
   ```

2. **Colunas obrigatórias:**
   - Verificar se CSV tem as colunas: `Cena`, `Locação`, `Personagens`, `Observações`
   - Nomes devem ser exatos (com acentos)

3. **Dados inválidos:**
   - Verificar se não há células completamente vazias
   - Remover caracteres especiais problemáticos
   - Verificar se números estão no formato correto

### 4. 🖥️ Interface Não Abre

#### Problema
```
Interface gráfica não inicia
Executável não responde
Erro de inicialização
```

#### Soluções
1. **Executar como administrador:**
   - Clique direito no `GeradorOD.exe`
   - Selecione "Executar como administrador"

2. **Verificar antivírus:**
   - Adicionar executável à lista de exceções
   - Temporariamente desabilitar proteção em tempo real

3. **Verificar dependências:**
   - Instalar Visual C++ Redistributable
   - Atualizar Windows para versão mais recente

4. **Teste de linha de comando:**
   ```cmd
   GeradorOD.exe --help
   ```

### 5. 🐌 Performance Lenta

#### Problema
```
Processamento muito demorado
Interface trava durante geração
Uso excessivo de memória
```

#### Soluções
1. **Arquivos muito grandes:**
   - PDF: Máximo recomendado 50MB
   - CSV: Máximo recomendado 10,000 linhas

2. **Fechar outros programas:**
   - Liberar memória RAM
   - Fechar navegadores pesados

3. **Verificar disco:**
   - Garantir espaço livre suficiente (>1GB)
   - Usar SSD se possível

### 6. 📋 Erro na Geração de Excel

#### Problema
```
❌ Erro ao gerar OD do Dia X
❌ Arquivo Excel corrompido
❌ Formatação incorreta
```

#### Soluções
1. **Verificar permissões:**
   - Pasta `arquivos/ODs/` deve ter permissão de escrita
   - Fechar Excel se estiver com arquivo aberto

2. **Dados inconsistentes:**
   - Verificar se dados do PDF e CSV são compatíveis
   - Validar formato de datas

3. **Problema de memória:**
   - Gerar dias individualmente em vez de todos juntos
   - Reiniciar aplicação entre gerações

## 🔍 Debugging Avançado

### Logs Detalhados

#### Habilitando Debug Mode
```cmd
# Definir variável de ambiente (Windows)
set OD_DEBUG=true
GeradorOD.exe

# PowerShell
$env:OD_DEBUG="true"
.\GeradorOD.exe
```

#### Interpretando Logs
```
🚀 Sistema iniciado - verificando arquivos...
🔍 Verificando arquivos necessários...
✅ DECUPAGEM.csv encontrado
✅ PLANO_FINAL.pdf encontrado
📅 Carregando dias disponíveis do plano...
📅 5 dias encontrados: 1, 2, 3, 4, 5
🎬 Iniciando geração de TODAS as ODs...
📅 Processando Dia 1...
✅ OD do Dia 1 gerada com sucesso!
```

### Validação Manual

#### Teste de Arquivos
```python
# Verificar se arquivos existem
import os
print("DECUPAGEM.csv:", os.path.exists("arquivos/DECUPAGEM.csv"))
print("PLANO_FINAL.pdf:", os.path.exists("arquivos/PLANO_FINAL.pdf"))
```

#### Teste de CSV
```python
import pandas as pd
try:
    df = pd.read_csv("arquivos/DECUPAGEM.csv", encoding="utf-8")
    print("Colunas:", df.columns.tolist())
    print("Linhas:", len(df))
except Exception as e:
    print("Erro:", e)
```

#### Teste de PDF
```python
import pdfplumber
try:
    with pdfplumber.open("arquivos/PLANO_FINAL.pdf") as pdf:
        print("Páginas:", len(pdf.pages))
        print("Primeira página:", pdf.pages[0].extract_text()[:100])
except Exception as e:
    print("Erro:", e)
```

## 🆘 Quando Pedir Ajuda

### Informações para Incluir no Report

1. **Versão do sistema:**
   - Windows 10 ou 11
   - Versão específica (ex: Windows 11 22H2)

2. **Arquivos de entrada:**
   - Tamanho do PDF
   - Número de linhas do CSV
   - Se possível, enviar arquivos exemplo

3. **Erro específico:**
   - Mensagem de erro completa
   - Screenshot da interface
   - Logs do sistema

4. **Passos para reproduzir:**
   - O que você estava fazendo
   - Quando o erro ocorreu
   - Se é consistente ou esporádico

### Template de Report de Bug

```markdown
## 🐛 Descrição do Bug
[Descreva o problema de forma clara]

## 🔄 Passos para Reproduzir
1. Abrir aplicação
2. Clicar em "..."
3. Erro ocorre

## ✅ Comportamento Esperado
[O que deveria acontecer]

## ❌ Comportamento Atual  
[O que realmente acontece]

## 💻 Ambiente
- OS: Windows 11 22H2
- Versão: Ordem do Dia v2.0
- Arquivos: PDF 5MB, CSV 100 linhas

## 📋 Logs
```
[Cole os logs aqui]
```

## 📎 Anexos
[Screenshots, arquivos exemplo se possível]
```

## 🔧 Ferramentas de Diagnóstico

### Verificação de Sistema
```cmd
# Verificar versão do Windows
winver

# Verificar espaço em disco
dir /-c

# Verificar memória
systeminfo | find "Available Physical Memory"
```

### Verificação de Dependências
```cmd
# Verificar se Visual C++ está instalado
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products" /s | find "Visual C++"

# Verificar Python (se modo desenvolvimento)
python --version
```

### Reset do Ambiente
```cmd
# Limpar cache (se desenvolvimento)
rmdir /s /q __pycache__
rmdir /s /q .pytest_cache

# Remover ODs existentes
del arquivos\ODs\*.xlsx

# Recriar estrutura
mkdir arquivos\ODs
```

## 📞 Canais de Suporte

### Issues no GitHub
- URL: `https://github.com/seu-usuario/automatiza-od/issues`
- Para bugs e feature requests
- Incluir template de report

### Documentação
- README.md: Instruções gerais
- MANUAL_USUARIO.md: Manual detalhado
- Technical specs: Especificações técnicas

### Email de Suporte
- Para questões específicas da produção
- Incluir arquivos exemplo (se possível)
- Mencionar versão e sistema operacional

---

## 🔄 Atualizações e Manutenção

### Verificar Atualizações
1. Acessar GitHub Releases
2. Comparar versão atual com mais recente
3. Baixar nova versão se disponível
4. Testar com dados de backup primeiro

### Backup de Dados
```cmd
# Backup da configuração
copy config_dias_filmagem.json config_backup.json

# Backup dos arquivos
xcopy arquivos arquivos_backup /E /I

# Backup das ODs geradas
xcopy arquivos\ODs ODs_backup /E /I
```

### Manutenção Preventiva
- Verificar espaço em disco mensalmente
- Limpar arquivos temporários
- Atualizar antivírus
- Manter Windows atualizado
