mok = set()
mac = set()

for mis in range(5):
    mok.add(mis)
    mok.add(455)
for mip in range(8):
    mac.add(mip)

print(mok)
print(mac)

print(mac | mok)

# tasj = mok.difference(mac)
# print(tasj)



# set1 = set() 
# set2 = set() 
  
# for i in range(5): 
#     set1.add(i) 
  
# for i in range(3,9): 
#     set2.add(i) 
  
# # Difference of two sets 
# # using difference() function 
# set3 = set1.difference(set2) 
  
# print(" Difference of two sets using difference() function") 
# print(set3) 
  
# # Difference of two sets 
# # using '-' operator 
# set3 = set1 - set2 
  
# print("\nDifference of two sets using '-' operator") 
# print(set3) 