from turtle import *

# ----------------------------
# BACKGROUND
# ----------------------------
bgcolor("purple")

# ----------------------------
# VARIABLES
# ----------------------------
radius = 30
color1 = "white"

# ----------------------------
# DRAW MOON (CIRCLE)
# ----------------------------
penup()
goto(100, 100)
pendown()
fillcolor(color1)
begin_fill()
circle(radius)
end_fill()

# ----------------------------
# DRAW TRIANGLE (LOOP)
# ----------------------------
pensize(3)

for i in range(3):
    forward(100)
    left(120)

# ----------------------------
# DRAW STARS (LOOP + CONDITIONAL)
# ----------------------------
penup()

for i in range(3):
    goto(-100 + i * 100, 150)
    pendown()
    
    # CONDITIONAL: change color
    if i == 1:
        color("yellow")
    else:
        color("white")
    
    dot(10)  # simple star
    
    penup()

# ----------------------------
# END
# ----------------------------
done()