s=raw_input()
c=0
sp=s.split()

for i in sp:
 if i[::1] == i[::-1]:
  c=c+1
 else:
  pass
print c
  
