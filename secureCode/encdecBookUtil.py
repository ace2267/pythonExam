# def makeCookbook(input):
# 	decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m','*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}
#     output = input
#     return output
decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m','*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}
def decode1(inp):
   decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m','*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}
   encbook = {}
   for x in inp :
    print(x)
    if x in decbook :
      inp = inp.replace(x, decbook[x])

    return inp

# def encode(input):
#     output = input
#     return output
# inp = "2222222222"
# for x in inp :
# print(if x in decbook)

print(decode1("22555555582222222"))
