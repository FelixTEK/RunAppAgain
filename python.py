#FELIXTEK 2022
argument = ""

def function():
  print("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")   #function properties
  runagain()

def runagain():
  global argument
  argument = input("Run again? (Y/N)\n> ").capitalize()
  if argument == "Y":
    function()
  elif argument == "N":
    print("Bye.")
    quit()
  else:
    print("Invalid response.")
    runagain()

if __name__ == "__main__": #main function
  while True:
    function()
    if argument == "N":
      break
    
