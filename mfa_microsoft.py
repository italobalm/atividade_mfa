import pyotp
import qrcode
import time

secret = pyotp.random_base32()
print("Chave secreta do usuário", secret)

usuario = "aluno@teste.com"

emissor = "PraticaMFA-Microsoft"

uri = pyotp.totp.TOTP(secret).provisioning_uri(name=usuario, issuer_name=emissor)

qrcode.make(uri).save("qrcode_microsoft.png")

print(" QR Code gerado com sucesso! Escaneie 'qrcode_microsoft.png' no Microsoft Authenticator.")

senha_correta = "senha123"

senha = input(" Digite sua senha: ")


if senha == senha_correta:

    codigo = input(" Digite o código do Microsoft Authenticator: ")

    totp = pyotp.TOTP(secret)

    if totp.verify(codigo):

        print(" Acesso permitido! MFA com Microsoft Authenticator bem-sucedido.")

    else:

        print(" Código incorreto. Acesso negado.")
else:
    print(" Senha incorreta. Tente novamente.")
