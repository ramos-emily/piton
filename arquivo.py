# txt (bloco de notas)
with open ("my_arquivo.txt", "w") as arquivo:   # W serve para escrever
    arquivo.write("VouTirar10\n")
    arquivo.write("oiMarciaTenhaPiedadeDessaPobreAlma")

with open("my_arquivo.txt", "r") as arquivo:  # R serve para ler
    print(arquivo.read())



# CSV  (separa as informações por virgula, nao em formato de tabela)

# import csv

# with open ("batatinha.csv", "w", newline='') as csvfile:  #nweline pula linha   

#     seila = csv.writer(csvfile)
#     seila.writerow(['Nome', 'preco'])
#     seila.writerow(['livro', '20'])

# arquivo = open('batatinha.csv')

# linhas = csv.reader(arquivo)

# for linha in linhas:
#     print(linha)



# JSON (estrutura de arquivo, não é dicionário)





# XML (mais verboso, usado em receita federal, antiga)





# XLSX (Excel)