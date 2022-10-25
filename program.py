import time
startTime = time.process_time()

def f(x):
    return(x*x)

def integral(x):
    return((x*x*x)/3)

lowerLimit = -2
upperLimit = 3
tolerance = 0.05
n=1
totalt = 0
areaDiff = 0

def userInput():
    global lowerLimit
    global upperLimit
    global tolerance
    global n 
    lowerLimit = float(input('Enter the left (lower) limit: '))
    upperLimit=float(input('Enter the right (upper) limit: '))
    while (upperLimit < lowerLimit):
        print('The upper limit must be greater than the lower one!')
        upperLimit=float(input('Enter the right (upper limit): '))
    tolerance = float(input('Enter the tolerance: '))
    n = int(input('Enter the amount of starting elements: '))

def calculate():
    global lowerLimit
    global upperLimit
    global tolerance
    global n
    global areaDiff
    global totalt
    areaDiff = integral(upperLimit)-(integral(lowerLimit))-totalt
    while(areaDiff >= tolerance or areaDiff <= -tolerance):
        totalt = 0
        for x in range(n):
            totalt += f(lowerLimit)+(4*f((lowerLimit+upperLimit)/2)) + f(upperLimit)
        totalt=(1/3)* ((upperLimit-lowerLimit)/2)*totalt
        areaDiff = integral(upperLimit)-(integral(lowerLimit))- totalt
        n+=1

userInput()
calculate()

print('Amount of elements: '+ str(n-1) + ', Totalt area: '+ str(totalt)+ ' Difference from integral: '+ str(areaDiff))
print('CPU Execution time: '+(time.process_time() - startTime), ' seconds.')
