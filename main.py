import tkinter as tk
from tkinter import filedialog, messagebox

from calculadora_ir import calcular_ir
from formatador import formatar_moeda, formatar_porcentagem
from exportador import exportar_txt, exportar_pdf


def converter_valor(texto):
    texto = texto.replace(",", ".")
    return float(texto)


def atualizar_resultado(texto):
    texto_resultado.config(state="normal")
    texto_resultado.delete("1.0", tk.END)
    texto_resultado.insert("1.0", texto)
    texto_resultado.config(state="disabled")


def obter_resultado():
    return texto_resultado.get("1.0", tk.END).strip()


def calcular():
    try:
        salario_bruto = converter_valor(campo_salario.get())
        desconto_inss = converter_valor(campo_inss.get())
        dependentes = int(campo_dependentes.get())
        outras_deducoes = converter_valor(campo_outras.get())

        if salario_bruto < 0 or desconto_inss < 0 or dependentes < 0 or outras_deducoes < 0:
            messagebox.showerror("Erro", "Os valores não podem ser negativos.")
            return

        resultado = calcular_ir(
            salario_bruto,
            desconto_inss,
            dependentes,
            outras_deducoes
        )

        texto = (
            f"Resultado da Simulação\n\n"
            f"Salário bruto: {formatar_moeda(resultado['salario_bruto'])}\n"
            f"Desconto INSS: {formatar_moeda(resultado['desconto_inss'])}\n"
            f"Dependentes: {resultado['dependentes']}\n"
            f"Dedução por dependentes: {formatar_moeda(resultado['deducao_dependentes'])}\n"
            f"Outras deduções: {formatar_moeda(resultado['outras_deducoes'])}\n\n"
            f"Base de cálculo: {formatar_moeda(resultado['base_calculo'])}\n"
            f"Alíquota aplicada: {formatar_porcentagem(resultado['aliquota'])}\n"
            f"Parcela a deduzir: {formatar_moeda(resultado['parcela_deduzir'])}\n\n"
            f"Imposto de Renda devido: {formatar_moeda(resultado['ir_final'])}\n"
            f"Salário líquido aproximado: {formatar_moeda(resultado['salario_liquido'])}"
        )

        atualizar_resultado(texto)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite apenas números válidos. Exemplo: 3500 ou 3500,50"
        )


def limpar():
    campo_salario.delete(0, tk.END)
    campo_inss.delete(0, tk.END)
    campo_dependentes.delete(0, tk.END)
    campo_outras.delete(0, tk.END)

    campo_dependentes.insert(0, "0")
    campo_outras.insert(0, "0")

    atualizar_resultado("Preencha os dados e clique em calcular.")
    
def salvar_txt():
    texto = obter_resultado()

    if texto == "Preencha os dados e clique em calcular.":
        messagebox.showwarning(
            "Atenção",
            "Calcule primeiro antes de exportar."
        )
        return

    caminho = filedialog.asksaveasfilename(
        title="Salvar Relatório TXT",
        defaultextension=".txt",
        filetypes=[
            ("Arquivo TXT", "*.txt")
        ],
        initialfile="relatorio_ir.txt"
    )

    if caminho:

        exportar_txt(texto, caminho)

        messagebox.showinfo(
            "Sucesso",
            "TXT exportado com sucesso!"
        )


def salvar_pdf():
    texto = obter_resultado()

    if texto == "Preencha os dados e clique em calcular.":
        messagebox.showwarning(
            "Atenção",
            "Calcule primeiro antes de exportar."
        )
        return

    caminho = filedialog.asksaveasfilename(
        title="Salvar PDF",
        defaultextension=".pdf",
        filetypes=[("Arquivo PDF", "*.pdf")],
        initialfile="relatorio_ir.pdf"
    )

    if caminho:
        exportar_pdf(texto, caminho)

        messagebox.showinfo(
            "Sucesso",
            "PDF exportado com sucesso!"
        )

janela = tk.Tk()
janela.title("Simulador de IR sobre Salário Mensal")
janela.geometry("620x740")
janela.configure(bg="#f4f6f8")
janela.resizable(True, True)

titulo = tk.Label(
    janela,
    text="Simulador de Imposto de Renda Mensal",
    font=("Arial", 18, "bold"),
    bg="#f4f6f8",
    fg="#1f2937"
)
titulo.pack(pady=20)

subtitulo = tk.Label(
    janela,
    text="Informe os dados abaixo para calcular o IR sobre o salário mensal",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#4b5563"
)
subtitulo.pack(pady=5)

frame_formulario = tk.Frame(janela, bg="#ffffff", padx=25, pady=20)
frame_formulario.pack(pady=15)

def criar_campo(texto, linha):
    label = tk.Label(
        frame_formulario,
        text=texto,
        font=("Arial", 11, "bold"),
        bg="#ffffff",
        fg="#374151"
    )
    label.grid(row=linha, column=0, sticky="w", pady=8)

    campo = tk.Entry(
        frame_formulario,
        font=("Arial", 11),
        width=25,
        bd=1,
        relief="solid"
    )
    campo.grid(row=linha, column=1, pady=8, padx=10)

    return campo


campo_salario = criar_campo("Salário bruto:", 0)
campo_inss = criar_campo("Desconto INSS:", 1)
campo_dependentes = criar_campo("Quantidade de dependentes:", 2)
campo_outras = criar_campo("Outras deduções:", 3)

campo_dependentes.insert(0, "0")
campo_outras.insert(0, "0")

frame_botoes = tk.Frame(janela, bg="#f4f6f8")
frame_botoes.pack(pady=10)

botao_calcular = tk.Button(
    frame_botoes,
    text="Calcular IR",
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    padx=20,
    pady=8,
    command=calcular
)
botao_calcular.grid(row=0, column=0, padx=8)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    font=("Arial", 11, "bold"),
    bg="#6b7280",
    fg="white",
    padx=20,
    pady=8,
    command=limpar
)
botao_limpar.grid(row=0, column=1, padx=8)

botao_txt = tk.Button(
    frame_botoes,
    text="Exportar TXT",
    font=("Arial", 10, "bold"),
    bg="#16a34a",
    fg="white",
    padx=14,
    pady=8,
    command=salvar_txt
)
botao_txt.grid(row=0, column=2, padx=5)

botao_pdf = tk.Button(
    frame_botoes,
    text="Exportar PDF",
    font=("Arial", 10, "bold"),
    bg="#dc2626",
    fg="white",
    padx=14,
    pady=8,
    command=salvar_pdf
)
botao_pdf.grid(row=0, column=3, padx=5)


frame_resultado = tk.Frame(janela, bg="#f4f6f8")
frame_resultado.pack(pady=15, fill="both", expand=True)

scroll_resultado = tk.Scrollbar(frame_resultado)
scroll_resultado.pack(side="right", fill="y")

texto_resultado = tk.Text(
    frame_resultado,
    font=("Arial", 11),
    bg="#ffffff",
    fg="#111827",
    wrap="word",
    padx=15,
    pady=10,
    width=60,
    height=18,
    relief="solid",
    bd=1,
    yscrollcommand=scroll_resultado.set
)
texto_resultado.pack(side="left", fill="both", expand=True)
texto_resultado.config(state="disabled")
scroll_resultado.config(command=texto_resultado.yview)

atualizar_resultado("Preencha os dados e clique em calcular.")

rodape = tk.Label(
    janela,
    text="Projeto A3 - Matemática Computacional Aplicada",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#6b7280"
)
rodape.pack(pady=5)

janela.mainloop()