
def longestSub(stra):
  count =  0
  letters = []
  nums = []
  strings = []
  for i in stra:
    for j in letters:
      if j == i:
        nums.append(count)
        count = 0
        streak = ""
        for a in letters:
          streak += a
        strings.append(streak)
        letters = []
    letters.append(i)
    count+=1

  nums.append(count)

  highest = 0;
  for i in nums:
    if i > highest:
      highest = i

  lena = ""
  for a in strings:
    if len(a) == highest:
      lena = a

  print(str(highest)+" with "+str(lena))

longestSub("heheheha")
