#!/usr/bin/env python3
"""
Interface Gráfica Moderna para o Sistema Gerador de OD
Utiliza CustomTkinter para uma aparência moderna e profissional
"""

import sys
import os
import threading
import customtkinter as ctk
from tkinter import messagebox, filedialog
from pathlib import Path
import json
from gerador_od_completo import GeradorODCompleto

# Configurações do tema moderno
ctk.set_appearance_mode("light")  # "light" ou "dark"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


class ToastNotification:
    """Classe para mostrar notificações toast"""

    def __init__(self, parent, message, tipo="info", duration=3000):
        self.parent = parent
        self.duration = duration

        # Cores por tipo com melhor contraste
        colors = {
            "success": {"bg": "#28a745", "text": "#ffffff"},
            "error": {"bg": "#dc3545", "text": "#ffffff"},
            "warning": {"bg": "#ffc107", "text": "#212529"},
            "info": {"bg": "#17a2b8", "text": "#ffffff"},
        }

        color = colors.get(tipo, colors["info"])

        # Criar janela toast
        self.toast = ctk.CTkToplevel(parent)
        self.toast.title("")
        self.toast.geometry("350x80")
        self.toast.resizable(False, False)
        self.toast.attributes("-topmost", True)
        self.toast.overrideredirect(True)

        # Posicionar no canto superior direito
        parent.update_idletasks()
        x = parent.winfo_x() + parent.winfo_width() - 370
        y = parent.winfo_y() + 20
        self.toast.geometry(f"350x80+{x}+{y}")

        # Frame principal com cor de fundo
        frame = ctk.CTkFrame(self.toast, fg_color=color["bg"], corner_radius=8)
        frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Texto da mensagem
        label = ctk.CTkLabel(
            frame,
            text=message,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=color["text"],
            wraplength=320,
        )
        label.pack(expand=True, padx=15, pady=15)

        # Auto fechar
        self.toast.after(duration, self.close)

    def close(self):
        """Fecha o toast"""
        try:
            self.toast.destroy()
        except:
            pass


class GeradorODGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.setup_window()
        self.gerador = GeradorODCompleto()
        self.dias_disponiveis = []
        self.criar_interface()
        self.verificar_arquivos_iniciais()

    def setup_window(self):
        """Configura a janela principal"""
        self.root.title("📋 Ordem do Dia - Sistema de Geração")
        self.root.geometry("600x700")
        self.root.resizable(True, True)

        # Centralizar janela na tela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"600x700+{x}+{y}")

        # Configurar grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

    def criar_interface(self):
        """Cria toda a interface gráfica"""
        self.criar_cabecalho()
        self.criar_area_principal()
        self.criar_rodape()

    def criar_cabecalho(self):
        """Cria o cabeçalho com título e logo"""
        # Frame do cabeçalho com cores melhoradas
        header_frame = ctk.CTkFrame(
            self.root, height=120, corner_radius=0, fg_color="#f8f9fa"
        )
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_propagate(False)

        # Título principal com melhor contraste
        title_label = ctk.CTkLabel(
            header_frame,
            text="📋 Ordem do Dia",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#212529",
        )
        title_label.grid(row=0, column=0, pady=(20, 5))

        # Subtítulo com melhor contraste
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Sistema de geração automática para produções audiovisuais",
            font=ctk.CTkFont(size=14),
            text_color="#6c757d",
        )
        subtitle_label.grid(row=1, column=0, pady=(0, 20))

    def criar_area_principal(self):
        """Cria a área principal com controles"""
        # Frame principal
        main_frame = ctk.CTkFrame(self.root, corner_radius=10, fg_color="#ffffff")
        main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(10, 10))
        main_frame.grid_columnconfigure(0, weight=1)

        # Warning sobre arquivos necessários
        self.criar_aviso_arquivos(main_frame)

        # Status dos arquivos
        self.criar_status_arquivos(main_frame)

        # Seleção de dias
        self.criar_selecao_dias(main_frame)

        # Botões de ação
        self.criar_botoes_acao(main_frame)

        # Área de progresso
        self.criar_area_progresso(main_frame)

    def criar_aviso_arquivos(self, parent):
        """Cria o aviso sobre arquivos necessários"""
        warning_frame = ctk.CTkFrame(parent, fg_color="#fff3cd", corner_radius=8)
        warning_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        warning_frame.grid_columnconfigure(0, weight=1)

        warning_icon = ctk.CTkLabel(
            warning_frame, text="⚠️", font=ctk.CTkFont(size=20), text_color="#856404"
        )
        warning_icon.grid(row=0, column=0, pady=(10, 5))

        warning_text = ctk.CTkLabel(
            warning_frame,
            text="IMPORTANTE: Certifique-se de que os arquivos estão na pasta 'arquivos':\n• DECUPAGEM.csv (dados das cenas)\n• PLANO_FINAL.pdf (cronograma de filmagem)",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#856404",
            justify="center",
        )
        warning_text.grid(row=1, column=0, pady=(0, 15), padx=15)

    def criar_status_arquivos(self, parent):
        """Cria a área de status dos arquivos"""
        status_frame = ctk.CTkFrame(parent, corner_radius=8, fg_color="#f8f9fa")
        status_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 15))
        status_frame.grid_columnconfigure(1, weight=1)

        # Título da seção
        status_title = ctk.CTkLabel(
            status_frame,
            text="📁 Status dos Arquivos",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#212529",
        )
        status_title.grid(row=0, column=0, columnspan=3, pady=(15, 10))

        # Status DECUPAGEM.csv
        self.decupagem_status = ctk.CTkLabel(
            status_frame,
            text="❌ DECUPAGEM.csv",
            font=ctk.CTkFont(size=12),
            text_color="#dc3545",
        )
        self.decupagem_status.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        # Status PLANO_FINAL.pdf
        self.plano_status = ctk.CTkLabel(
            status_frame,
            text="❌ PLANO_FINAL.pdf",
            font=ctk.CTkFont(size=12),
            text_color="#dc3545",
        )
        self.plano_status.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

        # Botão para verificar arquivos
        self.btn_verificar = ctk.CTkButton(
            status_frame,
            text="🔄 Verificar Arquivos",
            command=self.verificar_arquivos_com_toast,
            width=140,
            height=32,
            font=ctk.CTkFont(size=12),
            fg_color="#007bff",
            hover_color="#0056b3",
            text_color="#ffffff",
        )
        self.btn_verificar.grid(row=1, column=2, rowspan=2, padx=(10, 20), pady=10)

        # Botão para abrir pasta
        self.btn_abrir_pasta = ctk.CTkButton(
            status_frame,
            text="📂 Abrir Pasta",
            command=self.abrir_pasta_arquivos,
            width=140,
            height=32,
            font=ctk.CTkFont(size=12),
            fg_color="#6c757d",
            hover_color="#5a6268",
            text_color="#ffffff",
        )
        self.btn_abrir_pasta.grid(row=1, column=1, rowspan=2, padx=10, pady=10)

    def criar_selecao_dias(self, parent):
        """Cria a área de seleção de dias"""
        dias_frame = ctk.CTkFrame(parent, corner_radius=8, fg_color="#f8f9fa")
        dias_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 15))
        dias_frame.grid_columnconfigure(0, weight=1)

        # Título da seção
        dias_title = ctk.CTkLabel(
            dias_frame,
            text="📅 Selecionar Dias para Gerar",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#212529",
        )
        dias_title.grid(row=0, column=0, pady=(15, 10))

        # Opção "Todos os dias" (selecionada por padrão)
        self.todos_dias_var = ctk.BooleanVar(value=True)
        self.todos_dias_checkbox = ctk.CTkCheckBox(
            dias_frame,
            text="🎬 Todos os dias",
            variable=self.todos_dias_var,
            command=self.on_todos_dias_changed,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#007bff",
            fg_color="#007bff",
            hover_color="#0056b3",
        )
        self.todos_dias_checkbox.grid(row=1, column=0, pady=(0, 10))

        # Frame para checkboxes individuais
        self.dias_checkboxes_frame = ctk.CTkFrame(dias_frame, fg_color="transparent")
        self.dias_checkboxes_frame.grid(
            row=2, column=0, sticky="ew", padx=20, pady=(0, 15)
        )
        self.dias_checkboxes_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Placeholder para checkboxes dos dias
        self.dias_vars = {}
        self.dias_checkboxes = {}

    def criar_botoes_acao(self, parent):
        """Cria os botões de ação principal"""
        botoes_frame = ctk.CTkFrame(parent, fg_color="transparent")
        botoes_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=(0, 15))
        botoes_frame.grid_columnconfigure((0, 1), weight=1)

        # Botão Gerar ODs
        self.btn_gerar = ctk.CTkButton(
            botoes_frame,
            text="🚀 Gerar ODs",
            command=self.gerar_ods,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#28a745",
            hover_color="#218838",
            text_color="#ffffff",
        )
        self.btn_gerar.grid(row=0, column=0, padx=(0, 10), sticky="ew")

        # Botão Limpar ODs existentes
        self.btn_limpar = ctk.CTkButton(
            botoes_frame,
            text="🗑️ Limpar ODs",
            command=self.limpar_ods,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#dc3545",
            hover_color="#c82333",
            text_color="#ffffff",
        )
        self.btn_limpar.grid(row=0, column=1, padx=(10, 0), sticky="ew")

    def criar_area_progresso(self, parent):
        """Cria a área de progresso e logs"""
        progress_frame = ctk.CTkFrame(parent, corner_radius=8, fg_color="#f8f9fa")
        progress_frame.grid(row=4, column=0, sticky="nsew", padx=20, pady=(0, 20))
        progress_frame.grid_columnconfigure(0, weight=1)
        progress_frame.grid_rowconfigure(1, weight=1)

        # Título da seção
        progress_title = ctk.CTkLabel(
            progress_frame,
            text="📊 Progresso",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#212529",
        )
        progress_title.grid(row=0, column=0, pady=(15, 10))

        # Barra de progresso
        self.progress_bar = ctk.CTkProgressBar(
            progress_frame, width=400, progress_color="#007bff"
        )
        self.progress_bar.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")
        self.progress_bar.set(0)

        # Área de texto para logs
        self.log_text = ctk.CTkTextbox(
            progress_frame,
            height=150,
            font=ctk.CTkFont(family="Consolas", size=11),
            wrap="word",
            fg_color="#ffffff",
            text_color="#212529",
        )
        self.log_text.grid(row=2, column=0, padx=20, pady=(0, 15), sticky="nsew")

    def criar_rodape(self):
        """Cria o rodapé"""
        footer_frame = ctk.CTkFrame(
            self.root, height=50, corner_radius=0, fg_color="#e9ecef"
        )
        footer_frame.grid(row=2, column=0, sticky="ew", padx=0, pady=0)
        footer_frame.grid_columnconfigure(0, weight=1)
        footer_frame.grid_propagate(False)

        footer_label = ctk.CTkLabel(
            footer_frame,
            text="Ordem do Dia v2.0 | Sistema profissional para produção audiovisual",
            font=ctk.CTkFont(size=10),
            text_color="#6c757d",
        )
        footer_label.grid(row=0, column=0, pady=15)

    def verificar_arquivos_iniciais(self):
        """Verifica arquivos na inicialização"""
        self.log("🚀 Sistema iniciado - verificando arquivos...")
        self.verificar_arquivos()

    def verificar_arquivos_com_toast(self):
        """Verifica arquivos e exibe toast com resultado"""
        self.log("🔍 Verificando arquivos necessários...")

        # Verificar DECUPAGEM.csv
        decupagem_existe = os.path.exists("arquivos/DECUPAGEM.csv")
        if decupagem_existe:
            self.decupagem_status.configure(
                text="✅ DECUPAGEM.csv", text_color="#28a745"
            )
            self.log("✅ DECUPAGEM.csv encontrado")
        else:
            self.decupagem_status.configure(
                text="❌ DECUPAGEM.csv", text_color="#dc3545"
            )
            self.log("❌ DECUPAGEM.csv não encontrado")

        # Verificar PLANO_FINAL.pdf
        plano_existe = os.path.exists("arquivos/PLANO_FINAL.pdf")
        if plano_existe:
            self.plano_status.configure(text="✅ PLANO_FINAL.pdf", text_color="#28a745")
            self.log("✅ PLANO_FINAL.pdf encontrado")
        else:
            self.plano_status.configure(text="❌ PLANO_FINAL.pdf", text_color="#dc3545")
            self.log("❌ PLANO_FINAL.pdf não encontrado")

        # Atualizar botão gerar
        arquivos_ok = decupagem_existe and plano_existe
        if arquivos_ok:
            self.btn_gerar.configure(state="normal")
            self.carregar_dias_disponiveis()
            # Toast de sucesso
            ToastNotification(
                self.root,
                "✅ Todos os arquivos foram encontrados!\nSistema pronto para gerar ODs.",
                "success",
            )
        else:
            self.btn_gerar.configure(state="disabled")
            self.log(
                "⚠️ Arquivos necessários não encontrados - botão de gerar desabilitado"
            )
            # Toast de erro
            arquivos_faltando = []
            if not decupagem_existe:
                arquivos_faltando.append("DECUPAGEM.csv")
            if not plano_existe:
                arquivos_faltando.append("PLANO_FINAL.pdf")

            ToastNotification(
                self.root,
                f"❌ Arquivos não encontrados:\n{', '.join(arquivos_faltando)}",
                "error",
            )

    def verificar_arquivos(self):
        """Verifica se os arquivos necessários existem (sem toast)"""
        self.log("🔍 Verificando arquivos necessários...")

        # Verificar DECUPAGEM.csv
        decupagem_existe = os.path.exists("arquivos/DECUPAGEM.csv")
        if decupagem_existe:
            self.decupagem_status.configure(
                text="✅ DECUPAGEM.csv", text_color="#28a745"
            )
            self.log("✅ DECUPAGEM.csv encontrado")
        else:
            self.decupagem_status.configure(
                text="❌ DECUPAGEM.csv", text_color="#dc3545"
            )
            self.log("❌ DECUPAGEM.csv não encontrado")

        # Verificar PLANO_FINAL.pdf
        plano_existe = os.path.exists("arquivos/PLANO_FINAL.pdf")
        if plano_existe:
            self.plano_status.configure(text="✅ PLANO_FINAL.pdf", text_color="#28a745")
            self.log("✅ PLANO_FINAL.pdf encontrado")
        else:
            self.plano_status.configure(text="❌ PLANO_FINAL.pdf", text_color="#dc3545")
            self.log("❌ PLANO_FINAL.pdf não encontrado")

        # Atualizar botão gerar
        arquivos_ok = decupagem_existe and plano_existe
        if arquivos_ok:
            self.btn_gerar.configure(state="normal")
            self.carregar_dias_disponiveis()
        else:
            self.btn_gerar.configure(state="disabled")
            self.log(
                "⚠️ Arquivos necessários não encontrados - botão de gerar desabilitado"
            )

    def carregar_dias_disponiveis(self):
        """Carrega os dias disponíveis do plano de filmagem"""
        try:
            self.log("📅 Carregando dias disponíveis do plano...")

            # Carregar dados usando o gerador
            if self.gerador._carregar_dados():
                self.dias_disponiveis = list(
                    self.gerador.config["dias_filmagem"].keys()
                )
                self.log(
                    f"📅 {len(self.dias_disponiveis)} dias encontrados: {', '.join(self.dias_disponiveis)}"
                )
                self.criar_checkboxes_dias()
            else:
                self.log("❌ Erro ao carregar dados do plano")

        except Exception as e:
            self.log(f"❌ Erro ao carregar dias: {str(e)}")

    def criar_checkboxes_dias(self):
        """Cria checkboxes para cada dia disponível"""
        # Limpar checkboxes existentes
        for widget in self.dias_checkboxes_frame.winfo_children():
            widget.destroy()

        self.dias_vars.clear()
        self.dias_checkboxes.clear()

        # Criar checkboxes para cada dia
        for i, dia in enumerate(self.dias_disponiveis):
            var = ctk.BooleanVar(value=False)
            self.dias_vars[dia] = var

            checkbox = ctk.CTkCheckBox(
                self.dias_checkboxes_frame,
                text=f"📅 Dia {dia}",
                variable=var,
                command=self.on_dia_individual_changed,
                font=ctk.CTkFont(size=12),
                text_color="#212529",
                fg_color="#007bff",
                hover_color="#0056b3",
                state="disabled",  # Inicialmente desabilitado (todos os dias selecionado)
            )

            # Organizar em grid (3 colunas)
            row = i // 3
            col = i % 3
            checkbox.grid(row=row, column=col, padx=10, pady=5, sticky="w")

            self.dias_checkboxes[dia] = checkbox

    def on_todos_dias_changed(self):
        """Callback quando 'todos os dias' é alterado"""
        todos_selecionado = self.todos_dias_var.get()

        # Habilitar/desabilitar checkboxes individuais
        for checkbox in self.dias_checkboxes.values():
            if todos_selecionado:
                checkbox.configure(state="disabled")
            else:
                checkbox.configure(state="normal")

        # Se todos os dias foi desmarcado, não selecionar nenhum individual
        if not todos_selecionado:
            for var in self.dias_vars.values():
                var.set(False)

    def on_dia_individual_changed(self):
        """Callback quando um dia individual é alterado"""
        # Se algum dia individual foi selecionado, desmarcar 'todos os dias'
        algum_selecionado = any(var.get() for var in self.dias_vars.values())
        if algum_selecionado:
            self.todos_dias_var.set(False)

    def abrir_pasta_arquivos(self):
        """Abre a pasta arquivos no explorador"""
        try:
            pasta_arquivos = Path("arquivos").absolute()
            if not pasta_arquivos.exists():
                pasta_arquivos.mkdir(parents=True)
                self.log("📂 Pasta 'arquivos' criada")

            os.startfile(pasta_arquivos)
            self.log("📂 Pasta 'arquivos' aberta no explorador")
        except Exception as e:
            self.log(f"❌ Erro ao abrir pasta: {str(e)}")
            messagebox.showerror("Erro", f"Não foi possível abrir a pasta: {str(e)}")

    def limpar_ods(self):
        """Remove todas as ODs existentes"""
        try:
            pasta_ods = Path("arquivos/ODs")
            if not pasta_ods.exists():
                messagebox.showinfo("Info", "Nenhuma OD encontrada para limpar.")
                return

            arquivos_od = list(pasta_ods.glob("OD_Dia_*.xlsx"))
            if not arquivos_od:
                messagebox.showinfo("Info", "Nenhuma OD encontrada para limpar.")
                return

            resposta = messagebox.askyesno(
                "Confirmar Limpeza",
                f"Tem certeza que deseja remover {len(arquivos_od)} arquivo(s) de OD existente(s)?",
            )

            if resposta:
                for arquivo in arquivos_od:
                    arquivo.unlink()
                    self.log(f"🗑️ Removido: {arquivo.name}")

                self.log(f"✅ {len(arquivos_od)} arquivo(s) de OD removido(s)")
                messagebox.showinfo(
                    "Sucesso",
                    f"{len(arquivos_od)} arquivo(s) de OD removido(s) com sucesso!",
                )

        except Exception as e:
            self.log(f"❌ Erro ao limpar ODs: {str(e)}")
            messagebox.showerror("Erro", f"Erro ao limpar ODs: {str(e)}")

    def gerar_ods(self):
        """Gera as ODs selecionadas"""
        # Verificar o que foi selecionado
        if self.todos_dias_var.get():
            dias_para_gerar = self.dias_disponiveis
            self.log("🎬 Iniciando geração de TODAS as ODs...")
        else:
            dias_para_gerar = [dia for dia, var in self.dias_vars.items() if var.get()]

        if not dias_para_gerar:
            messagebox.showwarning("Aviso", "Selecione pelo menos um dia para gerar!")
            return

        self.log(f"🎬 Iniciando geração de ODs para: {', '.join(dias_para_gerar)}")

        # Desabilitar botões durante geração
        self.btn_gerar.configure(state="disabled")
        self.btn_limpar.configure(state="disabled")

        # Executar geração em thread separada
        thread = threading.Thread(
            target=self.executar_geracao, args=(dias_para_gerar,), daemon=True
        )
        thread.start()

    def executar_geracao(self, dias_para_gerar):
        """Executa a geração das ODs em thread separada"""
        try:
            total_dias = len(dias_para_gerar)
            sucessos = 0
            falhas = 0

            self.progress_bar.set(0)

            for i, dia in enumerate(dias_para_gerar):
                self.log(f"📅 Processando Dia {dia}...")

                try:
                    if self.gerador.gerar_od_dia(int(dia)):
                        sucessos += 1
                        self.log(f"✅ OD do Dia {dia} gerada com sucesso!")
                    else:
                        falhas += 1
                        self.log(f"❌ Falha ao gerar OD do Dia {dia}")

                except Exception as e:
                    falhas += 1
                    self.log(f"❌ Erro ao gerar OD do Dia {dia}: {str(e)}")

                # Atualizar progresso
                progresso = (i + 1) / total_dias
                self.progress_bar.set(progresso)

            # Resultado final
            self.log(f"\n📊 Geração concluída:")
            self.log(f"   ✅ Sucessos: {sucessos}")
            self.log(f"   ❌ Falhas: {falhas}")
            self.log(f"   📅 Total: {total_dias}")

            # Mostrar resultado
            if falhas == 0:
                messagebox.showinfo(
                    "Sucesso!", f"Todas as {sucessos} ODs foram geradas com sucesso! 🎉"
                )
            else:
                messagebox.showwarning(
                    "Concluído com Avisos",
                    f"Geração concluída:\n✅ {sucessos} sucessos\n❌ {falhas} falhas\n\nVerifique o log para detalhes.",
                )

        except Exception as e:
            self.log(f"❌ Erro geral na geração: {str(e)}")
            messagebox.showerror("Erro", f"Erro durante a geração: {str(e)}")

        finally:
            # Reabilitar botões
            self.btn_gerar.configure(state="normal")
            self.btn_limpar.configure(state="normal")

    def log(self, mensagem):
        """Adiciona mensagem ao log"""
        self.log_text.insert("end", f"{mensagem}\n")
        self.log_text.see("end")
        self.root.update_idletasks()

    def run(self):
        """Inicia a aplicação"""
        self.root.mainloop()


def main():
    """Função principal"""
    # Verificar se está no diretório correto
    if not os.path.exists("arquivos"):
        os.makedirs("arquivos", exist_ok=True)

    # Criar e executar aplicação
    app = GeradorODGUI()
    app.run()


if __name__ == "__main__":
    main()
