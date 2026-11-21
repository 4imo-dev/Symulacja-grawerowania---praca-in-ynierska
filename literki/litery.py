# ========================= BIBLIOTEKA TURTLE =========================
# t.xcor i t.ycor() zwracają aktualną pozycję turtle w układzie współrzędnych
# t.setheading(90) ustawia kierunek turtle w górę (90 stopni)

# ====================================================================
# PODPROGRAMY DLA POSZCZEGÓLNYCH LITER
# ====================================================================

def litera_A(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.goto(x + s * 0.4, y + s)
    t.goto(x + s * 0.8, y)
    t.penup()
    t.goto(x + s * 0.12, y + s * 0.3)
    t.pendown()
    t.goto(x + s * 0.68, y + s * 0.3)
    t.penup()

    t.goto(x + s * 0.8, y)
    t.setheading(90)

def litera_B(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.3)
    t.circle(-s * 0.25, 180)
    t.forward(s * 0.3)
    t.left(180)
    t.forward(s * 0.4)
    t.circle(-s * 0.25, 180)
    t.forward(s * 0.4)
    t.penup()

    t.goto(x + s * 0.65, y)
    t.setheading(90)

def litera_C(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.7, y + s * 0.9)
    t.setheading(135)
    
    t.pendown()
    t.circle(s * 0.4, 135)
    t.forward(s * 0.2)
    t.circle(s * 0.4, 135)
    t.penup()

    t.goto(x + s * 0.7, y)
    t.setheading(90)

def litera_D(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)
    
    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.2)
    t.circle(-s * 0.5, 180)
    t.forward(s * 0.2)
    t.penup()

    t.goto(x + s * 0.7, y)
    t.setheading(90)

def litera_E(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.5)
    t.penup()
    t.goto(x, y + s * 0.5)
    t.setheading(0)
    t.pendown()
    t.forward(s * 0.45)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(s * 0.5)
    t.penup()

    t.goto(x + s * 0.5, y)
    t.setheading(90)

def litera_F(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.5)
    t.penup()
    t.goto(x, y + s * 0.5)
    t.pendown()
    t.forward(s * 0.45)
    t.penup()

    t.goto(x + s * 0.5, y)
    t.setheading(90)

def litera_G(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.7, y + s * 0.9)
    t.setheading(135)

    t.pendown()
    t.circle(s * 0.4, 135)
    t.forward(s * 0.2)
    t.circle(s * 0.4, 135)
    t.setheading(90)
    t.forward(s * 0.4)
    t.setheading(180)
    t.forward(s * 0.35)
    t.penup()

    t.goto(x + s * 0.7, y)
    t.setheading(90)

def litera_H(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)
    
    t.pendown()
    t.forward(s)
    t.penup()
    t.goto(x, y + s * 0.5)
    t.setheading(0)
    t.pendown()
    t.forward(s * 0.6)
    t.penup()
    t.goto(x + s * 0.6, y)
    t.setheading(90)
    t.pendown()
    t.forward(s)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

def litera_I(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.penup()

    t.goto(x, y)
    t.setheading(-90)

def litera_J(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s * 0.05)
    t.setheading(-45)

    t.pendown()
    t.circle(s * 0.15, 135)
    t.forward(s * 0.85)
    t.penup()

    t.goto(x + s * 0.25, y)
    t.setheading(90)

def litera_K(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)
    
    t.pendown()
    t.forward(s)
    t.penup()
    t.goto(x, y + s * 0.5)
    t.pendown()
    t.goto(x + s * 0.5, y + s)
    t.penup()
    t.goto(x, y + s * 0.5)
    t.pendown()
    t.goto(x + s * 0.5, y)
    t.penup()

    t.goto(x + s * 0.5, y)
    t.setheading(90)

def litera_L(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s)
    t.setheading(-90)

    t.pendown()
    t.forward(s)
    t.left(90)
    t.forward(s * 0.45)
    t.penup()

    t.goto(x + s * 0.45, y)
    t.setheading(90)

def litera_M(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.goto(x + s * 0.5, y)
    t.goto(x + s, y + s)
    t.setheading(-90)
    t.forward(s)
    t.penup()

    t.goto(x + s, y)
    t.setheading(90)

def litera_N(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.goto(x + s * 0.7, y)
    t.forward(s)
    t.penup()

    t.goto(x + s * 0.7, y)
    t.setheading(90)

def litera_O(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.4, y)
    t.setheading(0)

    t.pendown()
    t.circle(s * 0.4, 90)
    t.forward(s * 0.2)
    t.circle(s * 0.4, 180)
    t.forward(s * 0.2)
    t.circle(s * 0.4, 90)
    t.penup()

    t.goto(x + s * 0.8, y)
    t.setheading(90)

def litera_P(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.25)
    t.circle(-s * 0.25, 180)
    t.forward(s * 0.25)
    t.penup()

    t.goto(x + s * 0.5, y)
    t.setheading(90)

def litera_R(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.25)
    t.circle(-s * 0.25, 180)
    t.forward(s * 0.25)
    t.penup()
    t.goto(x + s * 0.25, y + s * 0.5)
    t.pendown()
    t.goto(x + s * 0.5, y)
    t.penup()

    t.goto(x + s * 0.5, y)
    t.setheading(90)

def litera_S(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.5, y + s * 0.9)
    t.setheading(135)

    t.pendown()
    t.circle(s * 0.3, 90)
    t.circle(s * 0.23, 130)
    t.forward(s * 0.05)
    t.circle(-s * 0.23, 130)
    t.circle(-s * 0.3, 90)
    t.penup()
    
    t.goto(x + s * 0.5, y)
    t.setheading(90)

def litera_T(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.35, y)
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.penup()
    t.goto(x, y + s)
    t.setheading(0)
    t.pendown()
    t.forward(s * 0.7)
    t.penup()

    t.goto(x + s * 0.7, y)
    t.setheading(90)

def litera_U(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s)
    t.setheading(-90)

    t.pendown()
    t.forward(s * 0.65)
    t.circle(s * 0.35, 180)
    t.forward(s * 0.65)
    t.penup()

    t.goto(x + s * 0.7, y)
    t.setheading(90)

def litera_W(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s)
    t.setheading(0)

    t.pendown()
    t.goto(x + s * 0.3, y)
    t.goto(x + s * 0.6, y + s)
    t.goto(x + s * 0.9, y)
    t.goto(x + s * 1.2, y + s)
    t.penup()

    t.goto(x + s * 1.2, y)
    t.setheading(90)

def litera_Y(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.3, y)
    t.setheading(90)

    t.pendown()
    t.forward(s * 0.4)
    t.goto(x, y + s)
    t.penup()
    t.goto(x + s * 0.3, y + s * 0.4)
    t.pendown()
    t.goto(x + s * 0.6, y + s)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

def litera_Z(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s)
    t.setheading(0)

    t.pendown()
    t.forward(s * 0.6)
    t.goto(x, y)
    t.forward(s * 0.6)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)
