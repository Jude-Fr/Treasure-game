import random
def treasure_hunt():

  l= int(input("Enter the length of the grid "))
  w= int(input("Enter the width of the grid "))

s1 = random.randint(1,w)
s2 = random.randint(1,l)
attempts =0

def row_guess():
nonlocal attempts
correct = False
while not correct:
  guess = int(input("Guess the row position "))
  attempts +=1
  if guess < s1:
    print(f"You guessed too low for the row position, try again! {attempts} attempts used!")
elif guess > s1:
print(f"You guessed too high for the row position, try again! {attempts} attemps used!")
else:
print(f"You guessed correctly! {attempts} attempts used, now try to guess the column position!")
correct = True

def column_guess():
nonlocal attempts
correct = False
while not correct:
  guess = int(input("Guess the column position "))
  attempts +=1
  if guess < s2:
    print(f"You guessed too low for the column position, try again! {attempts} attempts used!")
elif guess > s2:
print(f"You guessed too high for the column position, try again! {attempts} attemps used!")
else:
print(f"You guessed the position of the treasure correctly! {attempts} attemps used!")
correct = True

print("Guess the row in which the treasure is held")
row_guess()
print("Guess the column in which the treasure is held")
column_guess()

treasure_hunt()
