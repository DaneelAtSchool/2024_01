#-*-coding:utf8;-*-
#qpy:console

while True:
    print("введите символ: ")
    symb = input()

    if not (len(symb) == 1):
        print("Должен быть только один символ")
        continue

    symcode = ord(symb)
    if (symb == 'a') or (symb == 'A'):
        print("Первый символ алфавита.")
    else:
        print("предыдущий символ: ")
        print(chr(symcode-1))

    if (symb == 'z') or (symb == 'Z'):
        print("Последний символ алфавита.")
    else:
        print("следующий символ: ")
        print(chr(symcode+1))

    break;
    
    
