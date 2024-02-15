


String=input("Enter a String: ")
Text=String.strip('"').split()
rev = ' '.join(reversed(Text))
result = f'"{rev}"'
print(result)