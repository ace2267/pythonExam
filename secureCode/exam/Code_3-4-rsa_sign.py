from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA

def readPEM():
	h = open('mykey.pem', 'r')
	key = RSA.importKey(h.read())
	h.close()	
	return key

def rsa_sign(msg):
	private_key = readPEM()
	public_key = private_key.publickey()	
	hash = SHA.new(msg).digest()	
	signature = private_key.sign(hash, '')
	return public_key, signature

def rsa_verify(msg, public_key, signature):	
	hash = SHA.new(msg).digest()	
	if public_key.verify(hash, signature):
		print ('VERIFIED')
	else:
		print ('DENIED')

if __name__ == '__main__':
	msg = 'My name is samsjang'
	public_key, signature = rsa_sign(msg.encode('utf-8'))
	rsa_verify(msg.encode('utf-8'), public_key, signature)