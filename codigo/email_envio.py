from email import run
from conexao import dal
import os
import win32com.client
import datetime

# Criar uma instância do Outlook
outlook = win32com.client.Dispatch("Outlook.Application")

# Obter a caixa de entrada
inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)  # Código 6 representa a pasta de entrada do Outlook

# Especificar a data de início para a filtragem
data_inicio = datetime.datetime(2022, 1, 1)  # Substitua com a data de início desejada

# Obter os emails da pasta de entrada filtrados pela data de recebimento
emails = inbox.Items.Restrict("[ReceivedTime] >= '" + data_inicio.strftime('%m/%d/%Y %H:%M %p') + "'")

# Especificar o endereço de email do remetente desejado
remetente_desejado = "exemplo@dominio.com"  # Substitua com o endereço de email do remetente desejado

# Aplicar um filtro para obter apenas os emails do remetente específico
emails = inbox.Items.Restrict("[SenderEmailAddress] = '" + remetente_desejado + "'")

# Iterar pelos emails
if emails.Count > 0:
    print("Lista de emails a partir de", data_inicio.strftime('%m/%d/%Y'), ":")
    for email in emails:
        print("-" * 30)
        print("Assunto:", email.Subject)
        print("Remetente:", email.SenderName)
        print("Data:", email.ReceivedTime)

        # Iterar pelos anexos do email
        for anexo in email.Attachments:
            # Obter o nome do arquivo e a extensão
            nome_arquivo, extensao = os.path.splitext(anexo.FileName)

            # Salvar o anexo em um arquivo local
            caminho_arquivo = os.path.join("caminho/para/salvar", anexo.FileName)  # Substitua com o caminho desejado
            anexo.SaveAsFile(caminho_arquivo)
            print(f"Anexo salvo: {caminho_arquivo}")
else:
    print("Nenhum email encontrado.")