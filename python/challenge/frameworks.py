frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

try:
  print("Enter the index of the element that you want to extract from the list:")  
  
  index = int(input())

  print(frameworks[index])

except:
    print("Error")
  