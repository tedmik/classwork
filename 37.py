num_sides = int(input("How many sides does your shape have?: "))
if(num_sides == 3):
  print("Your shape is a triangle")
elif(num_sides == 4):
  print("Your shape is a square or rectangle")
elif(num_sides == 5):
  print("Your shape is a pentagon")
elif(num_sides == 6):
  print("Your shape is a hexagon")
elif(num_sides == 7):
  print("Your shape is a heptagon")
elif(num_sides == 8):
  print("Your shape is a octagon")
elif(num_sides == 9):
  print("Your shape is a nonagon")
elif(num_sides == 10):
  print("Your shape is a decagon")
elif(num_sides >= 10 or num_sides <= 3):
  print("Not supported side amount")
