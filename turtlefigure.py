
import math




def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end

def fern(n, l, pen):
     print("working here")
     if n==0 or l<2 :
          return
     #endif
     
     pen.forward(0.3*l)
     pen.left(55)
     fern(n-1,l/2, pen)
     pen.right(55)
     pen.forward(0.7*l)
     pen.right(40)
     fern(n-1, l/2, pen)
     pen.left(40)
     pen.forward(l)
     pen.left(5)
     fern(n-1, 0.8*l, pen)
     pen.right(5)
     pen.backward(2*l)

#end

def circle(n, l, pen):
     print("sss")
     if n==0 or l<2 :
          return
     #endif
     pen.circle(l)
     circle(n-1, l/2, pen)
     pen.left(90)
     pen.up()
     pen.forward(2*l)
     pen.left(90)
     pen.down()
     circle(n-1, l/2, pen)
     pen.left(90)
     pen.up()
     pen.forward(2*l)
     pen.down()
     pen.left(90)

#end

def dandelion(n, l, pen):
     print("sss")
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)

#end
     
     

def koch(n, l, pen):
     if n== 0 or l<2 :
          pen.forward(l)
          return
     #endif
     koch(n-1,l/3, pen)
     pen.left(60)
     koch(n-1,l/3, pen)
     pen.right(120)
     koch(n-1,l/3, pen)
     pen.left(60)
     koch(n-1,l/3, pen)
     
# end

def flake(n, l, pen):
     if n== 0 or l<2 :
          return
     #endif
     for i in range(3):
          koch(n, l, pen)
          pen.right(120)
     #end
     
     
     
def antiflake(n, l, pen):
     if n== 0 or l<2 :
          return
     #endif
     for i in range(3):
          koch(n, l, pen)
          pen.left(120)
     #end


def c_curve(n, l, pen):
     #termination
     if n==0:
          pen.forward(l)
          return
     #endif
     c_curve(n-1, l, pen)
     pen.right(90)
     c_curve(n-1, l, pen)
     pen.left(90)

#end

def pentagon(n, l, pen):
     #termination
     if n==0:
          pen.forward(l)
          return
     else:
          for i in range(5):
               pentagon(n-1, l/4, pen)
               pen.forward(l)
               pen.left(72)

#end
     

def swiss_casket(n, l, pen):
     #termination
     if n==0:
          pen.forward(l)
          return
     else:
          for i in range(4):
               swiss_casket(n-1, l/3, pen)
               pen.forward(l)
               pen.left(90)

#end


def sierpinski_gasket(n, l, pen):
     #termination
     if n==0 or l<2:
          return
     else:
          for i in range(3):
               sierpinski_gasket(n-1, l/2, pen)
               pen.forward(l)
               pen.left(120)
#end

def corner(n, l, pen):
     if n==0 or l<2:
          return
     pen.forward(l/2)
     pen.right(90)
     pen.forward(l/2)
     pen.left(90)
     pen.forward(l)
     pen.left(90)
     pen.forward(l)
     pen.left(90)
     pen.forward(l/2)
     pen.left(90)
     pen.forward(l/2)
     pen.right(90)
     pen.forward(l/2)
     pen.backward(l/2)
     pen.right(90)
     pen.forward(l)
     pen.backward(l)
     pen.left(90)
     pen.forward(l/2)
     pen.left(90)
     corner(n-1, l/2, pen)
     pen.forward(l/2)
     pen.left(90)
     pen.forward(l/2)
     corner(n-1, l/2, pen)
     pen.forward(l/2)
     pen.left(90)
     pen.forward(l/2)
     corner(n-1, l/2, pen)
     pen.forward(l/2)
     pen.left(90)
     pen.forward(l/2)
     pen.left(90)
     pen.forward(l/2)
     pen.left(90)
     pen.backward(l)

def square(n, l, pen):
     for i in range(4):
          corner(n, l/2, pen)
          pen.forward(l/2)
          pen.left(90)
          pen.forward(l/2)

    
     

