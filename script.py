# Remove Duplicates
def remove_duplicates(obj):
  new=[]
  for item in obj:
    if(test(new,item)==False):
      new.append(item)
  return new
def test(obj,num):
  for item in obj:
    if(item==num):
      return True
  else:
    return False
