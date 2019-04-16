import ccrypt

def findPass(passhash, dictfile):	
	salt = passhash[3:5]
	with open(dictfile, 'r') as dfile:	
		for word in dfile.readlines():
			word = word.strip('\n')
			cryptwd = ccrypt.crypt(word, salt)
			if cryptwd == passhash[3:]:
				return word
	return ''
	
def main():	
	dictfile = 'dictionary.txt'
	with open('passwords.txt', 'r') as passFile:
		for line in passFile.readlines():
			data = line.split(':')
			user = data[0].strip()
			passwd = data[1].strip()
			word = findPass(passwd, dictfile)
			if word:
				print('FOUND Password: ID [%s] Password [%s]' %(user, word))
			else:
				print('Password Not Found!')
		
if __name__ == '__main__':
	main()