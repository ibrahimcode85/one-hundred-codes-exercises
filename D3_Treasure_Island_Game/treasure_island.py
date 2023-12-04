# 1. Print welcome message.
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 ''')    
print("\n")
print('''
 ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, ,adPPYba,  
a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88 I8[    ""  
8b       88 ,adPPPPP88 88      88      88 8PP"""""""  `"Y8ba,   
"8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa aa    ]8I  
 `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' `"YbbdP"'  
 aa,    ,88                                                     
  "Y8bbdP"                                                      
''')
print("\n")
print("\n")

print("Welcome to Treasure Island.") 
print("Your mission is to find the treasure.")
print("\n")

# 2. First game choice
left_or_right = input('''You're at a cross road. Where do you want to go? Type: "left" or "right".''').lower()
print("\n")

if left_or_right == 'left':
    # 3. Second game choice
    swim_or_wait = input('You came to a large lake. What do you want to do? Type: "wait" or "swim".').lower()
    print("\n")

    if swim_or_wait == 'wait':
        #4. Third game choice
        which_door = input('Now there are three doors in front of you. Which one do you want to choose? Type: "red", "yellow", "blue".').lower()
        print("\n")

        if   which_door == 'yellow': 
            print("Congratulation! You found the treasure!!")

        elif which_door == 'red': 
            print("OMG there's a Giant sleeping behind the door!!")
            print("And you have just woke him up!")
            print("Game Over!")
            print("\n")
            
        elif which_door == 'blue':
            print("What luck - you have just started a big fire that could destroy the whole island!")
            print("Game Over")
            print("\n")

    else:
        print('You were chased by a group of Sharks!! You can never out-swim them.')
        print('Game Over!')
        print("\n")

else:
    print('You came across a group of Pirates!! They took you as a prisoner.')
    print('Game Over!')
    print("\n")


