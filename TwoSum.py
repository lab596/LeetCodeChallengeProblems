
def twoSum(arr, tar):
  num1 = 0
  for j in range(len(arr)-1):
    num2 = 1
    for i in range(len(arr)-1):  
      sum = arr[num1] + arr[num2]
      if sum == tar:
        print("["+str(num1)+","+str(num2)+"]")
      num2+=1
    num1+=1
  


twoSum([2,7,11,15], 9)
