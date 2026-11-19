import tkinter as tk
from tkinter import messagebox, ttk


class CadastroClienteApp:
    """Formulário simples para cadastrar clientes em memória."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Cadastro de cliente")
        self.root.resizable(False, False)

        self.nome = tk.StringVar()
        self.filiacao = tk.StringVar()
        self.documento = tk.StringVar()
        self.data_nascimento = tk.StringVar()
        self.endereco = tk.StringVar()
        self.estado_civil = tk.StringVar()
        self.sexo = tk.StringVar()

        self._criar_formulario()
        self._criar_tabela()

    def _criar_formulario(self) -> None:
        formulario = ttk.LabelFrame(self.root, text="Dados do cliente", padding=12)
        formulario.grid(row=0, column=0, padx=12, pady=12, sticky="ew")

        campos = (
            ("Nome:", self.nome),
            ("Filiação:", self.filiacao),
            ("Documento:", self.documento),
            ("Data de nascimento (DD/MM/AAAA):", self.data_nascimento),
            ("Endereço:", self.endereco),
        )

        for linha, (rotulo, variavel) in enumerate(campos):
            ttk.Label(formulario, text=rotulo).grid(
                row=linha, column=0, padx=(0, 8), pady=4, sticky="w"
            )
            ttk.Entry(formulario, textvariable=variavel, width=42).grid(
                row=linha, column=1, pady=4, sticky="ew"
            )

        ttk.Label(formulario, text="Estado civil:").grid(
            row=5, column=0, padx=(0, 8), pady=4, sticky="w"
        )
        ttk.Combobox(
            formulario,
            textvariable=self.estado_civil,
            values=("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)"),
            state="readonly",
            width=39,
        ).grid(row=5, column=1, pady=4, sticky="ew")

        ttk.Label(formulario, text="Sexo:").grid(
            row=6, column=0, padx=(0, 8), pady=4, sticky="w"
        )
        ttk.Combobox(
            formulario,
            textvariable=self.sexo,
            values=("Feminino", "Masculino", "Não informar"),
            state="readonly",
            width=39,
        ).grid(row=6, column=1, pady=4, sticky="ew")

        botoes = ttk.Frame(formulario)
        botoes.grid(row=7, column=0, columnspan=2, pady=(10, 0), sticky="e")
        ttk.Button(botoes, text="Limpar", command=self._limpar).pack(
            side="left", padx=(0, 8)
        )
        ttk.Button(botoes, text="Cadastrar", command=self._cadastrar).pack(side="left")

    def _criar_tabela(self) -> None:
        area_lista = ttk.LabelFrame(self.root, text="Clientes cadastrados", padding=8)
        area_lista.grid(row=1, column=0, padx=12, pady=(0, 12), sticky="nsew")

        colunas = ("nome", "documento", "nascimento", "estado_civil", "sexo")
        self.tabela = ttk.Treeview(area_lista, columns=colunas, show="headings", height=7)
        titulos = {
            "nome": "Nome",
            "documento": "Documento",
            "nascimento": "Nascimento",
            "estado_civil": "Estado civil",
            "sexo": "Sexo",
        }
        larguras = {
            "nome": 180,
            "documento": 120,
            "nascimento": 120,
            "estado_civil": 120,
            "sexo": 100,
        }
        for coluna in colunas:
            self.tabela.heading(coluna, text=titulos[coluna])
            self.tabela.column(coluna, width=larguras[coluna], anchor="w")
        self.tabela.pack()

    def _cadastrar(self) -> None:
        campos_obrigatorios = (
            ("Nome", self.nome.get()),
            ("Documento", self.documento.get()),
            ("Data de nascimento", self.data_nascimento.get()),
            ("Endereço", self.endereco.get()),
            ("Estado civil", self.estado_civil.get()),
            ("Sexo", self.sexo.get()),
        )
        faltantes = [nome for nome, valor in campos_obrigatorios if not valor.strip()]
        if faltantes:
            messagebox.showwarning(
                "Dados incompletos",
                f"Preencha os campos obrigatórios: {', '.join(faltantes)}.",
            )
            return

        self.tabela.insert(
            "",
            "end",
            values=(
                self.nome.get().strip(),
                self.documento.get().strip(),
                self.data_nascimento.get().strip(),
                self.estado_civil.get(),
                self.sexo.get(),
            ),
        )
        messagebox.showinfo("Cadastro realizado", "Cliente cadastrado com sucesso.")
        self._limpar()

    def _limpar(self) -> None:
        for variavel in (
            self.nome,
            self.filiacao,
            self.documento,
            self.data_nascimento,
            self.endereco,
            self.estado_civil,
            self.sexo,
        ):
            variavel.set("")


if __name__ == "__main__":
    janela = tk.Tk()
    CadastroClienteApp(janela)
    janela.mainloop()
