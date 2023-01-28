from func import *

font_digit = None

def setup():
    global font_digit
    size(600,600)
    font_digit = loadFont("ArialNarrow-Bold-48.vlw");

def draw():
    background(0, 0, 54)
    draw_number(hour(), 200, 250, font_digit, color(255, 0, 0))
    delim(260, 250, font_digit)
    draw_number(minute(), 300, 250, font_digit, color(0, 255, 100))
    delim(360, 250, font_digit)
    draw_number(second(), 400, 250, font_digit, color(0, 100, 255))
    
    noStroke()
    
    fill(0, 255, 100)
    rect(10, 400, 580, 10)    
    fill(0, 100, 255)
    rect(580 * second() / 60, 390, 20, 30)
    
    # fill(0, 255, 100)
    # rect(10, 450, 580, 10)    
    # fill(0, 100, 255)
    # rect(580 * minute() / 60, 440, 20, 30)
    
    noFill()
    strokeWeight(5)    
    stroke(0, 100, 58)    
    arc(425,235,80,100, radians(180 + millis()), radians(220 + millis()))
    stroke(255, 255, 10) 
    arc(425,235,180,50, radians(180 + millis() / 2), radians(220 + millis() / 2))
    stroke(23, 56, 100) 
    arc(425,235,20,180, radians(180 + millis() / 3), radians(220 + millis() / 3)) 
    rotate(0.5);   
    stroke(255, 0, 100) 
    arc(485,20,40,150, radians(180 + millis()), radians(220 + millis())) 
    #translate(width/2, height/2);
    #rotate(90);
    #line(200,100, 200, 200)
    
    # for a in range(360):
#     stroke(255, 255, 0)
#     rotate(0.05);  
    line(100,100, 100, 110)
    text("x " + str(mouseX) +" комбоо", 30, 30)
    print(map(1,0, 59, 0, 1000))

    




    
