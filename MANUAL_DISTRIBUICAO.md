# Manual de Distribuição - Sistema Gerador de OD

## Resumo
Este documento explica como distribuir o Sistema Gerador de OD como executável para máquinas Windows 10/11 sem necessidade de instalação do Python.

## 📦 Conteúdo da Distribuição

Após executar o build, você terá a pasta `distribuicao_completa/` com:

```
distribuicao_completa/
├── GeradorOD.exe          # Executável principal (±60MB)
├── README.txt             # Manual do usuário
├── exemplo_uso.bat        # Script de exemplo
└── arquivos/
    ├── DECUPAGEM.csv      # Planilha com dados das cenas
    ├── PLANO_FINAL.pdf    # Cronograma de filmagem
    └── ODs/               # Pasta onde serão geradas as ODs
```

## 🚀 Como Gerar o Executável

1. **No ambiente de desenvolvimento**, execute:
   ```bash
   python build_exe.py
   ```

2. **Aguarde o processo** (pode levar alguns minutos)

3. **Copie a pasta** `distribuicao_completa/` para onde desejar distribuir

## 📋 Requisitos para Máquina de Destino

- ✅ Windows 10 ou 11 (64-bit)
- ✅ Nenhuma instalação adicional necessária
- ✅ Aproximadamente 100MB de espaço livre

## 📁 Instalação na Máquina de Destino

1. **Copie** a pasta `distribuicao_completa/` para qualquer local
2. **Substitua** os arquivos na pasta `arquivos/`:
   - `DECUPAGEM.csv` (com seus dados de cenas)
   - `PLANO_FINAL.pdf` (com seu cronograma)
3. **Pronto para usar!**

## 🎮 Como Usar

### Opção 1: Linha de Comando
```bash
# Abrir terminal na pasta do executável
cd caminho/para/distribuicao_completa

# Gerar OD de um dia específico
GeradorOD.exe 1

# Gerar todas as ODs
GeradorOD.exe all
```

### Opção 2: Script .bat
1. **Duplo clique** em `exemplo_uso.bat`
2. **Digite** o comando desejado
3. **Pressione Enter**

### Opção 3: Criar Atalhos
Criar atalhos na área de trabalho para comandos frequentes:
- **Alvo**: `C:\\caminho\\para\\GeradorOD.exe all`
- **Iniciar em**: `C:\\caminho\\para\\distribuicao_completa`

## 📋 Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| `GeradorOD.exe` | Mostra ajuda |
| `GeradorOD.exe 1` | Gera OD do dia 1 |
| `GeradorOD.exe 2` | Gera OD do dia 2 |
| `GeradorOD.exe all` | Gera todas as ODs |

## 📤 Saída

- **Arquivos gerados**: `arquivos/ODs/OD_Dia_X.xlsx`
- **Configuração**: `config_dias_filmagem.json` (gerado automaticamente)
- **Debug**: `arquivos/PLANO_FINAL_debug_text.txt`

## 🐛 Solução de Problemas

### Erro: "Arquivo não encontrado"
- ✅ Verificar se `DECUPAGEM.csv` e `PLANO_FINAL.pdf` estão na pasta `arquivos/`
- ✅ Verificar se a pasta `arquivos/ODs/` existe

### Erro: "Acesso negado"
- ✅ Executar como administrador
- ✅ Verificar permissões da pasta

### Executável não abre
- ✅ Verificar se é Windows 64-bit
- ✅ Verificar antivírus (pode estar bloqueando)
- ✅ Executar pelo terminal para ver mensagens de erro

### Caracteres estranhos no terminal
- ✅ No PowerShell: `chcp 65001` antes de executar
- ✅ No CMD: `chcp 65001` antes de executar

## 📋 Estrutura de Arquivos Necessários

### DECUPAGEM.csv
```csv
CENA,LOCAÇÃO / SET,DESCRIÇÃO CENA,ELENCO,PLANOS,OBSERVAÇÕES CONTITNUIDADE
1,COZINHA CASA ELIÉSER,Manhã. Eliéser prepara café...,Maria Lauro,Plano geral da cozinha,Luz natural
2,LANCHONETE,Tarde. Cliente entra...,Cliente Funcionário,Close-up do rosto,Música ambiente
```

### PLANO_FINAL.pdf
Deve conter o cronograma no formato:
```
ACORDA

DIÁRIA 01: 24/08 - 07h á 17h00
07h00 - 07h30 CAFÉ DA MANHÃ :30
07h30 - 09h30 - PREPARAÇÃO 01 2:00
3 INT QUARTO MARIA E LAURO CASA ELIÉSER Tempo estimado: 1:30 3/8
...
```

## 🔄 Atualizações

Para atualizar o sistema:
1. **Substituir** apenas o arquivo `GeradorOD.exe`
2. **Manter** os arquivos da pasta `arquivos/`
3. **Verificar** se há novos requisitos no README.txt

## 📞 Suporte

Para problemas específicos:
1. **Verificar** este manual primeiro
2. **Executar** pelo terminal para ver mensagens detalhadas
3. **Salvar** o log de erro para análise
4. **Contatar** o desenvolvedor com o log

## 📝 Notas Técnicas

- **Tamanho**: Executável de aproximadamente 60MB
- **Dependências**: Todas incluídas (pandas, openpyxl, pdfplumber, etc.)
- **Compatibilidade**: Windows 10/11 (64-bit)
- **Linguagem**: Interface em português brasileiro
- **Encoding**: UTF-8 para suporte completo a acentos

---

**Gerado automaticamente pelo Sistema Gerador de OD v1.0**
