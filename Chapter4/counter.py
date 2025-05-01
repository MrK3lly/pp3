# counts for user

start = int(input("Please enter the starting number: "))

end = int(input("Please enter the ending number: "))

count = int(input("Please enter how much you'd like to count by: "))

for i in range(start, end, count):
  print(i, end=" ")

