
def convert_to_deget_format(number): 
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)

       
def draw_number(number, x, y, font_digit, clr=color(0, 255 ,0)): 
    fill(clr)
    textSize(120)
    textFont(font_digit)
    number = convert_to_deget_format(number)
    text(number, x, y)
    
def delim(x,y,font_digit):
    textSize(120)
    textFont(font_digit)
    text(':', x, y)
