
def twoNum(arr1, arr2):
  arr1num = ""
  arr1numc = ""
  arr2num = ""
  arr2numc = ""
  for i in arr1:
    arr1num += str(i) 


  for i in arr2:
    arr2num += str(i) 

  arr2numc = arr2num[::-1]
    
  arr1numc = arr1num[::-1]

  a = int(arr1numc)
  b = int(arr2numc)

  c = a + b

  ci = str(c)[::-1]
  
  arrf = []

  for i in str(ci):
    arrf.append(int(i))
  
  print(arrf)
    

  

twoNum([9,9,9,9,9,9,9],[9,9,9,9])
