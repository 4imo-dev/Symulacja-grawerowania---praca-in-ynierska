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
    t.goto(x + s * 0.25, y + s)
    t.goto(x + s * 0.5, y)
    t.penup()
    t.goto(x + s * 0.1, y + s * 0.38)
    t.pendown()
    t.goto(x + s * 0.4, y + s * 0.38)
    t.penup()

    t.goto(x + s * 0.5, y)
    t.setheading(90)

#POPRAWIĆ KOŃCOWĄ ODLEGŁOŚĆ
def litera_B(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.2)
    t.circle(-s * 0.24, 180)
    t.forward(s * 0.2)
    t.left(180)
    t.forward(s * 0.22)
    t.circle(-s * 0.26, 180)
    t.forward(s * 0.22)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

# POPRAWIĆ
def litera_C(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.45, y + s * 0.9)
    t.setheading(135)
    
    t.pendown()
    t.circle(s * 0.3, 90)
    t.circle(s * 0.55, 100)
    t.circle(s * 0.3, 90)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

#POPRAWIĆ KOŃCOWĄ ODLEGŁOŚĆ
def litera_D(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)
    
    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.15)
    t.circle(-s * 0.5, 180)
    t.forward(s * 0.15)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

def litera_E(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.42)
    t.penup()
    t.goto(x, y + s * 0.52)
    t.setheading(0)
    t.pendown()
    t.forward(s * 0.32)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(s * 0.42)
    t.penup()

    t.goto(x + s * 0.42, y)
    t.setheading(90)

def litera_F(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.42)
    t.penup()
    t.goto(x, y + s * 0.52)
    t.pendown()
    t.forward(s * 0.32)
    t.penup()

    t.goto(x + s * 0.42, y)
    t.setheading(90)

# POPRAWIĆ
def litera_G(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.45, y + s * 0.9)
    t.setheading(135)

    t.pendown()
    t.circle(s * 0.3, 90)
    t.circle(s * 0.55, 100)
    t.circle(s * 0.3, 90)
    t.setheading(90)
    t.forward(s * 0.35)
    t.setheading(180)
    t.forward(s * 0.22)
    t.penup()

    t.goto(x + s * 0.6, y)
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
    t.forward(s * 0.42)
    t.penup()
    t.goto(x + s * 0.42, y)
    t.setheading(90)
    t.pendown()
    t.forward(s)
    t.penup()

    t.goto(x + s * 0.42, y)
    t.setheading(90)

def litera_I(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.penup()

    t.goto(x, y)
    t.setheading(-90)

#POPRAWIĆ KOŃCOWĄ ODLEGŁOŚĆ
def litera_J(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s * 0.25)
    t.setheading(-90)

    t.pendown()
    t.circle(s * 0.2, 180)
    t.forward(s * 0.8)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

def litera_K(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)
    
    t.pendown()
    t.forward(s)
    t.penup()
    t.goto(x, y + s * 0.45)
    t.pendown()
    t.goto(x + s * 0.42, y + s)
    t.penup()
    t.goto(x + s * 0.13, y + s * 0.62)
    t.pendown()
    t.goto(x + s * 0.42, y)
    t.penup()

    t.goto(x + s * 0.42, y)
    t.setheading(90)

def litera_L(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s)
    t.setheading(-90)

    t.pendown()
    t.forward(s)
    t.left(90)
    t.forward(s * 0.38)
    t.penup()

    t.goto(x + s * 0.38, y)
    t.setheading(90)

def litera_M(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.goto(x + s * 0.25, y + s * 0.4)
    t.goto(x + s * 0.5, y + s)
    t.setheading(-90)
    t.forward(s)
    t.penup()

    t.goto(x + s * 0.5, y)
    t.setheading(90)

def litera_N(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.goto(x + s * 0.42, y)
    t.forward(s)
    t.penup()

    t.goto(x + s * 0.42, y)
    t.setheading(90)

#POPRAWIĆ KOŃCOWĄ ODLEGŁOŚĆ
def litera_O(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.25, y)
    t.setheading(0)

    t.pendown()
    t.circle(s * 0.25, 90)
    t.forward(s * 0.5)
    t.circle(s * 0.25, 180)
    t.forward(s * 0.5)
    t.circle(s * 0.25, 90)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

#POPRAWIĆ KOŃCOWĄ ODLEGŁOŚĆ
def litera_P(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.2)
    t.circle(-s * 0.24, 180)
    t.forward(s * 0.2)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

def litera_R(t, s):
    x, y = t.xcor(), t.ycor()
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.right(90)
    t.forward(s * 0.2)
    t.circle(-s * 0.24, 180)
    t.forward(s * 0.2)
    t.goto(x + s * 0.42, y)
    t.penup()

    t.goto(x + s * 0.42, y)
    t.setheading(90)

#POPRAWIĆ KOŃCOWĄ ODLEGŁOŚĆ
def litera_S(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.42, y + s * 0.9)
    t.setheading(135)

    t.pendown()
    t.circle(s * 0.22, 190)
    t.setheading(-30)
    t.forward(s * 0.25)
    t.circle(-s * 0.22, 200)
    t.penup()
    
    t.goto(x + s * 0.6, y)
    t.setheading(90)

def litera_T(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.22, y)
    t.setheading(90)

    t.pendown()
    t.forward(s)
    t.setheading(180)
    t.backward(s * 0.22)
    t.forward(s * 0.44)
    t.penup()

    t.goto(x + s * 0.44, y)
    t.setheading(90)

#POPRAWIĆ KOŃCOWĄ ODLEGŁOŚĆ
def litera_U(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s)
    t.setheading(-90)

    t.pendown()
    t.forward(s * 0.75)
    t.circle(s * 0.22, 180)
    t.forward(s * 0.75)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

def litera_W(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s)
    t.setheading(90)

    t.pendown()
    t.goto(x + s * 0.15, y)
    t.goto(x + s * 0.3, y + s * 0.5)
    t.goto(x + s * 0.45, y)
    t.goto(x + s * 0.6, y + s)
    t.penup()

    t.goto(x + s * 0.6, y)
    t.setheading(90)

def litera_Y(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x + s * 0.22, y)
    t.setheading(90)

    t.pendown()
    t.forward(s * 0.5)
    t.goto(x, y + s)
    t.penup()
    t.goto(x + s * 0.22, y + s * 0.5)
    t.pendown()
    t.goto(x + s * 0.44, y + s)
    t.penup()

    t.goto(x + s * 0.44, y)
    t.setheading(90)

def litera_Z(t, s):
    x, y = t.xcor(), t.ycor()
    t.penup()
    t.goto(x, y + s)
    t.setheading(0)

    t.pendown()
    t.forward(s * 0.42)
    t.goto(x, y)
    t.forward(s * 0.42)
    t.penup()

    t.goto(x + s * 0.42, y)
    t.setheading(90)