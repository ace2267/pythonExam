import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

x = 10
if x < 10:
    print('한자리수')
elif x < 100:
    print("두자리수")
else:
    print("세자리이상")

if x < 10:
    pass
else:
    print(x)