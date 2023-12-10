# 0. Import relevant module
import random

# 1. Get the required list of letters, numbers and symbols
# initialized lists
list_letters = []
list_numbers = []

# list of letters
for i in range(97, 123):
    list_letters.append(chr(i))

for i in range(97,123): # re-loop again for uppercase letters.
    list_letters.append(chr(i).upper())


# list of numbers
for i in range(0,10):
    list_numbers.append(i)

# list of symbols
    list_symbols = ['!', '#', '$', '%', "(", ")", '*', '+']

# 2. Print welcome statement
print("Welcome to the Py-Password Generator!")

# 3. Get relevant user input
n_letter  = int(input("How many letters would you like in your password:\n"))
n_numbers = int(input("How many numbers would you like in your password:\n"))
n_symbols = int(input("How many symbols would you like in your password:\n"))

# 4. Create a list of letter, number and symbol to select form

# 4.1 Get random letters
list_combined = []
for i in range(0, n_letter):
    random_i = random.randint(0, len(list_letters) - 1)
    list_combined.append(list_letters[random_i])


# 4.2 Get random numbers
for i in range(0, n_numbers):
    random_i = random.randint(0, len(list_numbers) - 1)
    list_combined.append(list_numbers[random_i])


# 4.3 Gen random symbols
for i in range(0, n_symbols):
    random_i = random.randint(0, len(list_symbols) - 1)
    list_combined.append(list_symbols[random_i])

# 5. Generate the password based on the letters,symbols and numbers selected
list_password = random.sample(list_combined, len(list_combined)) #randomly select from list without replacement

password_final=""
for i in list_password: password_final += str(i)

print(f"Here is your password: {password_final}")

