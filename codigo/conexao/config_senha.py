from cryptography.fernet import Fernet

# Gere uma nova chave para criptografia
chave = Fernet.generate_key()

chave = "dN2mecmR9OpsZIVxIe7NjA0hWN9IVHwW3ezZVCTaPow="

# Crie um objeto Fernet com a chave
cipher_suite = Fernet(chave)


chave = "b'dN2mecmR9OpsZIVxIe7NjA0hWN9IVHwW3ezZVCTaPow='"
senha_original = "ameixa"

# Criptografe a senha
senha = senha_original.encode()  # Converta a senha em bytes
senha_criptografada = cipher_suite.encrypt(senha)

senha_criptografada = "gAAAAABkPf3CPL8Ju5W5SZYcZY7_U5FWU5qehMyxgK-Jg_aYd0NwlTB5IsvcoWz9jbSnlq21kdS7s0PjlIwz320MMdSWF_4R7g=="

# Descriptografe a senha
senha_descriptografada = cipher_suite.decrypt(senha_criptografada)

# Converta a senha descriptografada de bytes para string
senha_descriptografada_str = senha_descriptografada.decode()

print("Senha original:", senha)
print("Senha criptografada:", senha_criptografada)
print("Senha descriptografada:", senha_descriptografada_str)
print(senha)