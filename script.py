# Median
def median(obj):
  l = len(obj)
  obj = sorted(obj)
  if(l%2==0)and(l!=1):
    return ((obj[(l/2)-1]+obj[l/2])/2.)
  else:
    return obj[l/2]

print (median([1]))
