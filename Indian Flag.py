import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("Black")
wn.colormode(255)  # Enable RGB mode for colors
t = turtle.Turtle()
t.speed(10)
t.penup()
t.shape("turtle")

# Function to draw filled rectangles (for the stripes)
def drawFillRectangle(x, y, length, width, color):
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.end_fill()
    t.penup()

# Function to draw a circle with a specific color
def drawCircle(x, y, color, radius):
    t.goto(x, y - radius)  # Adjust to center the circle
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

# Function to draw the 24 blue spokes of the Ashoka Chakra
def drawSpokes(x, y, radius):
    t.goto(x, y)  # Move to the center of the chakra
    t.setheading(0)
    t.pendown()
    t.color((0, 0, 128))  # Blue color for the spokes
    for i in range(24):  # Draw 24 spokes
        t.forward(radius)
        t.backward(radius)
        t.left(15)
    t.penup()

# Function to draw the saffron stripe
def drawSaffron():
    x = -230
    y = 100
    color = (255, 153, 51)  # Saffron RGB
    drawFillRectangle(x, y, 80, 460, color)

# Function to draw the white stripe
def drawWhite():
    x = -230
    y = 20
    color = 'white'
    drawFillRectangle(x, y, 80, 460, color)

# Function to draw the green stripe
def drawGreen():
    x = -230
    y = -60
    color = (19, 136, 8)  # Green RGB
    drawFillRectangle(x, y, 80, 460, color)

# Function to draw the Ashoka Chakra with blue outer line and hollow white center
def drawAshokaChakra():
    # Outer blue circle for the Ashoka Chakra
    drawCircle(0, -20, (0, 0, 128), 40)  # Outer blue circle
    # Inner white circle to create the hollow center effect
    drawCircle(0, -20, "white", 35)
    # Draw blue spokes inside the white circle
    drawSpokes(0, -20, 35)

# Drawing the flag
drawSaffron()
drawWhite()
drawGreen()

# Drawing the Ashoka Chakra with blue outline, white center, and blue spokes
drawAshokaChakra()

# Writing text at the bottom
t.goto(120, -200)
t.color((19, 136, 8))  # Green color for the text
t.write('VANDE MATARAM !!!', font=('Arial', 15, 'normal'))
t.back(20)

wn.listen()
wn.mainloop()
