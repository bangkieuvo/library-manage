def encrypt(cipher):
	import hashlib
	sha256 = hashlib.sha256()
	sha256.update(cipher.encode("utf-8"))
	return sha256.hexdigest()

