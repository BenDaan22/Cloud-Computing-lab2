#fibonacci sequence codes
# sum of two elements defines the next
#EULER challenges

num = 0
nextNum = 1

print("The sequence is \n")
while nextNum < 10:
  print(nextNum, end =',')
  #num = nextNum
  #nextNum = num + nextNum
  num, nextNum = nextNum, num + nextNum

