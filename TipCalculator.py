
print("Welcome to the Tip Calculator.")

total_bill = float(input("What was the total bill? $"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

num_people = int(input("How many people to split the bill? "))

total_each_person = (total_bill / num_people) * (1 + (percentage_tip / 100)) 

print(f"Each person should pay: ${total_each_person:.2f}")
