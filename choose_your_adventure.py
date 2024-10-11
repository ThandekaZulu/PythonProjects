name = input("Type your name: ")
print("welcome", name, "to this adventure!")

should_we_play = input("Do you want to play? ").lower()


if should_we_play == "yes" or should_we_play == "y":
  print("Let play!")

  direction = input("Left/Right? ").lower()
  if direction == "left":
    print("Sorry game over")
  elif direction == "right":
    choice = input("Bridge (swim/cross)? ")
    if choice == "swim":
      print("Eaten by allegator")
    else:
      print("You won!")
  else:
    print("Not valid reply.")

else:
  print("Not playing then")
