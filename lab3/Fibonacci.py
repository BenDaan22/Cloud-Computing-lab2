#fibonacci sequence codes
# sum of two elements defines the next
#EULER challenges

num = 0
nextNum = 1

print("The sequence is \n")
while nextNum < 20:
  print(nextNum, end =',')

  num, nextNum = nextNum, num + nextNum
