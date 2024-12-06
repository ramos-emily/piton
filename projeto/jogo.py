import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Lista de perguntas
questions = [
    ["Qual é a capital da França?", "Paris", "Londres", "Berlim", "Roma", 1],
    ["Qual é o resultado de 8 + 5?", "12", "13", "15", "18", 2],
    ["Quem pintou a Mona Lisa?", "Picasso", "Da Vinci", "Van Gogh", "Warhol", 2],
    ["Quanto é 6 multiplicado por 7?", "36", "42", "48", "54", 2],
    ["Qual é o maior planeta do sistema solar?", "Marte", "Saturno", "Júpiter", "Vênus", 3],
    ["Quem escreveu a obra 'Dom Quixote'?", "Machado de Assis", "Miguel de Cervantes", "Jorge Luis Borges", "Gabriel García Márquez", 2],
    ["Qual é a fórmula química da água?", "H2O", "CO2", "NaCl", "CH4", 1],
    ["Quem foi o primeiro presidente dos Estados Unidos?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John F. Kennedy", 1],
    ["Qual é o resultado de 4 ao cubo?", "16", "32", "64", "128", 3],
    ["Qual é a capital da Rússia?", "Moscou", "São Petersburgo", "Kiev", "Varsóvia", 1],
    ["Quem descobriu a teoria da relatividade?", "Isaac Newton", "Galileu Galilei", "Albert Einstein", "Nikola Tesla", 3],
    ["Qual é o símbolo químico do ouro?", "Au", "Ag", "Cu", "Fe", 1],
    ["Quem foi o autor da obra 'Romeu e Julieta'?", "William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen", 1],
    ["Qual é a capital do Brasil?", "Rio de Janeiro", "Brasília", "São Paulo", "Salvador", 2],
    ["Qual é o resultado de 9 dividido por 3?", "1", "2", "3", "4", 3],
    ["Quem pintou a obra 'A Noite Estrelada'?", "Leonardo da Vinci", "Michelangelo", "Salvador Dalí", "Vincent van Gogh", 4],
    ["Qual é o maior oceano do mundo?", "Atlântico", "Índico", "Pacífico", "Ártico", 3],
    ["Qual é o resultado de 2 elevado a 8?", "8", "16", "64", "256", 4],
    ["Quem escreveu a obra '1984'?", "George Orwell", "Aldous Huxley", "Ernest Hemingway", "F. Scott Fitzgerald", 1],
    ["Qual é o resultado de 15 menos 7?", "5", "6", "7", "8", 3],
    ["Quem foi o pintor do quadro 'A Última Ceia'?", "Pablo Picasso", "Salvador Dalí", "Michelangelo", "Leonardo da Vinci", 4]
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
current_question = 0
score = 0

# Função para verificar a resposta
def check_answer(answer):
    global score, current_question

    if answer == correct_answer.get():
        score += 1
        print("acertou!!!")

    current_question += 1

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