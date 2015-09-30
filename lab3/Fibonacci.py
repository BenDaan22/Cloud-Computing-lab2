#fibonacci sequence codes
# sum of two elements defines the next
#EULER challenges

#make the variables to be added
num = 0
nextNum = 1

print("The sequence is \n")
#use while loop to loop through the sequence
while nextNum < 20:
  print(nextNum, end =',')

  #this puts the first element as the second element
  #such as num will be nextNum
  #then nextNum will be the combination of the past two numbers
  num, nextNum = nextNum, num + nextNum
