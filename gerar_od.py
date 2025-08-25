#!/usr/bin/env python3
"""
Sistema Minimalista de Geração de OD
Aplica YAGNI - apenas funcionalidades essenciais
Detecta automaticamente se deve usar GUI ou linha de comando
"""

import sys
import os
from gerador_od_completo import GeradorODCompleto


def main():
    """Interface que detecta se deve usar GUI ou linha de comando"""

    # Se executado sem argumentos, abrir GUI
    if len(sys.argv) < 2:
        try:
            # Tentar importar e executar GUI
            from gerar_od_gui import GeradorODGUI

            app = GeradorODGUI()
            app.run()
            return
        except ImportError:
            # Se não conseguir importar GUI, mostrar ajuda da linha de comando
            print("Sistema de Geracao de OD")
            print("\nUso:")
            print("  GeradorOD.exe [dia]     # Gera OD de um dia especifico")
            print("  GeradorOD.exe all       # Gera todas as ODs")
            print("\nExemplos:")
            print("  GeradorOD.exe 1")
            print("  GeradorOD.exe 3")
            print("  GeradorOD.exe all")
            print("\nOpcoes:")
            print("  --help, -h, help        # Mostra esta mensagem")
            print(
                "\nNota: Para usar a interface grafica, instale: pip install customtkinter pillow"
            )
            return

    # Processamento via linha de comando
    comando = sys.argv[1].lower()

    # Verificar se é pedido de ajuda
    if comando in ["--help", "-h", "help"]:
        print("Sistema de Geracao de OD")
        print("\nUso:")
        print("  GeradorOD.exe [dia]     # Gera OD de um dia especifico")
        print("  GeradorOD.exe all       # Gera todas as ODs")
        print("\nExemplos:")
        print("  GeradorOD.exe 1")
        print("  GeradorOD.exe 3")
        print("  GeradorOD.exe all")
        print("\nOpcoes:")
        print("  --help, -h, help        # Mostra esta mensagem")
        return

    try:
        gerador = GeradorODCompleto()

        if comando == "all":
            print("Gerando todas as ODs...")
            gerador.gerar_todas_ods()
            print("Todas as ODs geradas com sucesso!")
        else:
            dia = int(comando)
            print(f"Gerando OD do Dia {dia}...")
            gerador.gerar_od_dia(dia)
            print(f"OD do Dia {dia} gerada com sucesso!")

    except ValueError:
        print("Erro: Digite um numero valido ou 'all'")
        print("Use 'GeradorOD.exe --help' para ver as opcoes disponíveis")
    except Exception as e:
        print(f"Erro: {str(e)}")


if __name__ == "__main__":
    main()
