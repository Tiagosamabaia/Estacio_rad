import tkinter as tk
from tkinter import ttk, messagebox

def adicionar_aluno():
    nome = aluno_nome_entry.get()
    idade = aluno_idade_entry.get()
    nota = aluno_nota_entry.get()
   
    if nome and idade and nota:
        alunos_listbox.insert(tk.END, f"{nome} - {idade} anos - Nota: {nota}")
        aluno_nome_entry.delete(0, tk.END)
        aluno_idade_entry.delete(0, tk.END)
        aluno_nota_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Preencha todos os campos do aluno")

def adicionar_professor():
    nome = prof_nome_entry.get()
    departamento = prof_departamento_entry.get()
   
    if nome and departamento:
        professores_listbox.insert(tk.END, f"{nome} - Departamento: {departamento}")
        prof_nome_entry.delete(0, tk.END)
        prof_departamento_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Preencha todos os campos do professor")

def adicionar_disciplina():
    nome = disc_nome_entry.get()
    codigo = disc_codigo_entry.get()
   
    if nome and codigo:
        disciplinas_listbox.insert(tk.END, f"{nome} - Código: {codigo}")
        disc_nome_entry.delete(0, tk.END)
        disc_codigo_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Preencha todos os campos da disciplina")

root = tk.Tk()
root.title("Cadastro Escolar")
root.geometry("400x400")

tab_control = ttk.Notebook(root)

# Aba de Alunos
tab_alunos = ttk.Frame(tab_control)
tab_control.add(tab_alunos, text='Alunos')

aluno_nome_label = tk.Label(tab_alunos, text="Nome:")
aluno_nome_entry = tk.Entry(tab_alunos)
aluno_idade_label = tk.Label(tab_alunos, text="Idade:")
aluno_idade_entry = tk.Entry(tab_alunos)
aluno_nota_label = tk.Label(tab_alunos, text="Nota Final:")
aluno_nota_entry = tk.Entry(tab_alunos)
alunos_listbox = tk.Listbox(tab_alunos)

adicionar_aluno_button = tk.Button(tab_alunos, text="Adicionar Aluno", command=adicionar_aluno)

# Organizando layout da aba Alunos
aluno_nome_label.pack()
aluno_nome_entry.pack()
aluno_idade_label.pack()
aluno_idade_entry.pack()
aluno_nota_label.pack()
aluno_nota_entry.pack()
adicionar_aluno_button.pack(pady=10)
alunos_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Aba de Professores
tab_professores = ttk.Frame(tab_control)
tab_control.add(tab_professores, text='Professores')

prof_nome_label = tk.Label(tab_professores, text="Nome:")
prof_nome_entry = tk.Entry(tab_professores)
prof_departamento_label = tk.Label(tab_professores, text="Departamento:")
prof_departamento_entry = tk.Entry(tab_professores)
professores_listbox = tk.Listbox(tab_professores)

adicionar_professor_button = tk.Button(tab_professores, text="Adicionar Professor", command=adicionar_professor)

# Organizando layout da aba Professores
prof_nome_label.pack()
prof_nome_entry.pack()
prof_departamento_label.pack()
prof_departamento_entry.pack()
adicionar_professor_button.pack(pady=10)
professores_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Aba de Disciplinas
tab_disciplinas = ttk.Frame(tab_control)
tab_control.add(tab_disciplinas, text='Disciplinas')

disc_nome_label = tk.Label(tab_disciplinas, text="Nome:")
disc_nome_entry = tk.Entry(tab_disciplinas)
disc_codigo_label = tk.Label(tab_disciplinas, text="Código:")
disc_codigo_entry = tk.Entry(tab_disciplinas)
disciplinas_listbox = tk.Listbox(tab_disciplinas)

adicionar_disciplina_button = tk.Button(tab_disciplinas, text="Adicionar Disciplina", command=adicionar_disciplina)

# Organizando layout da aba Disciplinas
disc_nome_label.pack()
disc_nome_entry.pack()
disc_codigo_label.pack()
disc_codigo_entry.pack()
adicionar_disciplina_button.pack(pady=10)
disciplinas_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Finalizando a configuração do Notebook
tab_control.pack(expand=1, fill='both')

root.mainloop()