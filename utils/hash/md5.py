import hashlib

def getHash(email):
  return hashlib.md5(email.encode()).hexdigest()