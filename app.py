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


# Class used to hold comp values and perform actions
class ManosComputer:
    memory_dict = {}
    # This variable will indicate if it's an indirect call or not (0 or 1)
    I = 0

    def __init__(self, memory):
        self.memory_dict = memory

    sigDict = {"s1": "0", "s2": "0", "s3": "0"}

    regDict = {"AR": "455",
               "PC": "200",
               "DR": "00c7",
               "AC": "0001",
               "IR": "1200",
               "TR": "0000",
               "E": "0",
               "M": "0400"
               }

    def arGetsPc(self):
        self.regDict["AR"] = self.regDict["PC"]

    def incrementPC(self):
        self.regDict["PC"] = str(int(self.regDict["PC"]) + 1)

    def getMemory(self):
        return self.memory_dict[self.regDict["AR"]]

    def irGetsMemory(self):
        self.regDict["IR"] = self.getMemory()

    def arGetsIr(self):
        # the -3: gets the last three letters of the string IR is holding
        self.regDict["AR"] = self.regDict["IR"][-3:]


# Class used to display the values of ManosComputer
class Display:
    manoComp = ManosComputer({"": ""})

    def __init__(self, manosComputer):
        self.manoComp = manosComputer

    def displayRegisters(self):
        print("\n")
        for key in self.manoComp.regDict.keys():
            print(key + " : " + self.manoComp.regDict[key])


# Place program execution inside the main function
def main():
    memory_dict = {}
    startingPCVal = random.randint(0, 4095)

    # fills all 4096 values
    for i in range(0, 4095):
        memory_dict[str(i)] = generateHexValue()

    manosComputer = ManosComputer(memory_dict)
    display = Display(manosComputer)
    display.displayRegisters()

if __name__=='__main__':
  main()
