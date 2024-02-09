#-*-coding:utf8;-*-
#qpy:console


print("Нужно ввести: ФИО, Город, Улицу, Номер дома, Номер квартиры, Номер телефона.")


print("Введите ФИО: ")
while True:
    FIO = input()
    if FIO != FIO.title():
        print("все слова должны начинаться с большой буквы!")    
        continue
        
    if not (len(FIO.split(" ")) == 3):
        print("Должно быть 3 компонента ФИО!")
        continue
        
    print("\n")
    break;
        
            
print("Введите город: ")
while True:
    Town = input()
    if Town != Town.title():
        print("все слова должны начинаться с большой буквы!")    
        continue
        
    if not Town.isalpha():
        print("введите только буквы")
        continue

    print("\n")
    break;     

        
        
print("Введите номер квартиры: ")
while True:
    Fnumber = input()
    if not Fnumber.isdigit():
        print("введите только цифры")
        continue
        
    print("\n")
    break;

print("Введите номер телефона: ")
while True:
    Phonenumber = input()
    if not Phonenumber.isdigit():
        print("введите только цифры")
        continue
        
    print("\n")
    break;

print("Введите улицу: ")
while True:
    Street = input()
    if not Street.isalnum():
        print("введите только цифры и буквы")
        continue
        
    print("\n")
    break;

print("Введите номер дома: ")
while True:
    Hnumber = input()
    if not Hnumber.isalnum():
        print("введите только цифры и буквы")
        continue
        
    print("\n")
    break;
