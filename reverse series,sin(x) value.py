#print N numbers of Fibonacci series
n=int(input("Enter the number:"))
a,b=0,1
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
'''
output:
Enter the number:8
0 1 1 2 3 5 8 13
'''
#Calculate sin(x),x is a radian value
x=float(input("Enter x in radians: "))  
sin_x=0
for i in range(20):  
    factorial = 1
    for j in range(1, 2*i + 2):
        factorial*=j
    power = 1
    for k in range(2*i + 1):
        power*=x
    term = ((-1)**i)*power/factorial
    sin_x+=term
print('sin({x}) ≈ ',sin_x)
'''
output:
Enter x in radians: 1.5708
sin({x}) ≈  0.9999999999932534
'''    

