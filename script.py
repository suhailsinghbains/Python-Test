# Product from Object
def product(obj):
  product=1
  for num in obj:
    product*=num
  return product

print (product([3,4,5,6]))
