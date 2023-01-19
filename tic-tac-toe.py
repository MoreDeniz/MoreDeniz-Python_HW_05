# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

field = list(range(1, 10))
# Функция для отображения поля
def my_field(val):
    print("\t     |     |")
    print(f"\t  {val[0]}  |  {val[1]}  |  {val[2]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {val[3]}  |  {val[4]}  |  {val[5]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {val[6]}  |  {val[7]}  |  {val[8]}")
    print("\t     |     |")

def one_step(symbol):
    flag = False
    while not flag:
        try:  # Обработка ошибок ввода
            print("Ход ", symbol, end=": ")
            chance = int(input("Выбирай поле: "))
        except ValueError:
            print("Неверный ввод!!! Попробуй ещё раз ")
            continue
        if 0 < chance < 10:
            if (str(field[chance - 1]) not in 'XO'):
                field[chance - 1] = symbol
                flag = True
            else:
                print("Ooops! Поле уже занято! Выбирай другое! ")
            continue
        else:
            print("Неверный ввод!!! Попробуй ещё раз ")


def check_Victory(field):
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
            [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  # все возможные комбинации
    for i in wins:
        if field[i[0]-1] == field[i[1]-1] == field[i[2]-1]:
            return field[i[0]-1]
    return False

def single_game():
    my_field(field)
    counter = 0
    while True:  # цикл для одной игры
        if counter % 2 == 0:
            one_step('X')
        else:
            one_step('O')
        counter += 1

        winner = check_Victory(field)
        if winner:
            my_field(field)
            print(f'УРА!!! Победил {winner}!')
            break
        if counter == 9:
            my_field(field)
            print(f'НИЧЬЯ!!!')
            break
        my_field(field)

if __name__ == "__main__":
    print('ИГРА КРЕСТИКИ-НОЛИКИ. Первым ходит "Х".')
    win = single_game()

