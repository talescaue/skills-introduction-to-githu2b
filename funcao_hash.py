import hashlib

def gerar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

mensagem = "Integridade dos dados!"
hash_gerado = gerar_hash(mensagem)

print("Mensagem original:", mensagem)
print("Hash SHA-256:", hash_gerado)
