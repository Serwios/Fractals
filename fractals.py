import turtle

#src -> https://habr.com/ru/company/piter/blog/496538/

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
            
            
def main(iterations, axiom, rules, angle, length=8, size=2, y_offset=0, x_offset=0, offset_angle=0, width=450, height=450):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()

    wn.exitonclick()
    
def chooseFactorial():
    print("Welcome in factorial program \n You can choose one of this factsorials")
    print("1. Koch snowflake")
    print("2. Koch square island")
    print("3. Crystall")
    print("4. Square snowflake")
    print("5. Vincheck fractal")
    
    choose = int(input("Your number: "))
    
    if choose == 1:
        return ["F--F--F", {"F":"F+F--F+F"}, 4, 60]
    elif choose == 2:
        return ["F+F+F+F", {"F":"F-F+F+FFF-F-F+F"}, 2, 90]
    elif choose == 3:
        return ["F+F+F+F", {"F":"FF+F++F+F"}, 3, 90]
    elif choose == 4:
        return ["F--F", {"F":"F-F+F+F-F"}, 4, 90]
    elif choose == 5:
        return ["F-F-F-F", {"F":"F-F+F+F-F"}, 4, 90]



settings = chooseFactorial()
main(settings[2], settings[0], settings[1], settings[3])
