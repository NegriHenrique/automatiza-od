#!/usr/bin/env python3
"""
Script para gerar executável do Sistema de Geração de OD
"""

import PyInstaller.__main__
import os
import shutil
from pathlib import Path


def limpar_build():
    """Remove diretórios de build anteriores"""
    dirs_para_remover = ["build", "dist", "__pycache__"]
    for dir_name in dirs_para_remover:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✅ Removido: {dir_name}")


def criar_executavel():
    """Cria o executável com PyInstaller"""
    print("🔨 Gerando executável...")

    # Argumentos do PyInstaller
    args = [
        "gerar_od.py",  # Arquivo principal
        "--onefile",  # Gerar um único arquivo
        "--name=GeradorOD",  # Nome do executável
        "--icon=NONE",  # Sem ícone por enquanto
        "--windowed",  # Sem console (GUI)
        "--clean",  # Limpar cache
        "--noconfirm",  # Não pedir confirmação
        "--add-data=arquivos;arquivos",  # Incluir pasta arquivos
        "--distpath=distribuicao",  # Pasta de saída
        "--workpath=build_temp",  # Pasta temporária
        "--hidden-import=customtkinter",  # Incluir customtkinter
        "--hidden-import=PIL",  # Incluir Pillow
        "--hidden-import=PIL._tkinter_finder",  # Fix para tkinter
    ]

    PyInstaller.__main__.run(args)
    print("✅ Executável gerado!")


def criar_estrutura_distribuicao():
    """Cria estrutura para distribuição"""
    print("📦 Criando estrutura de distribuição...")

    # Criar pasta principal
    dist_path = Path("distribuicao_completa")
    if dist_path.exists():
        shutil.rmtree(dist_path)

    dist_path.mkdir()

    # Copiar executável
    exe_source = Path("distribuicao/GeradorOD.exe")
    if exe_source.exists():
        shutil.copy2(exe_source, dist_path / "GeradorOD.exe")
        print("✅ Executável copiado")

    # Criar pasta arquivos com estrutura necessária
    arquivos_dist = dist_path / "arquivos"
    arquivos_dist.mkdir()

    # Copiar arquivos necessários
    arquivos_necessarios = ["arquivos/DECUPAGEM.csv", "arquivos/PLANO_FINAL.pdf"]

    for arquivo in arquivos_necessarios:
        if os.path.exists(arquivo):
            dest = dist_path / arquivo
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(arquivo, dest)
            print(f"✅ Copiado: {arquivo}")

    # Criar pasta ODs vazia
    ods_path = arquivos_dist / "ODs"
    ods_path.mkdir()
    print("✅ Pasta ODs criada")

    # Criar arquivo README de distribuição
    readme_content = """# Sistema Gerador de OD - Executável v2.0

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
"""

    with open(dist_path / "README.txt", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ README criado")

    # Criar script de exemplo para Windows
    bat_content = """@echo off
echo Sistema Gerador de OD
echo.
echo Exemplos de uso:
echo   GeradorOD.exe 1     - Gera OD do dia 1
echo   GeradorOD.exe all   - Gera todas as ODs
echo.
pause
"""

    with open(dist_path / "exemplo_uso.bat", "w", encoding="utf-8") as f:
        f.write(bat_content)

    print("✅ Script de exemplo criado")
    print(f"📦 Distribuição completa criada em: {dist_path.absolute()}")


def main():
    print("🚀 Iniciando build do executável...")

    # Limpar builds anteriores
    limpar_build()

    # Criar executável
    criar_executavel()

    # Criar estrutura de distribuição
    criar_estrutura_distribuicao()

    print("\n🎉 Build concluído com sucesso!")
    print("📁 Pasta de distribuição: distribuicao_completa/")
    print("💡 Para testar: cd distribuicao_completa && GeradorOD.exe all")


if __name__ == "__main__":
    main()
