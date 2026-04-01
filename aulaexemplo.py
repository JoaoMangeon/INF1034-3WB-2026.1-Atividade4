from turtle import *

def soma_2(x):
    return x + 2

t = Turtle()
t.speed(0)
#Plano Cartesiano

#Eixo dos X
t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

#Eixo dos Y
t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

#t.color("red")
#t.pu()
#t.goto(-100, soma_2(-100))
#t.pd()
#t.goto(100, soma_2(100))

#O range vai do primeiro valor até o último -1
print(list(range(-100, 100)))

t.color('blue')
t.pu()
t.goto(-200, soma_2(-200))
t.pd()
for x in range(-99, 101):
    t.goto(2*x, soma_2(2*x))

mainloop()