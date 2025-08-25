import re

# Ler o arquivo
with open('security_check.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir emojis comuns por texto
replacements = {
    '🔍': 'Executando',
    '⏰': 'Timeout',
    '❌': 'Erro',
    '⚠️': 'Aviso',
    '✅': 'Sucesso',
    '🔒': 'Seguranca',
    '📊': 'Relatorio',
    '🛡️': 'Protecao',
    '⛔': 'Bloqueado',
    '🚨': 'Alerta',
    '🔴': 'HIGH',
    '🟡': 'MEDIUM',
    '🟢': 'LOW',
    '📍': 'Local',
    '📦': 'Pacote',
    '📋': 'Lista',
    '💡': 'Dica',
    '🔐': 'Permissoes',
    '→': '->',
    '📄': 'Arquivo',
    '🎉': 'SUCESSO',
    '🔧': 'CORRIGIR'
}

for emoji, replacement in replacements.items():
    content = content.replace(emoji, replacement)

# Substituir acentos comuns
accents = {
    'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a',
    'é': 'e', 'ê': 'e',
    'í': 'i', 'î': 'i',
    'ó': 'o', 'ô': 'o', 'õ': 'o',
    'ú': 'u', 'û': 'u',
    'ç': 'c',
    'Ã': 'A', 'Á': 'A', 'À': 'A', 'Â': 'A',
    'É': 'E', 'Ê': 'E',
    'Í': 'I', 'Î': 'I',
    'Ó': 'O', 'Ô': 'O', 'Õ': 'O',
    'Ú': 'U', 'Û': 'U',
    'Ç': 'C'
}

for accented, plain in accents.items():
    content = content.replace(accented, plain)

# Escrever de volta
with open('security_check.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Arquivo security_check.py corrigido!')
