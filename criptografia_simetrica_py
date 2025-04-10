from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def b64(data):
    return base64.b64encode(data).decode()

chave = get_random_bytes(16)
aes = AES.new(chave, AES.MODE_EAX)
nonce = aes.nonce

mensagem = b'Dados sigilosos aqui!'
cifrada, tag = aes.encrypt_and_digest(mensagem)

aes_decifra = AES.new(chave, AES.MODE_EAX, nonce=nonce)
mensagem_original = aes_decifra.decrypt(cifrada)

print("Mensagem cifrada (Base64):", b64(cifrada))
print("Mensagem original:", mensagem_original.decode())
