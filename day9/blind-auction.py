rom replit import clear
from art import logo

dict = {}


print(logo)
print("Welcome to the secret auction program")

end_of_bid = False

while not end_of_bid:
  name = input("What is your name? ")
  bid = float(input("What is your bid? $"))
  cont = input("Are there any other bidders? Type 'yes or 'no'. ")

  dict.update({name: bid})


  if cont == 'no':
    end_of_bid = True

  clear()

max_value = max(dict, key=dict.get)

print(f"{max_value} won the auction")    
