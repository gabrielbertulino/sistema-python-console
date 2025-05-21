import bcrypt

def criptografar_senha(senha: str) -> bytes:
    # bcrypt gera um salt e aplica o hash
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

def verificar_senha(senha: str, hash_senha: bytes) -> bool:
    return bcrypt.checkpw(senha.encode(), hash_senha)
