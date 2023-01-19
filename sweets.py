# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random

def print_hi(name):
    print(f'Привет, {name}!')

def step_player(max_num, oststok):
    take_sweets = -1
    while take_sweets < 1 or take_sweets > max_num or take_sweets > oststok:
        print(f'Введите число от 1 до {max_num}! ')
        take_sweets = int(input())
        if take_sweets < 1:
            print(f'Надо взять хотя бы 1 конфету!')
        elif take_sweets > max_num:
            print(f'Не надо жадничать! Больше {max_num} конфет брать нельзя!')
        elif take_sweets > oststok:
            print(f'Нельзя взять больше, чем осталось: {oststok}')
    return take_sweets

def step_bot(max_num, ostatok):
    if ostatok <= max_num:
        take_sweets = ostatok
    else:
        take_sweets = ostatok % (max_num + 1)
        if take_sweets == 0:
            take_sweets += max_num
    return take_sweets

def sweets():
    print('Привет, я - Комп. Как тебя зовут? ')
    name = input()
    print_hi(name.capitalize())

    player1 = 'Комп'
    player2 = name.capitalize()
    sweets = int(input(f'Задай количество конфет, больше 30: '))
    print(sweets)
    max_num = 28
    ost = sweets
    print(f'Будем брать от 1 до 28 конфет за 1 ход. Побеждает тот, кто возьмёт последнюю конфету)')
    # Жеребьёвка:
    toss = random.randint(0, 1)
    if toss == 0:
        first = player1
        second = player2
        print(f'Начинаю я!')
    else:
        first = player2
        second = player1
        print(f'Твой первый ход! Бери от 1 до 28 конфет.')

    # Игра
    while sweets >= 0:
        if first == player1:
            take_bot = step_bot(max_num, ost)
            print(f'Ходит {player1}:')
            print(f'Беру {take_bot} конфет.')
            ost -= take_bot
            print(f'Осталось {ost} конфет.')
            if ost <= 0:
                print(f'Победил: {player1}!!!')
                break
        else:
            print(f'Ход {player2}:')
            take_player = step_player(max_num, ost)

            print(f'Беру {take_player} конфет')
            ost -= take_player
            print(f'Осталось {ost} конфет.')
            if ost <= 0:
                print(f'Победил: {player2}!!!')
                break
        if first == player1:
            first = player2
        else:
            first = player1

if __name__ == '__main__':
    sweets()

