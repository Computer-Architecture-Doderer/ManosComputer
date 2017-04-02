import random

# Generates the random numbers
def generateRandomNumber():
  x = random.randint(0,14)

  if x > 9:
    if x == 10:
      x = "a"
    elif x == 11:
      x = "b"
    elif x == 12:
      x = "c"
    elif x == 13:
      x = "d"
    elif x == 14:
      x = "e"

  return str(x)

# This method is used to specify the last 3 Hex numbers if the first Hex is a 7
def pickRandomNumForSeven():
  x = random.randint(1,12)

  switcher = {
        1: "800",
        2: "400",
        3: "200",
        4: "100",
        5: "080",
        6: "040",
        7: "020",
        8: "010",
        9: "008",
        10: "004",
        11: "002",
        12: "001"
    }

  return switcher.get(x, "800")

# Generates Hex values
def generateHexValue():
  z = generateRandomNumber()

  # Check if the value is 7 because the last 3 hex can't be random if it is
  if z == "7":
    z += pickRandomNumForSeven()
  else:
    for i in range(0,3):
      z += generateRandomNumber()

  return z

# Class for converting between hex and int
class NumConverter:

  @staticmethod
  def intToHex(a):
    return format(a, 'x')

  @staticmethod
  def hexToInt(a):
    return int(a,16)

# Place program execution inside the main function
def main():
  
  # init a dictionary to hold 4096 memory values
  memory_dict = {}

  #fills all 4096 values
  for i in range(1,15):
    memory_dict[i] = generateHexValue()

  print(memory_dict)
  

if __name__=='__main__':
  main()
