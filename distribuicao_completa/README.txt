# Sistema Gerador de OD - Executável v2.0

## Como usar:

### MODO AUTOMÁTICO (Recomendado):
1. **Duplo clique** em `GeradorOD.exe`
2. A interface gráfica será aberta automaticamente
3. Siga as instruções na tela

### Preparação dos Arquivos:
1. Certifique-se de que os arquivos estão na pasta 'arquivos/':
   - DECUPAGEM.csv (planilha com as cenas)
   - PLANO_FINAL.pdf (cronograma de filmagem)
2. Use o botão "📂 Abrir Pasta" na interface para acessar a pasta
3. Use o botão "🔄 Verificar Arquivos" para confirmar que estão corretos

### Interface Gráfica:
- ⚠️ **Aviso laranja**: Lembrete sobre arquivos necessários
- 📁 **Status dos Arquivos**: Mostra se os arquivos foram encontrados
- 📅 **Seleção de Dias**: Escolha quais ODs gerar
  - "🎬 Todos os dias" (padrão) - Gera todas as ODs
  - Ou selecione dias específicos individualmente
- 🚀 **Gerar ODs**: Inicia a geração
- 🗑️ **Limpar ODs**: Remove ODs existentes
- 📊 **Progresso**: Mostra andamento e logs detalhados

### MODO LINHA DE COMANDO (Avançado):
Abra o terminal na pasta do executável e execute:
- `GeradorOD.exe 1` - Gera apenas a OD do dia 1
- `GeradorOD.exe all` - Gera todas as ODs

## Estrutura de pastas necessária:
```
pasta_do_executavel/
├── GeradorOD.exe
├── arquivos/
│   ├── DECUPAGEM.csv
│   ├── PLANO_FINAL.pdf
│   └── ODs/
│       ├── OD_Dia_1.xlsx
│       ├── OD_Dia_2.xlsx
│       └── ...
└── README.txt (este arquivo)
```

## Recursos da Interface:
- ✨ **Design Moderno**: Interface limpa e intuitiva
- 🔄 **Verificação Automática**: Detecta arquivos automaticamente
- 📊 **Progresso Visual**: Barra de progresso e logs em tempo real
- 🎯 **Seleção Flexível**: Gere todos os dias ou apenas os selecionados
- 🛡️ **Validação**: Confirma arquivos antes de gerar
- 🔍 **Logs Detalhados**: Acompanhe cada etapa do processo

## Facilidades de UX/UI:
- **Avisos Visuais**: Cores e ícones indicam status
- **Botões Intuitivos**: Ações claras com emojis descritivos
- **Feedback Imediato**: Confirmações e alertas apropriados
- **Organização Clara**: Seções bem definidas e hierarquia visual
- **Acessibilidade**: Botões grandes e textos legíveis

## Solução de Problemas:

### Interface não abre:
- ✅ Verificar se é Windows 64-bit
- ✅ Executar como administrador se necessário
- ✅ Verificar antivírus (pode estar bloqueando)

### Erro: "Arquivo não encontrado":
- ✅ Usar botão "📂 Abrir Pasta" para verificar localização
- ✅ Verificar se `DECUPAGEM.csv` e `PLANO_FINAL.pdf` estão corretos
- ✅ Usar botão "🔄 Verificar Arquivos" para confirmar

### Geração falha:
- ✅ Verificar logs na área de "📊 Progresso"
- ✅ Confirmar formato dos arquivos (CSV e PDF)
- ✅ Verificar permissões da pasta

## Suporte:
- Use a área de logs da interface para diagnosticar problemas
- Verifique se todos os arquivos estão no formato correto
- Para problemas específicos, contate o desenvolvedor

---

**Sistema Gerador de OD v2.0**
Interface Gráfica Moderna | Developed with ❤️ for Audiovisual Production
