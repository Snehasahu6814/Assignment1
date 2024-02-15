
# from collections import OrderedDict
# String=input("Enter a String")
# d1=dict()

# for x in String:
#     if  x in d1:
#         d1[x]=d1[x]+1
#     else:
#         d1[x]=1
#         dict = OrderedDict(sorted(d1.items()))
# res= max(dict,key=dict.get)
        
# print(res)


from collections import Counter
def StringOccurence(String):
    charcount=Counter(String)
    # print(charcount.items())
    
    sort=sorted(charcount.items(),key=lambda x: (-x[1],x[0]))
    
    
    # print(sort)
    for i,s in sort[:3]:
        print(f"{i}:{s}")
   
    
String="HAPPIESTMINDS"
StringOccurence(String)



    
    
    
