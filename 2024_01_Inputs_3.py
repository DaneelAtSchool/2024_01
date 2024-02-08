#-*-coding:utf8;-*-
#qpy:console

print("Введите строку: ")
usrStr = input()

cmlStr = ""
idx = 0
for ch in usrStr:
    if (0 == idx % 2):
        cmlStr += ch.lower()
    else:
        cmlStr += ch.upper()
    idx+=1
print(cmlStr)
    
    





