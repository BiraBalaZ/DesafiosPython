from os import system
import classes

carA        = classes.CarA()
carB        = classes.CarB()
carC        = classes.CarC()
motorcycleA = classes.MotorcycleA()
motorcycleB = classes.MotorcycleB()
motorcycleC = classes.MotorcycleC()

cars = [carA, carB, carC, motorcycleA, motorcycleB, motorcycleC]

system('cls')
print('+--------+---------+---------+---------+----------+---------+--------+')
print('|  Year  |  Model  |  Motor  |  Color  | Velocity |  Wheels |  Step  |')
print('+--------+---------+---------+---------+----------+---------+--------+')

for i in range(0, len(cars)):
    print(f'| {cars[i].year:^7}', end='')
    print(f'| {cars[i].model:^7}', end=' ')
    print(f'| {cars[i].mark:^7}', end=' ')
    print(f'| {cars[i].color:^7}', end=' ')
    print(f'|  {cars[i].velocity:^7}', end=' ')
    print(f'| {cars[i].wheels:^7}', end=' ')
    print(f'| {cars[i].step:^7}|')

print('+--------+---------+---------+---------+----------+---------+--------+')
