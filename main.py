from os import system
import classes

carA        = classes.CarA()
carB        = classes.CarB()
carC        = classes.CarC()
motorcycleA = classes.MotorcycleA()
motorcycleB = classes.MotorcycleB()
motorcycleC = classes.MotorcycleC()

cars = [carA, carB, carC, motorcycleA, motorcycleB, motorcycleC]
cabecalho = ['Year', 'Model', 'Motor', 'Color', 'Velocity', 'Wheels', 'Step']

system('cls')

def line():
    '''Docstring'''
    for j in range(0, len(cabecalho)):
        tamanho = len(cabecalho[j]) + 4
        print(f'+' + '-' * tamanho, end = '')
    print('+\n', end = '')

line()

for j in range(0, len(cabecalho)):
    tamanho = len(cabecalho[j]) + 4
    print(f'|  {cabecalho[j]}  ', end = '')
print('|\n', end = '')

line()

for i in range(0, len(cars)):
    print(f'| {cars[i].year:^7}', end='')
    print(f'| {cars[i].model:^7}', end=' ')
    print(f'| {cars[i].mark:7}', end=' ')
    print(f'| {cars[i].color:^7}', end=' ')
    print(f'|  {cars[i].velocity:^9}', end=' ')
    print(f'| {cars[i].wheels:^8}', end=' ')
    print(f'| {cars[i].step:^7}|')

line()
