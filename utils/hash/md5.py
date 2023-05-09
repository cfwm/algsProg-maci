import hashlib

def getHash(email: str) -> str:
  return hashlib.md5(email.encode()).hexdigest()