import win32com.client
import datetime


outlook = win32com.client.Dispatch("Outlook.Application")
# Filtrar por endereço de email do campo Bcc:

inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
bcc_filtrado = inbox.Items.Restrict("[BCC] = 'exemplo@dominio.com'")


# Filtrar por palavras-chave no corpo do email:
inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
corpo_filtrado = inbox.Items.Restrict("[Body] LIKE '%palavra_chave%'")

# Filtrar por endereço de email do campo Cc:

inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
cc_filtrado = inbox.Items.Restrict("[CC] = 'exemplo@dominio.com'")

# Filtrar por data e hora de criação do email:

inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
data_filtrada = inbox.Items.Restrict("[CreationTime] >= '" + datetime.datetime(2023, 1, 1).strftime('%m/%d/%Y %H:%M %p') + "'")

# Filtrar por palavras-chave no corpo do email em formato HTML:

inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
html_body_filtrado = inbox.Items.Restrict("[HTMLBody] LIKE '%palavra_chave%'")

# Filtrar por importância do email (baixa, normal ou alta):

inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
importancia_filtrada = inbox.Items.Restrict("[Importance] = 2")  # 2 representa a importância normal

# Filtrar por data e hora de recebimento do email:

inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
data_recebimento_filtrada = inbox.Items.Restrict("[ReceivedTime] >= '" + datetime.datetime(2023, 1, 1).strftime('%m/%d/%Y %H:%M %p') + "'")

# Filtrar por endereço de email do remetente:

nbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
remetente_filtrado = inbox.Items.Restrict("[SenderEmailAddress] = 'exemplo@dominio.com'")
