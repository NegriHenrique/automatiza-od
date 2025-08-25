#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar executavel do Sistema de Geracao de OD
"""

import PyInstaller.__main__
import os
import shutil
from pathlib import Path


def limpar_build():
    """Remove diretorios de build anteriores"""
    dirs_para_remover = ["build", "dist", "__pycache__"]
    for dir_name in dirs_para_remover:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"OK Removido: {dir_name}")


def criar_executavel():
    """Cria o executavel com PyInstaller"""
    print("Gerando executavel...")

    # Argumentos do PyInstaller com configuracoes de seguranca
    args = [
        "gerar_od.py",  # Arquivo principal
        "--onefile",  # Gerar um unico arquivo
        "--name=GeradorOD",  # Nome do executavel
        "--icon=NONE",  # Sem icone por enquanto
        "--windowed",  # Sem console (GUI)
        "--clean",  # Limpar cache
        "--noconfirm",  # Nao pedir confirmacao
        "--add-data=arquivos;arquivos",  # Incluir pasta arquivos
        "--distpath=distribuicao",  # Pasta de saida
        "--workpath=build_temp",  # Pasta temporaria
        "--hidden-import=customtkinter",  # Incluir customtkinter
        "--hidden-import=PIL",  # Incluir Pillow
        "--hidden-import=PIL._tkinter_finder",  # Fix para tkinter
        # Configuracoes de seguranca para reduzir alertas do Windows
        "--exclude-module=PyQt5",  # Excluir modulos desnecessarios
        "--exclude-module=PyQt6",
        "--exclude-module=tkinter.test",
        "--exclude-module=test",
        "--exclude-module=unittest",
        "--exclude-module=doctest",
        # Otimizações
        "--strip",  # Remover símbolos de debug
        "--optimize=2",  # Otimização máxima
        # Informações de versão (ajuda com alertas de segurança)
        "--version-file=version_info.txt",  # Arquivo de versão (se existir)
    ]

    # Adicionar arquivo de versão se não existir
    create_version_file()

    PyInstaller.__main__.run(args)
    print("Executavel gerado!")


def create_version_file():
    """Cria arquivo de informações de versão para o executável"""
    version_content = """# UTF-8
#
# Para mais detalhes sobre estrutura de versão, veja:
# https://docs.microsoft.com/en-us/windows/win32/menurc/versioninfo-resource

VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(2, 0, 0, 0),
    prodvers=(2, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Ordem do Dia - Produção Audiovisual'),
        StringStruct(u'FileDescription', u'Sistema Gerador de Ordem do Dia'),
        StringStruct(u'FileVersion', u'2.0.0.0'),
        StringStruct(u'InternalName', u'GeradorOD'),
        StringStruct(u'LegalCopyright', u'Copyright © 2025 - Sistema Ordem do Dia'),
        StringStruct(u'OriginalFilename', u'GeradorOD.exe'),
        StringStruct(u'ProductName', u'Gerador de Ordem do Dia'),
        StringStruct(u'ProductVersion', u'2.0.0.0')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)"""

    with open("version_info.txt", "w", encoding="utf-8") as f:
        f.write(version_content)
    print("Arquivo de versao criado")


def criar_estrutura_distribuicao():
    """Cria estrutura para distribuicao"""
    print("Criando estrutura de distribuicao...")

    # Criar pasta principal
    dist_path = Path("distribuicao_completa")
    if dist_path.exists():
        shutil.rmtree(dist_path)

    dist_path.mkdir()

    # Copiar executavel
    exe_source = Path("distribuicao/GeradorOD.exe")
    if exe_source.exists():
        shutil.copy2(exe_source, dist_path / "GeradorOD.exe")
        print("Executavel copiado")

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
            print(f"OK Copiado: {arquivo}")

    # Criar pasta ODs vazia
    ods_path = arquivos_dist / "ODs"
    ods_path.mkdir()
    print("OK Pasta ODs criada")

    # Criar arquivo README de distribuição
    readme_content = """# Sistema Gerador de OD - Executavel v2.0

## Como usar:

### MODO AUTOMATICO (Recomendado):
1. **Duplo clique** em `GeradorOD.exe`
2. A interface grafica sera aberta automaticamente
3. Siga as instrucoes na tela

### Preparacao dos Arquivos:
1. Certifique-se de que os arquivos estao na pasta 'arquivos/':
   - DECUPAGEM.csv (planilha com as cenas)
   - PLANO_FINAL.pdf (cronograma de filmagem)
2. Use o botao "Abrir Pasta" na interface para acessar a pasta
3. Use o botao "Verificar Arquivos" para confirmar que estao corretos

### Interface Grafica:
- **Aviso laranja**: Lembrete sobre arquivos necessarios
- **Status dos Arquivos**: Mostra se os arquivos foram encontrados
- **Selecao de Dias**: Escolha quais ODs gerar
  - "Todos os dias" (padrao) - Gera todas as ODs
  - Ou selecione dias especificos individualmente
- **Gerar ODs**: Inicia a geracao
- **Limpar ODs**: Remove ODs existentes
- **Progresso**: Mostra andamento e logs detalhados

### MODO LINHA DE COMANDO (Avancado):
Abra o terminal na pasta do executavel e execute:
- `GeradorOD.exe 1` - Gera apenas a OD do dia 1
- `GeradorOD.exe all` - Gera todas as ODs

## Estrutura de pastas necessaria:
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
- **Design Moderno**: Interface limpa e intuitiva
- **Verificacao Automatica**: Detecta arquivos automaticamente
- **Progresso Visual**: Barra de progresso e logs em tempo real
- **Selecao Flexivel**: Gere todos os dias ou apenas os selecionados
- **Validacao**: Confirma arquivos antes de gerar
- **Logs Detalhados**: Acompanhe cada etapa do processo

## Facilidades de UX/UI:
- **Avisos Visuais**: Cores e icones indicam status
- **Botoes Intuitivos**: Acoes claras com icones descritivos
- **Feedback Imediato**: Confirmacoes e alertas apropriados
- **Organizacao Clara**: Secoes bem definidas e hierarquia visual
- **Acessibilidade**: Botoes grandes e textos legiveis

## Solucao de Problemas:

### Interface nao abre:
- Verificar se e Windows 64-bit
- Executar como administrador se necessario
- Verificar antivirus (pode estar bloqueando)

### Erro: "Arquivo nao encontrado":
- Usar botao "Abrir Pasta" para verificar localizacao
- Verificar se `DECUPAGEM.csv` e `PLANO_FINAL.pdf` estao corretos
- Usar botao "Verificar Arquivos" para confirmar

### Geracao falha:
- Verificar logs na area de "Progresso"
- Confirmar formato dos arquivos (CSV e PDF)
- Verificar permissoes da pasta

## Suporte:
- Use a area de logs da interface para diagnosticar problemas
- Verifique se todos os arquivos estao no formato correto
- Para problemas especificos, contate o desenvolvedor

---

**Sistema Gerador de OD v2.0**
Interface Grafica Moderna | Developed for Audiovisual Production
"""

    with open(dist_path / "README.txt", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README criado")

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

    print("Script de exemplo criado")
    print(f"Distribuicao completa criada em: {dist_path.absolute()}")


def main():
    print("Iniciando build do executavel...")

    # Limpar builds anteriores
    limpar_build()

    # Criar executavel
    criar_executavel()

    # Criar estrutura de distribuicao
    criar_estrutura_distribuicao()

    print("\nBuild concluido com sucesso!")
    print("Pasta de distribuicao: distribuicao_completa/")
    print("Para testar: cd distribuicao_completa && GeradorOD.exe all")


if __name__ == "__main__":
    main()
