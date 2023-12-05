from controller import check_str

def main():
    while True:
        name = str(input('what is your name? '))
        if check_str(name):
            break
        else:
            print('введите строку!')
            continue
    check_str(name)
    age = int(input('How old are you? '))
    position = str(input('what is your position? '))
    earn = int(input('what is your salary? '))
    user_info = [name, age, position, earn]
    return user_info


def write(info):
    with open('users.txt', 'w') as file:
        for i in info:
            file.write(f'{i}  ')


def view():
    with open('users.txt', 'r') as file:
        print(file.read())


