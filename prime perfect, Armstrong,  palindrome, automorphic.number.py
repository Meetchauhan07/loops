#1 Check if num is Prime
num=int(input("Enter a number:"))

prime=True
if num<=1:
    prime=False
else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
if prime:
    print(num" is a prime number")
else:
    print(num "is not a prime number")
'''
output:    
Enter a number:35
35 is NOT a prime number
'''
#2 Check if Perfect
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
perfect=(sum==num)
if perfect:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
'''
output:
Enter a number:28
It is a perfect number
'''

#3 Check if Armstrong
order=len(str(num))
sum_arm=0
temp=num
while temp>0:
    digit=temp%10
    sum_arm+=digit**order
    temp//=10
armstrong=(sum_arm==num)
if armstrong:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
'''
output:
Enter a number:153
It is an armstrong number
'''

#4 Check if Palindrome
temp=num
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10
palindrome=(reverse==num)
if palindrome:
    print("It is an palindrome number")
else:
    print("It is not an palindrome number")
'''
output:
Enter a number:89
It is not an palindrome number
'''

# 5. Check if Automorphic
square=num*num
num_str=str(num)
square_str=str(square)
if square_str.endswith(num_str):
    print("It is an automorphic number")
else:
    print("It is not an automorphic number")
'''
output
Enter a number:25
It is an automorphic number
'''
