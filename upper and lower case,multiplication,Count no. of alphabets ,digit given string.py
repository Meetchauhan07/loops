#alphabets in upper case and in lower case.
print("uppercase letters:")
for i in range(65,91):
    print(chr(i),end=',')
print("\n")
print("lowercase letters:")
for i in range(97, 123):
    print(chr(i), end=',')

'''
output:
uppercase letters:
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,

lowercase letters:
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
'''
#multiplication table
a=int(input("Enter the number"))
for i in range(1,11):
    print(a,'X',i,'=',a*i)
'''
output:
Enter the number7
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
'''
#Count no. of alphabets and no. of digits in any given string.
string=input("Enter the string")
a=0
d=0
for char in string:
    if('a'<=char<='z')or('A'<=char<'Z'):
        a=a+1
    elif'0'<=char<='9':
        d=d+1
print("Number of alphabets:",a)
print("Number of digits:",d)
'''
output:
Enter the string3431dhhcvb
Number of alphabets: 6
Number of digits: 4
'''








