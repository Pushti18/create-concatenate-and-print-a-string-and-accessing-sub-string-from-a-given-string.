st = "University"
for x,y in zip(st,st[::-1]):
  print(x,y,sep="\t")
r="ICT"
print(r)
print(','.join([st,r]))
print(r[::1])
print(r[::-1])
print(r[::2])
print(r[::-2])