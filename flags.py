import turtle                # module des graphiques tortue
tortue = turtle.Turtle()     # créer une nouvelle tortue
tortue.speed("fastest")      # tracé rapide
turtle.mode("logo") # la tortue commence étant orientée vers le nord
tortue.setheading(90) # pour faire face a l'est

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def rectangle(width, height, color):
    """Trace un rectangle plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()
    
def three_color_flag(width, color1, color2, color3):
    """Trace le drapeau un drapeau à 3 couleurs , `color1`, `color2`, et `color3`, de taille `size`. Les couleurs sont des tranches verticales.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.pendown()
    
    def onethird_vertical(color):
        tortue.pendown()
        tortue.begin_fill()
        tortue.color(color)
        for i in range(2):
            tortue.forward(width/3)
            tortue.right(90)
            tortue.forward(2 * (width/3))
            tortue.right(90)
        tortue.end_fill()
        tortue.forward(width/3)
        tortue.end_fill()
    
    onethird_vertical(color1)
    onethird_vertical(color2)
    onethird_vertical(color3)
    tortue.penup()

    tortue.back(width)
    
def belgian_flag(width):
    """Trace le drapeau belge de longueur `width` avec des proportions 3:2.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    three_color_flag(width, "#000000", "#fddb20", "#ef303e")

def french_flag(width):
    """Trace le drapeau français de longueur `width` avec des proportions 3:2.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    three_color_flag(width, "#002153", "#ffffff", "#cf0921")

def italian_flag(width):
    """Trace le drapeau italien de longueur `width` avec des proportions 3:2.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    three_color_flag(width, "#009344", "#ffffff", "#cf2734")

def romanian_flag(width):
    """Trace le drapeau roumain de longueur `width` avec des proportions 3:2.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    three_color_flag(width, "#012a7e", "#fed116", "#cd1127")

def european_flag(width):
    """Trace le drapeau de l'Union Européenne de longueur `width` avec des proportions 3:2.

    pre: La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    rectangle(width, (2 * (width/3)), "#003297")
    tortue.penup()
    tortue.forward(width/2)
    tortue.right(90)
    tortue.forward((2 * (width/3))/2)
    tortue.left(90)
    
    def drawEUStars(size, distance):
        tortue.left(90)
        def drawStar(size, color):
            tortue.color(color)
            tortue.pendown()
            tortue.setheading(prerangeHeading + 90)
            tortue.forward(size/4)
            tortue.begin_fill()
            for i in range(0, 5):
                tortue.forward(size)
                tortue.right(144)
                tortue.forward(size)
                tortue.left(72)
            tortue.end_fill()
            tortue.right(180)
            tortue.forward(size/4)
            tortue.penup()
        
        tortue.showturtle()
        tortue.penup()
        prerangeHeading = tortue.heading()
        for i in range(0, 12):
            tortue.setheading(prerangeHeading + (i * 30))
            predrawHeading = tortue.heading()
            tortue.forward(distance)
            drawStar(size, "#fec900")
            tortue.setheading(180 + predrawHeading)
            tortue.forward(distance)
            tortue.right(180)
        tortue.setheading(prerangeHeading)
        tortue.left(90)
        tortue.forward(width/2)
        tortue.right(90)
        tortue.forward((2 * (width/3))/2)
        tortue.right(90)
        
    drawEUStars(width/40, width/4.5)

def exemple_mouvement():
    """ Fonction qui imprime des drapeaux dans une variété de positions et rotations. """
    tortue.penup()

    tortue.setposition(-240, -50)
    tortue.setheading(140)
    belgian_flag(150)
    
    tortue.setposition(-160, 150)
    tortue.setheading(100)
    italian_flag(115)
    
    tortue.setposition(130, -200)
    tortue.setheading(90)
    french_flag(190)
    
    tortue.setposition(40, -90)
    tortue.setheading(85)
    romanian_flag(34)
    
    tortue.setposition(-30, 50)
    tortue.setheading(76)
    european_flag(200)

exemple_mouvement()

turtle.done() # empêche la fenetre turtle de se fermer tout seul sur VSCode. inutil sur Thonny.