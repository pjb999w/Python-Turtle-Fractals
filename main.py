# import lines
from tkinter import *
import tkinter.ttk as ttk
import turtleFigures
import turtle

# make the frame and give its geometry
root = Tk()
root.title("Turtle Application")
root.geometry("1000x800+300+300")
root.configure(bg = "black")

#--------------make the interface-----------

#make the canvas panel

canvasPanel = LabelFrame(root, text = "Canvas Frame", bg = "Red")
canvasPanel.grid(row = 0, column = 3, columnspan = 100, rowspan = 100)

canvas = Canvas(canvasPanel, width = 700, height = 700)
canvas.pack()

#make the control panel
controlPanel = LabelFrame(root, text = "Control Panel")
controlPanel.grid(row = 0, column = 0, rowspan = 7, columnspan = 3)

#make the info panel
infoPanel = LabelFrame(root, text = "Information", bg = "red")
infoPanel.grid(row = 8, column = 0, rowspan = 7, columnspan = 3)

infoText = Text(infoPanel, height = 25, width = 25, bg = "lightgreen", fg = "red")
infoText.pack()


#get the canvas pen and screen
screen = turtle.TurtleScreen(canvas)
pen = turtle.RawTurtle(screen)
0

#control the turtle pen and screen

pen.color("red")
pen.speed(0)
pen.width(1)






screen.bgcolor("blue")


# make the first label
label = Label(controlPanel, text = "Turtle Generator")
label.grid(row = 0, column = 0, columnspan = 2)

# make the euro widgets
lengthLabel = Label(controlPanel, text = "Length")
lengthLabel.grid(row = 1, column = 0)

lengthStr = StringVar()
lengthEntry = Entry(controlPanel, textvariable = lengthStr)
lengthEntry.grid(row = 1, column = 1)

# make the dollar widgets
orderLabel = Label(controlPanel, text = "Order")
orderLabel.grid(row = 2, column = 0)

orderStr = StringVar()
orderEntry = Entry(controlPanel, textvariable = orderStr)
orderEntry.grid(row = 2, column = 1)

# make the clear button
def clearF():
    # reset the entries using their textvars
    euroStr.set("")
    dollarStr.set("")
#end
clearButton = Button(controlPanel, text = "Clear", command = clearF)
clearButton.grid(row = 3, column = 0)


#make draw command
def drawF():
    #get the values of order and length
    length = int(lengthStr.get())
    order = int(orderStr.get())
    #get figure id
    figure = figureStr.get()
    figureId = figureList.index(figure)
    if figureId == 0:
        #insert text info
        infoText.insert(INSERT, "Name:\nTree\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        pen.up(); pen.backward(length);pen.down()

        # pen draws binary tree
        turtleFigures.tree(order, length, pen)
    elif figureId == 1:
        #insert text info
        infoText.insert(INSERT, "Name:\nCircle\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # pen draws binary circle
        turtleFigures.circle(order, length, pen)
    elif figureId == 2:
        #insert text info
        infoText.insert(INSERT, "Name:\nFern\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        
        #pen.up(); pen.forward(length);pen.down()
        #pen.up(); pen.backward(length);pen.down()

        # pen draws binary fern
        turtleFigures.fern(order, length, pen)
    elif figureId == 3:
        #insert text info
        infoText.insert(INSERT, "Name:\nDandelion\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        #pen.up(); pen.backward(length);pen.down()

        # pen draws binary dandelion
        turtleFigures.dandelion(order, length, pen)
        
    elif figureId == 4:
        #insert text info
        infoText.insert(INSERT, "Name:\nFlake\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        #pen.up(); pen.backward(length);pen.down()

        # pen draws flake
        print(order, length, "flake")
        turtleFigures.flake(order, length, pen)
    elif figureId == 5:
        #insert text info
        infoText.insert(INSERT, "Name:\nAntiflake\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        #pen.up(); pen.backward(length);pen.down()

        # pen draws antiflake
        print(order, length, "antiflake")
        turtleFigures.antiflake(order, length, pen)
    elif figureId == 6:
        #insert text info
        infoText.insert(INSERT, "Name:\nC Curve\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        #pen.up(); pen.backward(length);pen.down()

        # pen draws c_curve
        print(order, length, "c_curve")
        turtleFigures.c_curve(order, length, pen)
    elif figureId == 7:
        #insert text info
        infoText.insert(INSERT, "Name:\nPentagon\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        #pen.up(); pen.backward(length);pen.down()

        # pen draws pentagon
        print(order, length, "pentagon")
        turtleFigures.pentagon(order, length, pen)
    elif figureId == 8:
        #insert text info
        infoText.insert(INSERT, "Name:\nSwiss Casket\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        #pen.up(); pen.backward(length);pen.down()

        # pen draws swiss_casket
        print(order, length, "swiss_casket")
        turtleFigures.swiss_casket(order, length, pen)
    elif figureId == 9:
        #insert text info
        infoText.insert(INSERT, "Name:\nSierpinski Gasket\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        #pen.up(); pen.backward(length);pen.down()

        # pen draws sierpinski_gasket
        print(order, length, "sierpinski_gasket")
        turtleFigures.sierpinski_gasket(order, length, pen)
    elif figureId == 10:
        #insert text info
        infoText.insert(INSERT, "Name:\nSquare\n\n")
        lengthStrVar = str(lengthStr.get())
        orderStrVar = str(orderStr.get())
        infoText.insert(INSERT, "Length:\n%s" % (lengthStrVar))
        infoText.insert(INSERT, "\n\nOrder:\n%s\n\n" % (orderStrVar))
        # move pen to a better position
        pen.up(); pen.goto(0, -200);pen.down()

        # pen draws square
        print(order, length, "square")
        turtleFigures.square(order, length, pen)
        


#make draw button
drawButton = Button(controlPanel, text = "Draw", command = drawF)
drawButton.grid(row = 6, column = 1)

#make figure list

figureList = ["Tree", "Circle", "Fern", "Dandelion", "Flake", "Antiflake", "C Curve", "Pentagon", "Swiss Casket", "Sierpinski Gasket", "Square"]
figureStr = StringVar()
figureOptionMenu = ttk.OptionMenu(controlPanel, figureStr, figureList[0], *figureList)
figureOptionMenu.grid(row = 4, column = 1)

    
