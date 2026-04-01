from turtle import *
from time import sleep

t = Turtle()
t.speed(0)

def plano_cartesiano():
    t.pu()
    t.goto(-300, 0)
    t.pd()
    t.goto(300, 0)
    t.stamp()

    t.pu()
    t.goto(0, -300)
    t.pd()
    t.goto(0, 300)
    t.lt(90)
    t.stamp()

def funcao_1(x):
    return x**0.5

def funcao_2(x):
    return 1//x

def funcao_3(x):
    return 2**x

def funcao_4(x):
    return 5 - x**2

def funcao_5(x):
    return x**2- 5*x + 6

def funcao_6(x):
    return x**3 - x**2 - x+1


plano_cartesiano()
t.color('blue')
t.pu()
t.goto(0, funcao_1(0))
t.pd()
for x in range(0, 201):
    t.goto(x, funcao_1(x)*2)

sleep(3)
t.clear()

t.color('black')
t.seth(0)
plano_cartesiano()
t.color('blue')
t.pu()
t.goto(1, funcao_2(1))
t.pd()
for x in range(1, 201):
    t.goto(x, funcao_2(x))

sleep(3)
t.clear()

t.color('black')
t.seth(0)
plano_cartesiano()
t.color('blue')
t.pu()
t.goto(-100, funcao_3(-5))
t.pd()
for x in range(-5, 8):
    t.goto(x*2, funcao_3(x)*2)

sleep(3)
t.clear()

t.color('black')
t.seth(0)
plano_cartesiano()
t.color('blue')
t.pu()
t.goto(-21, funcao_4(-21))
t.pd()
for x in range(-20, 50):
    t.goto(x, funcao_4(x))

sleep(3)
t.clear()

t.color('black')
t.seth(0)
plano_cartesiano()
t.color('blue')
t.pu()
t.goto(-21, funcao_5(-21))
t.pd()
for x in range(-20, 50):
    t.goto(x, funcao_5(x))

sleep(3)
t.clear()

t.color('black')
t.seth(0)
plano_cartesiano()
t.color('blue')
t.pu()
t.goto(-21, funcao_6(-21))
t.pd()
for x in range(-20, 50):
    t.goto(x, funcao_6(x))

sleep(3)
t.clear()



mainloop()