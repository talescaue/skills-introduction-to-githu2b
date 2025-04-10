from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

chaves = RSA.generate(2048)
chave_publica = chaves.publickey()

mensagem = b'Segredo importante!'
cifra_rsa = PKCS1_OAEP.new(chave_publica)
criptografada = cifra_rsa.encrypt(mensagem)

decifra_rsa = PKCS1_OAEP.new(chaves)
mensagem_decifrada = decifra_rsa.decrypt(criptografada)

print("Mensagem RSA criptografada (Base64):", base64.b64encode(criptografada).decode())
print("Mensagem decifrada:", mensagem_decifrada.decode())
