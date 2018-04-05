# Prime or Not
def is_prime(x):
  n=2;
  if(x<n):
      return True
  while(n!=x):
    if(x%n==0):
      return False
    n+=1
  return True

x = is_prime(1)
print (x)
