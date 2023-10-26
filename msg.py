import tkinter as tk

def copiar_para_area_de_transferencia():
    nome = entry_nome.get()
    ramal = entry_ramal.get()
    setor = entry_setor.get()
    mensagem = entry_mensagem.get("1.0", tk.END).strip()
    possui_os = var_os.get()
    numero_os = entry_numero_os.get() if possui_os else ""

    # Estrutura da mensagem
    mensagem_formatada = f"NOME: {nome}\nRAMAL: {ramal}\nSETOR: {setor}\nMENSAGEM: {mensagem}\nPOSSUI OS? {'SIM' if possui_os else 'NÃO'}\nNUMERO DA OS: {numero_os}"

    # Copiar mensagem para a área de transferência
    root.clipboard_clear()
    root.clipboard_append(mensagem_formatada)
    root.update()
    label_copiado.config(text="Dados copiados para a área de transferência!")

# Criar a janela principal
root = tk.Tk()
root.title("Formulário")

# Criar os campos do formulário
label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_ramal = tk.Label(root, text="Ramal:")
label_ramal.pack()
entry_ramal = tk.Entry(root)
entry_ramal.pack()

label_setor = tk.Label(root, text="Setor:")
label_setor.pack()
entry_setor = tk.Entry(root)
entry_setor.pack()

label_mensagem = tk.Label(root, text="Mensagem:")
label_mensagem.pack()
entry_mensagem = tk.Text(root, height=5, width=40)
entry_mensagem.pack()

var_os = tk.IntVar()
check_os = tk.Checkbutton(root, text="Possui OS?", variable=var_os, command=lambda: entry_numero_os.config(state=tk.NORMAL) if var_os.get() else entry_numero_os.config(state=tk.DISABLED))
check_os.pack()

entry_numero_os = tk.Entry(root, state=tk.DISABLED)
entry_numero_os.pack()

# Botão para copiar dados para a área de transferência
btn_copiar = tk.Button(root, text="Copiar para Área de Transferência", command=copiar_para_area_de_transferencia)
btn_copiar.pack()

# Label para exibir a mensagem de confirmação
label_copiado = tk.Label(root, text="")
label_copiado.pack()

# Iniciar o loop principal da aplicação
root.mainloop()
