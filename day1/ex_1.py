import matplotlib.pyplot as mplot
import numpy as np
import sys
import math

xval = np.linspace(-3, 3, num = 101)
yval = []

if not sys.argv[1:]:
	print("usage: ex_1.py [function_number]\n\nFunction:\n\
		(1) -> f(x) = x\n\
		(2) -> f(x) = x**2\n\
		(3) -> f(x) = x**3\n\
		(4) -> f(x) = sin(x)\n\
		(5) -> f(x) = cos(x)\n\
		(6) -> f(x) = tan(x)\n\
		(7) -> f(x) = exp(x)\n\
		(8) -> f(x) = sqrt(|x|)\n")
		
	exit(1)

elif sys.argv[1] == "1":
	for i in xval:
		yval.append(i)

	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x')
	mplot.show()

elif sys.argv[1] == "2":
	for i in xval:
		yval.append(i**2)
	
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x**2')

elif sys.argv[1] == "3":
	for i in xval:
		yval.append(i**3)

	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = x**3')

elif sys.argv[1] == "4":
	for i in xval:
		yval.append(math.sin(i))

	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = sin(x)')
	mplot.show()

elif sys.argv[1] == "5":
	for i in xval:
		yval.append(math.cos(i))

	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = cos(x)')
	mplot.show()

elif sys.argv[1] == "6":
	for i in xval:
		yval.append(math.tan(i))

	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = tan(x)')

elif sys.argv[1] == "7":
	for i in xval:
		yval.append(math.exp(i))
	
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = exp(x)')
	mplot.show()

elif sys.argv[1] == "8":
	for i in xval:
		yval.append(math.sqrt(abs(i)))
	
	mplot.plot(xval, yval)
	mplot.ylabel('f(x)')
	mplot.xlabel('x')
	mplot.title('y = sqrt(|x|)')
	mplot.show()
