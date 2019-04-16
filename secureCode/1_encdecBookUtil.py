def makeCodebook():
   decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m','*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}
   encbook = {}
   
   for x in decbook : 
     encbook[decbook[x]] = x

   return decbook, encbook

# decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m','*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}
def decode(inp, dec):
  
   for x in inp :
    # print(x)
    if x in dec :
      inp = inp.replace(x, dec[x])
      # print(inp)
   return inp

def encode(inp, enc):
   for x in inp :
    # print(x)
    if x in enc :
      inp = inp.replace(x, enc[x])
      # print(inp)
   return inp

# def encode(input):
#     output = input
#     return output
# inp = "2222222222"
# for x in inp :
# print(if x in decbook)

if __name__ == "__main__":
   plaintext ="this is my life hello hello world" 
   dec, enc =makeCodebook()
   enctext = encode(plaintext, enc)
   print(enctext)
   dectext = decode(enctext, dec)
   print(dectext)
