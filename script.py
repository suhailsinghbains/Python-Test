#Check4thBit
def check_bit4(input):
  x = input & 0b1000
  if x:
    return "on"
  else:
    return "off"
