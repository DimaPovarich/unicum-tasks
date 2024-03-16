class Crm:
    def __init__(self):
        self.data_users = {}
    def add_user(self):
        self.new_user = str(input("введите свое имя: "))
        self.user_phone_number = str(input("введите свой номер телефона: "))
        self.data_users[self.new_user] = self.user_phone_number
        print(f"Пользователь {self.new_user} успешно зарегестрирован!")
    def delete_user(self):
        self.del_user = str(input("введите имя пользователя которого нужно удалить: "))
        while True:
            try:
                self.del_user = str(input("введите имя пользователя которого нужно удалить: "))
                del self.data_users[self.del_user]
                print(f"Пользователь {self.del_user} успешно удален!")
                break
            except:
                print("Нет такого пользователя!")
                continue

    def change_user(self):
        self.changer_user = str(input("Номер какого пользователя нужно изменить? "))
        self.data_users[self.changer_user] = input("Какой его номер телефона? ")
    def show_data_base(self):
        print(self.data_users)

system = Crm()
while True:
    ch = int(input("что вы хотите сделать? (1 - добавить пользователя, 2 - удалить пользователя, 3 - изменить данные пользоваетля, 4 - увидеть базу пользователей): "))
    if ch == 1:
        system.add_user()
    elif ch == 2:
        system.delete_user()
    elif ch == 3:
        system.change_user()
    elif ch == 4:
        system.show_data_base()
    change_end = int(input("Завершить выполнение?(1 - да , 2 - нет): "))
    if change_end == 1:
        break
    else:
        continue
print("АХАГАК ПЫЯЛА САН КУРОСАН КУРУСАН КУЛ ДА КУ КУЛ ДА КУ")


