import sys
user_pointX = 0
user_pointY = 0

menu_elements = ['Up', 'Right', 'Left', 'Down']
print(f'We are at start point: X = {user_pointX}, Y = {user_pointY}')

menu_selector = input('Where are we going? (Left,Right,Down,Up): ')
if menu_selector not in menu_elements:
    print(f'We cant go "{menu_selector}". Only {menu_elements}.')
    sys.exit()

step = float(input("Enter the number of steps (float or int number): "))
if step < 0:
    print("Step cannot be negative")
    sys.exit()

if menu_selector == "Left":
    user_pointX -= step
elif menu_selector == "Right":
    user_pointX += step
elif menu_selector == "Up":
    user_pointY += step
elif menu_selector == "Down":
    user_pointY -= step

print(f'Current coordinates: X = {user_pointX}, Y = {user_pointY}')

