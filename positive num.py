#positive numbers in lists
mylist[]
n=int(input("Enter the number of elements"))
for in range(0,n):
      val=int(input())
      mylist.append(val)
for num in mylist:
      if num>=0:
         print(num,end="")
