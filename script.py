# Reversing using Loop
def reverse(text):
  i = len(text)
  newText = ""
  while(i>0):
    newText+=text[i-1]
    i-=1
  return newText
print (reverse("HI"))
