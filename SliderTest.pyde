from slider import Slider

slider1 = Slider(0,20,6)
slider2 = Slider(200,300,220)

def setup():
    size(600,600)
    slider1.position(20,20)
    slider2.position(20,60)
    
def draw():
    background(255)
    num = slider1.value()
    num2 = slider2.value()
    println(str(num)+","+str(num2))