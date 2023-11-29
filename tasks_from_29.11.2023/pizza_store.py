katalog = {'pizza': 1000, 'apple': 100, 'camozin': 200, 'dota': 400, 'maksim': 10, 'moskva': 0, 'kamozins sausage': 2000}
basket = {}

def get_to_basket():
    while True:
        mas = []
        j = 0
        for i in katalog:
            mas.append(j)
            mas.append(i)
            j+=1
        while True:
            try:
                tovar = int(input(f'какой товар вы хотите положить в корзину?(из этого каталога, обращаться по индексу{mas})'))
                break
            except ValueError:
                print('нужно обратиться по индексу!!!')
        basket[mas[tovar*2+1]] = katalog.get(mas[tovar*2+1])
        print(f'{mas[tovar*2+1]} успешно добавлен в корзину')
        while True:
            try:
                change = int(input('добавить еще товары?(1 - да, 2 - нет): '))
                break
            except ValueError:
                print('введите цифру!!!')
        if change == 1:
            continue
        else:
            break


def my_decorator(print_paylist):
    def warapper():
        sum_basket = 0
        for i in basket:
            sum_basket += basket.get(i)
        while True:
            while True:
                try:
                    change = int(input('вы хотите оплатить онлайн(1 - да, 2 - нет): '))
                    break
                except ValueError:
                    print('введите цифру!!!')
            if change == 2:
                print_paylist(basket)
                while True:
                    try:
                        cash = int(input('сколько наличных вы даете?'))
                        break
                    except ValueError:
                        print('введите цифру!!!')
                if cash >= sum_basket:
                    cash_down = cash - sum_basket
                    print(f'корзина успешно оплачена на сумму {sum_basket}, ваша сдача {cash_down}')
                    break
                else:
                    print('недостаточно наличных средств')
                    while True:
                        try:
                            change1 = int(input('оплатить еще раз или выйти(1 - еще раз, 2 - выйти): '))
                            break
                        except ValueError:
                            print('введите цифру')
                    if change1 == 1:
                        continue
                    else:
                        break
            else:
                print_paylist(basket)
                print(f'корзина успешно оплачена на сумму {sum_basket}')
                break
    return warapper()

while True:
    print(f'каталог товаров: {katalog}')
    while True:
        try:
            change = int(input('выберете действие(1 - положить товар в корзину, 2 - оплатить корзину, 3 - показать что у меня в корзине, 4 - выйти из магазина):'))
            break
        except ValueError:
            print('введите цифру!!!')
    if change == 1:
        get_to_basket()

    elif change == 2:
        @my_decorator
        def print_paylist(basket):
            cheklist = []
            count_tovar = 1
            sum = 0
            for i in basket:
                cheklist.append(list(f'товар №{count_tovar} - {i}, цена: {basket[i]}'))
                count_tovar += 1

            for i in range(len(cheklist)):
                for j in range(len(cheklist[i])):
                    print(cheklist[i][j], end = ' ')
                print()
    elif change == 3:
        print('ваша корзина', basket)

    else:
        break
print('до свидания')

