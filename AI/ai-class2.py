def start_end():
  print("Welcome to the trip from Camaçari to Salvador\n")
  moves = {"1": "car", "2": "motorcycle", "3": "bike", "4": "bus"}
  ways = {
      "1": "Via Parafuso",
      "2": "Polo",
      "3": "Simões Filho",
      "4": "Dias d'Villa",
      "5": "Lauro de Freitas",
  }

  while True:
      move_choice = input("\nHow do you want to move?\n 1. Car\n 2. Motorcycle\n 3. Bike\n 4. Bus\n Enter '0' to exit: ")

      if move_choice == "0":
          print("\nExiting...")
          break

      if move_choice not in moves:
          print("Invalid choice. Please select again.")
          continue

      while True:
          way_choice = input("\nWhich way do you want to go to Salvador?\n 1. Via Parafuso\n 2. Polo\n 3. Simões Filho\n 4. Dias d'Villa\n 5. Lauro de Freitas\n: ")

          if way_choice not in ways:
              print("Invalid choice. Please select again.")
              continue
          else:
              break

      move = moves.get(move_choice)
      way = ways.get(way_choice)

      print(f"\nYou will go though via {way} using {move}. Good Trip!")

if __name__ == "__main__":
  start_end()