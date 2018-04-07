#Censorship comes into action
def censor(text, word):
  l = len(text)
  i=0
  obj=[]
  test=[]
  final=""
  while(i<l):
      test.append(text[i])
      if(text[i:i+len(word)]==word):
          j=0
          while(j<len(word)):
              obj.append(i+j)
              j+=1
      i+=1
  print (obj)
  k=0
  while (k<l):
      if k in obj:
          test[k]="*"
      k+=1
  k=0
  while(k<l):
    final+=str(test[k])
    k+=1
  return final
print (censor("this hack is wack hack", "hack"))
