array = []
length = int(input("How many numbers will be there in the array:"))


print("Enter the numbers...")
for i in range(int(length)):
  num = int(input("num"+str(i+1)+":"))
  array.append(int(num))
  
print("Your list is: ", array)

# Did Timing without print statements

flag = False
for i in range(int(length)):
  for j in range(int(length)-i-1):
    if array[j] > array[j+1]:
      array[j], array[j+1] = array[j+1], array[j]
      flag = True
  if flag==False:
    break