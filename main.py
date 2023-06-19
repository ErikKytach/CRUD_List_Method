array = [132, 23131, 44, 10]
def Add_number():
    new_number = int(input('\nНапишіть число яке хочете додати: '))
    for i in range(len(array)):
        if array[i] == new_number:
            print(f'\nВибачте, але число {new_number} вже є у списку! Спробуйте ще, але інше число.')
        else:    
            array.append(new_number)

def Update():
    x=0
    zamina=0
    check_number = int(input("\nВведіть число, яке хочете змінити: "))
    for i in range(len(array)):
        if check_number == array[i]:
            x+=1
            zamina+=i
    if x>0:
        new_number = int(input('\nДобре, тепер напишіть нове число, на яке Ви хочете замінити старе: '))
        array[zamina] = new_number
        print('\nУспішно! Старе число змінено на нове.')
    else:
        print('\nВибачте, але такого числа в списку немає! Перевірте себе.')

def Delete_number():
    x=0
    check_number = int(input("\nВведіть число, яке хочете видалити: "))
    for i in range(len(array)):
        if check_number == array[i]:
            x+=1
    if x > 0:
        array.remove(check_number)
        print(f'\nУспішно! Ви видалили число {check_number} із списку.')
    else:
        print('\nВибачте, але такого числа в списку немає! Спробуйте ще раз.')
def Read_numbers():
    for i in range(len(array)):
        print(f"\n{array[i]}")
def Working_numbers():
    while True:
        work = int(input("\nДодати число - 1\nРедагувати число - *2*\nВидалити число - *3*\nВивести список - *4\nЗавершити програму - *5*\nВводити тут -> "))
        if work == 1:
            Add_number()
        elif work == 2:
            Update()
        elif work == 3:
            Delete_number()
        elif work == 4:
            Read_numbers()
        elif work == 5:
            break
        else:
            print('Такої операції немає!')
Working_numbers()
