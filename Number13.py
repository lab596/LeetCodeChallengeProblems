s = input("Input a Roman Numeral: ")

dict = { "I" : 1,
        "V" : 5,
       "X" : 10,
      "L" : 50,
      "C" : 100,
      "D" : 500,
      "M" : 1000,
      "IV":4,
      "IX":9,
      "XL": 40,
      "XC":90,
      "CD":400,
      "CM":900
       }

symbols = []
skip = False

for i in range(len(s)):
  if(skip == True):
    skip = False
    continue
  
  if(i<len(s)-1 and (s[i:i+1] == "I" and (s[i+1:i+2] == "V" or s[i+1:i+2] == "X")) or (s[i:i+1] == "X" and (s[i+1:i+2] == "L" or s[i+1:i+2] == "C")) or (s[i:i+1] == "C" and (s[i+1:i+2] == "D" or s[i+1:i+2] == "M"))):
    skip = True
    symbols.append(s[i:i+2])

  else:
    symbols.append(s[i:i+1])




number = 0

for j in symbols:
  number += dict[str(j)]

print(number)
