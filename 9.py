a=int(raw_input('enter marks of 1st subject:'))
b=int(raw_input('enter marks of 2nd subject:'))
c=int(raw_input('enter marks of 3rd subject:'))
d=int(raw_input('enter marks of 4th subject:'))
e=int(raw_input('enter marks of 5th subject:'))
mean=(a+b+c+d+e)/5.0
prc=((a+b+c+d+e)*100)/250
print prc
if prc<35.0:
  print'FAIL'
else:
  print'PASS'
