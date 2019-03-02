i = int(input())
c = len(str(i))
s= 0
t =i
while t > 0:
  d = t % 10
  s += d ** c
  t //= 10
if i == s:
  print('yes')
else:
  print('no')
