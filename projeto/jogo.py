import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random
import os

# Ajusta o diretório para o local do script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Verifica o diretório de trabalho atual
print("Diretório atual:", os.getcwd())

# Lista os arquivos disponíveis para depuração
print("Arquivos disponíveis:", os.listdir())

# Lista de perguntas
questions = [
    ["Qual é o comando para exibir algo no console em Python?", "console.log()", "echo", "print()", "System.out.println()", 3],
    ["Como você cria uma lista em Python?", "list = ()", "list = {}", "list = ||", "list = []", 4],
    ["Qual é o operador de atribuição em Python?", "==", "=", "===", ":=", 2],
    ["Como você declara uma função em Python?", "func myFunc():", "function myFunc():", "def myFunc():", "fn myFunc():", 3],
    ["Como você inicia um loop `for` em Python?", "for i to n:", "foreach i in range():", "for i in range():", "for (i=0; i<n; i++):", 3],
    ["Qual é a função usada para obter o comprimento de uma lista?", "count()", "size()", "length()", "len()", 4],
    ["Qual é o tipo de dado para números decimais em Python?", "float", "int", "decimal", "double", 1],
    ["Como você cria uma string em Python?", "string(texto)", "{texto}", "'texto'", "[texto]", 3],
    ["Qual é a palavra-chave para criar uma classe em Python?", "Class", "object", "define", "class", 4],
    ["Como você importa um módulo em Python?", "import module", "use module", "require module", "include module", 1],
    ["Qual função é usada para ler a entrada do usuário no console?", "read()", "input()", "get()", "scanf()", 2],
    ["Qual é o valor de `5 // 2` em Python?", "2.5", "3", "3.5", "2", 4],
    ["Como você define uma variável global dentro de uma função?", "let var", "var global", "global var", "global: var", 3],
    ["Qual é a estrutura correta para um bloco `try` em Python?", "try: except:", "try {} catch {}", "try {} except {}", "try: catch:", 1],
    ["Qual é o método usado para adicionar um elemento em uma lista?", "append()", "insert()", "add()", "push()", 1],
    ["Qual biblioteca padrão é usada para trabalhar com datas em Python?", "calendar", "date", "time", "datetime", 4],
    ["Como você converte uma string para um número inteiro em Python?", "float()", "int()", "str()", "toInt()", 2],
    ["Como você remove um elemento de uma lista em Python?", "pop()", "del", "remove()", "delete()", 3],
    ["Qual é o resultado de `2 ** 3` em Python?", "6", "12", "8", "9", 3],
    ["Qual é a palavra-chave usada para encerrar um loop?", "stop", "exit", "end", "break", 4]
]

# Criar DataFrame do pandas
df = pd.DataFrame(questions, columns=["Pergunta", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

# Salvar no arquivo do Excel
df.to_excel("questions.xlsx", index=False)
print("Perguntas inseridas com sucesso no arquivo questions.xlsx!")

df = pd.read_excel('questions.xlsx')
questions = df.sample(n=10).values.tolist()

window = tk.Tk()
window.title("Quiz")
window.geometry("400x450")

# Carrega as imagens após a criação da janela
try:
    acerto_img = tk.PhotoImage(file="acerto_img.png")
    erro_img = tk.PhotoImage(file="erro_img.png")
    print("Imagens carregadas com sucesso.")
except Exception as e:
    print("Erro ao carregar imagens:", e)
    exit()

current_question = 0
score = 0

feedback_label = tk.Label(window)
feedback_label.pack(pady=20)

# Função para verificar a resposta
def check_answer(answer):
    global score, current_question

    if answer == correct_answer.get():
        score += 1
        feedback_label.config(image=acerto_img)
    else:
        feedback_label.config(image=erro_img)

    # Aguarda 1 segundo antes de passar para a próxima pergunta
    window.after(1000, next_question)

def next_question():
    global current_question

    current_question += 1

    # Limpa o feedback visual
    feedback_label.config(image="")

    if current_question < len(questions):
        display_question()
    else:
        show_result()

# Função para exibir a próxima pergunta
def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))
    correct_answer.set(answer)

# Função para exibir o resultado final
def show_result():
    messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você completou o quiz.\n\nPontuação final: {score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()

# Função para jogar novamente
def play_again():
    global score, current_question
    score = 0
    current_question = 0
    random.shuffle(questions)
    display_question()
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()

background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"
window.option_add('*Font', 'Arial')

question_label = tk.Label(window, text="", wraplength=380, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(window, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(window, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(window, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(window, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(window, text="Jogar Novamente", width=30, bg=button_color, fg=button_text_color, command=play_again, font=("Arial", 10, "bold"))

display_question()
window.mainloop()
