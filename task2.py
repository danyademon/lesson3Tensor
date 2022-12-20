user_pointX = 0
user_pointY = 0
menu_elements = list(range(5))

while True:
    print('Where are we going?')
    print(f'0.Exit\n1.Up\n2.Down\n3.Left\n4.Right')
    menu_selector = int(input('Type int number:'))

    if (menu_selector 
            not in menu_elements):
        #Если нет такого элемента в меню, то выходим из программы
        print(f'We cant go "{menu_selector}". Only {menu_elements}. Try again.\n')
        continue

    if menu_selector == 0:
        print('Good luck!')
        break

    step = float(input("Enter the number of steps: "))
    if step < 0:
        print("Step cannot be negative. Try again.")
        continue

    if menu_selector == 1:
        user_pointY += step  
    elif menu_selector == 2:
        user_pointY -= step
    elif menu_selector == 3:
        user_pointX -= step
    elif menu_selector == 4:
        user_pointX += step
    print(f'Current coordinates: X = {user_pointX}, Y = {user_pointY}\n') 