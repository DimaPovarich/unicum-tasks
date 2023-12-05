from model import write, main, view
def function():
    while True:
        change = int(input('what would you like to do?(1 - demonstrate file, 2 - write info about you): '))
        if change == 1:
            view()
        elif change == 2:
            info = main()
            write(info)
            print('информация успешно записана в файл!')