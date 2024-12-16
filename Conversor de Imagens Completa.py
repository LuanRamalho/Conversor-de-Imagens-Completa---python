import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import os

def escolher_imagem():
    global caminho_imagem
    caminho_imagem = filedialog.askopenfilename(title="Selecionar Imagem")
    if caminho_imagem:
        label_imagem["text"] = os.path.basename(caminho_imagem)  # Exibe o nome do arquivo

def converter_imagem():
    if not caminho_imagem:
        messagebox.showerror("Erro", "Selecione uma imagem primeiro!")
        return
    
    formato_saida = combo_saida.get()
    if not formato_saida:
        messagebox.showerror("Erro", "Selecione um formato de saída")
        return

    try:
        img = Image.open(caminho_imagem)
        nome_base, extensao = os.path.splitext(caminho_imagem)
        novo_caminho = nome_base + "." + formato_saida.lower() # Nomeia o arquivo de saida
        img.save(novo_caminho)
        messagebox.showinfo("Sucesso", f"Imagem convertida para {formato_saida}!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na conversão: {e}")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Conversor de Imagens")
janela.config(bg="#00FFBA")

# Widgets
label_entrada = tk.Label(janela, text="Formato de Entrada:", font=("Arial",12), bg="#00FFBA")
label_saida = tk.Label(janela, text="Formato de Saída:", font=("Arial",12), bg="#00FFBA")
formatos = ["JPG", "BMP", "GIF", "WEBP", "TIFF", "PNG"] 
combo_entrada = ttk.Combobox(janela, values=formatos, state="readonly", font=("Arial",12))
combo_saida = ttk.Combobox(janela, values=formatos, state="readonly", font=("Arial",12))
botao_escolher = tk.Button(janela, text="Escolher Imagem", command=escolher_imagem, font=("Arial",12, "bold"), bg="#4C0073", fg="#F5FFA4")
botao_converter = tk.Button(janela, text="Converter", command=converter_imagem, font=("Arial",12, "bold"), bg="#00483A", fg="#C7FF8A")
label_imagem = tk.Label(janela, text="Nenhuma imagem selecionada", font=("Arial",14,"bold"), bg="#00FFBA", fg="#5D002A")

# Layout (Grid) - Exemplo simples
label_entrada.grid(row=0, column=0, padx=5, pady=5)
combo_entrada.grid(row=0, column=1, padx=5, pady=5)
label_saida.grid(row=1, column=0, padx=5, pady=5)
combo_saida.grid(row=1, column=1, padx=5, pady=5)
botao_escolher.grid(row=2, column=0, columnspan=2, pady=10)
label_imagem.grid(row=3, column=0, columnspan=2)
botao_converter.grid(row=4, column=0, columnspan=2, pady=10)

caminho_imagem = "" # Variável global para armazenar o caminho da imagem

janela.mainloop()