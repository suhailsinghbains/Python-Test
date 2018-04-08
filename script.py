# Purify
def purify(obj):
  test=[]
  for num in obj:
    if(num%2==0):
      test.append(num)
  return test
