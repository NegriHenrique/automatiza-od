# 🎬 Sistema Dinâmico de Geração de OD

## ✨ **Funcionalidade Dinâmica Implementada**

O sistema agora lê automaticamente os dados do projeto atual dos arquivos:

- `arquivos/DECUPAGEM.csv` - Dados detalhados das cenas e planos
- `arquivos/PLANO_FINAL.pdf` - Divisão de cenas por dia (opcional)

## 🔄 **Como Funciona**

### 1. **Leitura Automática da Decupagem**

- Extrai todas as cenas, planos, elenco e locações
- Detecta automaticamente o título do projeto no CSV
- Organiza dados por cena com planos individuais

### 2. **Configuração Dinâmica de Dias**

- Se `PLANO_FINAL.pdf` existir: lê a divisão de dias do PDF
- Se não existir: cria divisão automática (3 cenas por dia)
- Detecta locações principais automaticamente

### 3. **Geração Automática de ODs**

- Cria configuração personalizada para cada projeto
- Adapta horários e atividades às cenas do dia
- Elenco dinâmico baseado nas cenas filmadas

## 📋 **Comandos Disponíveis**

```bash
# Gerar OD de um dia específico
python gerar_od.py 1

# Gerar todas as ODs do projeto
python gerar_od.py ALL

# Gerar ODs de múltiplos dias
python gerar_od.py 1 2 3
```

## 📁 **Estrutura de Arquivos do Projeto**

```
projeto/
├── arquivos/
│   ├── DECUPAGEM.csv        # Dados detalhados (OBRIGATÓRIO)
│   ├── PLANO_FINAL.pdf      # Divisão de dias (OPCIONAL)
│   └── ODs/                 # ODs geradas automaticamente
├── config_dias_filmagem.json # Configuração gerada automaticamente
├── gerar_od.py             # Interface principal
└── gerador_od_completo.py  # Sistema principal
```

## 🎯 **Adaptação para Novos Projetos**

### Para usar com um novo projeto:

1. **Substitua** `arquivos/DECUPAGEM.csv` com os dados do novo projeto
2. **Opcionalmente** adicione `arquivos/PLANO_FINAL.pdf` com a divisão de dias
3. **Execute** `python gerar_od.py ALL` para gerar todas as ODs

O sistema automaticamente:

- ✅ Detecta o novo projeto
- ✅ Gera nova configuração
- ✅ Adapta número de dias
- ✅ Organiza cenas por dia
- ✅ Cria ODs profissionais

## 🔍 **Detecção Automática**

### **Título do Projeto**

- Busca no CSV por linhas com palavras-chave: "FILME", "CURTA", "PROJETO", "SÉRIE"
- Fallback: "PROJETO DINÂMICO"

### **Divisão de Dias**

- PDF: procura padrões "DIA 1", "1° DIA", etc.
- Automático: 3 cenas por dia

### **Locações**

- Detecta "CASA", "EXT", "INT" automaticamente
- Agrupa cenas por locação similar

## 📊 **Exemplo de Saída**

```
🔍 Carregando dados do projeto atual...
✅ 15 cenas carregadas
📽️ Projeto detectado: MEU FILME
✅ Configuração gerada para 5 dias de filmagem

🎬 Gerando 5 ODs para o projeto: MEU FILME
🎬 Gerando OD do Dia 1...
📋 Cenas: 1, 2, 3
📍 Locação: CASA
✅ OD salva: arquivos/ODs/OD_Dia_1.xlsx
```

## 🚀 **Vantagens do Sistema Dinâmico**

- **Zero Configuração Manual**: Tudo automático
- **Adaptável**: Funciona com qualquer projeto
- **Inteligente**: Detecta padrões automaticamente
- **Profissional**: Mantém qualidade visual
- **Rápido**: Gera todas as ODs em segundos

---

### 💡 **O sistema está pronto para ser usado com qualquer projeto de filmagem!**
