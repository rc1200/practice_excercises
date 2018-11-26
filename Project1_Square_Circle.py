import turtle    
t = turtle.Turtle()
t.speed(0)



def square(length,angle):
    t.color('blue')

    for i in range(4):
        t.forward(length)
        t.left(angle)

    

#-------------------- loops -------------------

for i in range(500):
    
    square(100,90)
    t.left(1)
  
