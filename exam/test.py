# data 분해
# e,f = c[0]
# print(e)
# print(f)

print(ord('A'))
print(chr(90 +3))
for x in range(26) :
    print(chr(ord('A') + x))
inpStr = "ABDFEGGCCVBCC"
print(inpStr)
key = 5
for x in inpStr :
   inpStr = inpStr.replace(x, chr(ord(x) + key))

print(inpStr)