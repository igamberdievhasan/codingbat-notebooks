def lucky_sum(a, b, c):
  sum = 0
  if a!= 13 and b!=13 and c!= 13:
    sum = a+b+c
  if a == 13 and b == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    if a != 13:
      return a +b
    else:
      return 0
  return sum

