#Generate all Pythagorean Triplets with side length <= 30.
for a in range(1,31):
    for b in range(a,31):
        c = (a*a + b*b)**0.5
        if c==int(c) and c<=30:
            print(a,b,int(c))
'''
output:
3 4 5
5 12 13
6 8 10
7 24 25
8 15 17
9 12 15
10 24 26
12 16 20
15 20 25
18 24 30
20 21 29
'''
#Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
for i in range(24):
    if i==0:
        print("12 Midnight")
    elif i==12:
        print("12 Noon")
    elif i<12:
        print(i,"AM")
    else:
        print(i-12,"PM")
'''
output:
12 Midnight
1 AM
2 AM
3 AM
4 AM
5 AM
6 AM
7 AM
8 AM
9 AM
10 AM
11 AM
12 Noon
1 PM
2 PM
3 PM
4 PM
5 PM
6 PM
7 PM
8 PM
9 PM
10 PM
11 PM
'''

#Print factorial of a given number
n=int(input("Enter the number greater than 0:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)
'''
output:
Enter the number greater than 0:6
720
'''
























