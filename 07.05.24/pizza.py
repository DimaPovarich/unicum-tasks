katalog = {'pizza': 1000, 'apple': 100, 'camozin': 200, 'dota': 400, 'maksim': 10, 'moskva': 0, 'kamozins sausage': 2000}
basket = {}

class User:
    def __init__(self, name):
        self.name = name

class Basket:
    def add_to_basket(self, item):
        if item in katalog:
            basket[item] = katalog[item]
            print(f'{item} успешно добавлен в корзину')
        else:
            print(f'Товара {item} нет в каталоге')

    def pay_basket(self, user):
        sum_basket = sum(basket.values())
        while True:
            payment_method = int(input(f'{user.name}, выберите способ оплаты (1 - онлайн, 2 - наличными): '))
            if payment_method == 1:
                print(f'Корзина пользователя {user.name} успешно оплачена онлайн на сумму {sum_basket}')
                break
            elif payment_method == 2:
                cash = int(input('Введите сумму наличными: '))
                if cash >= sum_basket:
                    change = cash - sum_basket
                    print(f'Корзина пользователя {user.name} успешно оплачена наличными на сумму {sum_basket}. Ваша сдача: {change}')
                    break
                else:
                    print('Недостаточно наличных средств')
            else:
                print('Неверный способ оплаты')

def main():
    user = User('Tom')
    basket = Basket()

    while True:
        print(f'Каталог товаров: {katalog}')
        action = int(input('Выберите действие (1 - положить товар в корзину, 2 - оплатить корзину, 3 - показать корзину, 4 - выйти): '))

        if action == 1:
            item = input('Введите название товара: ')
            basket.add_to_basket(item)
        elif action == 2:
            basket.pay_basket(user)
        elif action == 3:
            print('Ваша корзина:', basket)
        elif action == 4:
            print('До свидания!')
            break
        else:
            print('Неверный выбор')

if __name__ == '__main__':
    main()
