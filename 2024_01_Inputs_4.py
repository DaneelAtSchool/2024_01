#-*-coding:utf8;-*-
#qpy:console



while True:
    print("введите символ или код символа: ")
    symb = input()

    if symb.isdigit():
        print(chr(int(symb)))
        
    if not (len(symb) == 1):
        print("Должен быть только один символ")
        continue

    print("код символа: ")
    print(ord (symb))
        
    break;
    
    


