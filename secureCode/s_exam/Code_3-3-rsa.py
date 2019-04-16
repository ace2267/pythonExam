__author__ = 'samsjang@naver.com'

#from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
from Crypto.PublicKey import RSA


def createPEM():
	private_key = RSA.generate(1024)
	f = open('mykey.pem', 'wb+')	
	f.write(key.exportKey('PEM'))
	f.close()
	
def readPEM():
	h = open('mykey.pem', 'r')
	key = RSA.importKey(h.read())
	h.close()	
	return key

def rsa_enc(msg):
	private_key = readPEM()
	public_key = private_key.publickey()
	encdata = public_key.encrypt(msg, 32)
	return encdata
	
def rsa_dec(msg):
	private_key = readPEM()
	decdata = private_key.decrypt(msg)
	return decdata
	
	
if __name__ == '__main__':
	#createPEM()
	msg = 'samsjang loves python'
	ciphered = rsa_enc(msg.encode('utf-8'))
	print(ciphered)
	deciphered = rsa_dec(ciphered)
	print(deciphered)