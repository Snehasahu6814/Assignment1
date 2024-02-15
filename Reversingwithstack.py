# String=input("Enter a String")
# Text=String.split()[::-1]

# l=[]
# for i in Text:
#     l.append(i)
# print(" ".join(l))

String=input("Enter a String : ")

    
Text=String.split()

stack=[]
for i in range (0,len(Text)):
   stack.append(Text[i])
print('Reversed String is :')
for i in range(0,len(Text)):
    print(stack.pop(),end=" ")


 