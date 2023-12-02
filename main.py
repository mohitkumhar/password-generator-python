import random

# print(string.punctuation)
punctuation = ['!','"', '#', '$', '%', '&', "'", '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ',']

alphabet_higher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

hard_password_list = punctuation + alphabet_lower + alphabet_higher + numbers

medium_password_list = alphabet_higher + alphabet_lower + numbers

simple_password_list = alphabet_lower

user = input("Which Type of Password Do You Want.? Hard, Medium, Simple, (h/m/s).?")

if user.lower() == 'h':
    password_list = random.sample(hard_password_list, 12)

elif user.lower() == 'm':
    password_list = random.sample(medium_password_list, 10)

elif user.lower() == 's':
    password_list = random.sample(simple_password_list, 10)

else:
    print("Invalid Input By User..!!")

password = ''

for i in password_list:
    password += i

print(f'The Generated Password is: {password}')
print(punctuation)