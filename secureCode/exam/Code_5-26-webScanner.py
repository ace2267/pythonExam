from urllib.request import urlopen, Request, URLError, quote
from queue import Queue
from threading import Thread

user_agent = 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko' # User-Agent for IE 11

def webScanner(q, targethost, exts):
	while not q.empty():
		scanlist = []		
		toscan = q.get()		
		
		if '.' in toscan: # FILE
			scanlist.append('%s' %toscan)
			for ext in exts:
				scanlist.append('%s%s' %(toscan, ext))
		else: # DIR
			scanlist.append('%s/' %toscan)	
			
		for toscan in scanlist:
			url = '%s/%s' %(targethost, quote(toscan))		
			try:
				req = Request(url)
				req.add_header('User-Agent', user_agent)
				res = urlopen(req)
				if len(res.read()):
					print ('[%d]: %s' %(res.code, url))
				res.close()
			except URLError as e:
				pass
				
def main():
	targethost = 'http://172.21.70.227'
	wordlist = './all.txt'	
	exts = ['~', '~1', '.back', '.bak', '.old', '.orig', '_backup']
	
	q = Queue()
	with open(wordlist, 'rt') as f:
		words = f.readlines()
	
	for word in words:
		word = word.rstrip()					
		q.put(word)
	
	print('+++[%s] SCANNING START..' %targethost)
	
	for i in range(50):
		t = Thread(target=webScanner, args=(q, targethost, exts))
		t.start()
		
if __name__ == '__main__':	
	main()