from cryptography.fernet import Fernet

# Gere uma nova chave para criptografia
chave = Fernet.generate_key()

# Crie um objeto Fernet com a chave
cipher_suite = Fernet(chave)

# Criptografe a senha
senha = 'alecrim'.encode()  # Converta a senha em bytes
senha_criptografada = cipher_suite.encrypt(senha)

# Descriptografe a senha
senha_descriptografada = cipher_suite.decrypt(senha_criptografada)

# Converta a senha descriptografada de bytes para string
senha_descriptografada_str = senha_descriptografada.decode()

print("Senha original:", senha)
print("Senha criptografada:", senha_criptografada)
print("Senha descriptografada:", senha_descriptografada_str)