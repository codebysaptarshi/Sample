#Jump Game
def Jump_Game(A):
  j=0
  if(A[0]==0):
    return -1
  else:
    i=0
    a=A[0]
    while(1):
      i=i+a
      j=j+1
      #a=A[i]
      if(i>=(len(A)-1)):
        break
      else:
        a=A[i]
    return j
#main
print("Test case 1 : ")
A=[1, 4, 3, 2, 6, 7]
print("The given array is ",A)
print("The minimum number of jumps required is ",Jump_Game(A))
print()
print("Test case 2 : ")
A=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("The given array is ",A)
print("The minimum number of jumps required is ",Jump_Game(A))
print()
print("Test case 3 : ")
A=[0,1,3,1]
print("The given array is ",A)
print("The minimum number of jumps required is ",Jump_Game(A))
