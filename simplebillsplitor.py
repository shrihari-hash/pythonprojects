people = int(input("How many people are in the group: "))

names = [] 
amounts = []


for i in range(people):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

print("\nPeople names in the group:")
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")


Bill_amount = int(input("\nEnter the total amount: "))


for i in range(people):
    amount = int(input(f"Enter amount paid by {names[i]}: "))
    amounts.append(amount)

print("\nPeople and their amounts:")
for i, (name, amount) in enumerate(zip(names, amounts), start=1):
    print(f"{i}. {name} - {amount}")


if sum(amounts) == Bill_amount:
    print("\n✅ The total matches the bill amount!")
else:
    print(f"\n❌ The total does not match. Entered total = {sum(amounts)}, Bill = {Bill_amount}")
