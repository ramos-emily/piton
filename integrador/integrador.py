import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
 
# lendo o arquivo csv
df = pd.read_csv('Esp8266_Receiver.csv')
 
# Função para classificar o número de produtos
def classificar(produtos):
    if produtos == 1:
        return "CRÍTICO"
    elif produtos == 2:
        return "MÉDIO"
    elif produtos == 3:
        return "ESTOQUE CHEIO"
    else:
        return "QUEBRADO!!"

# Exibe os status das esteiras
df["Esteira1_Status"] = df["esteira1"].apply(classificar)
df["Esteira2_Status"] = df["esteira2"].apply(classificar)
df["Esteira3_Status"] = df["esteira3"].apply(classificar)
 
# Definindo o caminho do arquivo TXT
arquivo_txt = 'Informações_Esteiras.txt'
df.to_string(buf=open(arquivo_txt, 'w'), index=False)
print(f"Os dados dos produtos foram criados com sucesso: '{arquivo_txt}'")

# Verifica se o arquivo foi criado
if not os.path.exists(arquivo_txt):
    print(f"Erro: O arquivo {arquivo_txt} não foi encontrado!")
    exit()  # Encerra o script se o arquivo não for encontrado
 
# Configuração do servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'  # Servidor SMTP (exemplo: Gmail)
SMTP_PORT = 587                 # Porta para TLS de segurança
EMAIL_USUARIO = 'dadau22k47@gmail.com'  # meu e-mail
EMAIL_SENHA = 'j c b q a u c g z l g s c r v j'       # Minha senha (ou senha de aplicativo)
 
# Configuração do e-mail
destinatario = 'dadau22k47@gmail.com'
assunto = 'Relatório de Informações das Esteiras'
mensagem = 'Segue em anexo o relatório atualizado das esteiras.'
 
# Criação do e-mail
email = MIMEMultipart()
email['From'] = EMAIL_USUARIO
email['To'] = destinatario
email['Subject'] = assunto
 
# Corpo do e-mail
email.attach(MIMEText(mensagem, 'plain'))
 
# Anexando o arquivo
with open(arquivo_txt, 'rb') as file: #Abre o arquivo especificado em arquivo_txt para leitura binária
    parte_anexo = MIMEBase('application', 'octet-stream') #Cria um objeto MIMEBase, que é usado para anexar arquivos binários no e-mail
    parte_anexo.set_payload(file.read())
    encoders.encode_base64(parte_anexo) #Codifica os dados binários pq a bibilhoteca nao lida bem com bonarios puros
    parte_anexo.add_header('Content-Disposition', f'attachment; filename="{arquivo_txt}"')
    email.attach(parte_anexo) #anexa o email
 
# Enviando o e-mail
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
        servidor.starttls()  
        servidor.login(EMAIL_USUARIO, EMAIL_SENHA)
        servidor.send_message(email)
        print(f"funcionoooooou, Deus é bom e o diabo é ruim {destinatario}!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
 