class Vehicle:
    '''Docstring'''
    year = "year"
    model = "model"
    mark = "mark"
    color = "color"
    velocity = "velocity"
    wheels = "wheels"
    step = "step"

class CarA(Vehicle):
    '''Docstring'''
    year = 2002
    model = "Mk 2"
    mark = "Mark-A"
    color = "Red"
    velocity = "140" #Km/Hr
    wheels = 4
    step = True

class CarB(Vehicle):
    '''Docstring'''
    year = 2013
    model = "Mk 7-A"
    mark = "Mark-A"
    color = "Black"
    velocity = "200" #Km/Hr
    wheels = 4
    step = False

class CarC(Vehicle):
    '''Docstring'''
    year = 2007
    model = "Mk 4"
    mark = "Mark-B"
    color = "White"
    velocity = "180" #Km/Hr
    wheels = 4
    step = True

class MotorcycleA(Vehicle):
    '''Docstring'''
    year = 2010
    model = "Mk 5-B"
    mark = "Mark-B"
    color = "Red"
    velocity = "270" #Km/Hr
    wheels = 2
    step = False

class MotorcycleB(Vehicle):
    '''Docstring'''
    year = 2014
    model = "Mk 7-B"
    mark = "Mark-A"
    color = "Gray"
    velocity = "290" #Km/Hr
    wheels = 2
    step = False

class MotorcycleC(Vehicle):
    '''Docstring'''
    year = 2021
    model = "Mk 9"
    mark = "Mark-D"
    color = "Black"
    velocity = "320" #Km/h
    wheels = 2
    step = True