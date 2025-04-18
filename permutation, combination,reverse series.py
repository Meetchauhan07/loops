#Print nCr and nPr.
n=int(input("no. of items:"))
r=int(input("no. of ways to choose:"))
#permutation
nfactorial=1
for i in range(1,n+1):
    nfactorial*=i
nrfactorial=1
for j in range(1,(n-r)+1):
    nrfactorial*=j
permutation=nfactorial/nrfactorial
print("nPr:",permutation)
#Combination
rfactorial=1
for i in range(1,r+1):
    rfactorial*=i
combination=nfactorial/(nrfactorial*rfactorial)
print("nCr",combination)
'''
output:
no. of items:10
no. of ways to choose:3
nPr: 720.0
nCr 120.0
'''
#Print N natural nos. in reverse.
n=int(input("Enter the number:"))
for i in range(n,0,-1):
    print(i,end=' ')
'''
output:
Enter the number:5
5 4 3 2 1
'''

    
    
