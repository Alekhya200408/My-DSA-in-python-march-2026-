# for length
s="Hello"

print(len(s))

# for revese the string
reverse=s[::-1]
print(reverse)
# with loop
rev=""
for ch in s:
    rev=ch+rev

print(rev)

# For finding Vowels
count=0
for ch in s:
    if ch in "aeiouAEIOU":
        count+=1

print (count)

# For Palindrome
st=input("Enter to check Palindrome:")

left=0
right=len(st)-1 #basically its cut out the 0th index

while left<right:
    if st[left]!=st[right]:
        print("Not Palindrome")
        break
    left+=1
    right-=1
else:
    print("Palindrome")   
    
# for counting
name=input("Enter the name:")
count=input("enter what you want to count:")
result=name.count(count)
print(result)