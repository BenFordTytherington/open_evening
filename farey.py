import turtle

########## EXTREME ##########
# Topics: Maths, Sequences #

# The function farey is required to have that name for the challenge checker !! DO NOT CHANGE !!


# INFORMATION:
# A farey sequence of order n is every fraction with numerator and denominator less than or equal to n
# example for order 3:
# 0/1, 1/3, 1/2, 2/3, 1/1

# THE CHALLENGE - create a function which creates a farey sequence stored as tuples in the form (numerator, denominator, float) and sorted
# This is so the graphics code can represent it on a turtle screen

def farey(order: int) -> set:
    return set()































# BOILERPLATE FOR THE GRAPHICS #
# order variable can be adjusted for different results (should be less than or equal to 10)
def main():
    order = 7
    f = farey(order)
    scale = 900

    colours = ['#424FFF', '#3AC7DE', '#4BF57D', '#A9DE3A', '#FAD54B', '#E38842', '#E38842', '#C738FC', '#F938FC', '#7E31EB']

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    window = turtle.Screen()
    window.bgcolor('#050505')

    window.screensize(scale, scale)

    for fract in f:
        for point in ((-450, 450), (450, 450), (-450, -450), (450, -450)):
            pen.penup()
            pen.goto(point)
            x = (fract[2] - 0.5) * scale
            pen.color(colours[fract[1] - 1])        
            pen.pendown()
            pen.goto((x, 0))
            pen.penup()
            pen.goto(point)
            y = (fract[2] - 0.5) * scale
            pen.color(colours[fract[1] - 1])
            pen.pendown()
            pen.goto((0, y))

    window.exitonclick()

if __name__ == '__main__':
    main()