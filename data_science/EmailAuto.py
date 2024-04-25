import win32com.client as win32
import schedule
import time

def agendar_envio():
    outlook = win32.Dispatch('outlook.application')

    # Cria o email
    email = outlook.CreateItem(0)

    # Define o email
    email.To = 'vitornickolas10@gmail.com'
    email.CC = ''  # Adiciona destinatário em cópia
    email.BCC = ''  # Adiciona destinatário em cópia oculta
    email.Subject = 'assunto'
    email.HTMLBody = '''
    Teste
    '''

    # ENVIAR ANEXOS
    # anexo = "C:\Users\vitor\Downloads\INTERVIEW - DASHBOARD - SINALIZAÇÕES 24.xlsx"
    # email.Attachments.Add(anexo)

    # Envia o email
    email.Send()

    print('Email enviado!')

# Define o horário de envio para todos os dias úteis (segunda a sexta) às 12h
def agendar_tarefas():
    schedule.every().monday.at("12:00").do(agendar_envio)
    schedule.every().tuesday.at("12:00").do(agendar_envio)
    schedule.every().wednesday.at("19:58").do(agendar_envio)
    schedule.every().wednesday.at("20:00").do(agendar_envio)
    schedule.every().wednesday.at("20:03").do(agendar_envio)

# Inicializa o agendamento
agendar_tarefas()

# Loop para verificar e executar tarefas agendadas
while True:
    schedule.run_pending()
    time.sleep(60)  # Aguarda 60 segundos antes de verificar novamente
    