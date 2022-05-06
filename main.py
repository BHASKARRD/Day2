print("Bhaskar"[3])


print(123 + 234)

num_char = len(input("what is your name"))
new_num_char = str(num_char)
print("your name has " + new_num_char + "characters.")

print(round(3/3))

score = 0
height = 7.4
inwinning = True

print(f"your score is {score}, your height is {height}, your winning is {inwinning}")


print ("welcome to the tip calcultor")
bill = float(input("what was the total bill? $"))
tip = int(input(" how much tip would you like to give? 10, 12 or 15?"))

people = int(input("how many people split the bill?"))
bill_with_tip = tip / 100 * bill + bill

print (bill_with_tip)