# Make a program to distribute the class Theory of Computation through the week

def distribute_classes(days, days_of_week):
  if days < 1:
      print("Invalid number of days It should be at least 1.")
      return

  days_cycle = (days_of_week * ((days - 1) // len(days_of_week) + 1))[:days]  # Repeat days of week to cover days
 
  for day in days_cycle:
  
      print(f"\n{day}: Theory of Computation - Afternoon")  

if __name__ == "__main__":
  days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] 
  while True:
      try:
          days = int(input("Enter the number of days to distribute the classes over the week (1-5): "))
          if days < 1 or days > 5:
              raise ValueError
          break
      except ValueError:
          print("Invalid input. Please enter a number between 1 and 5.")
  distribute_classes(days, days_of_week)
