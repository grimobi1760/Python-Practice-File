#set the function of cheese and cracker and assign two args
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")
#assign values to args directly
print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)
#assign values to args through variables
print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#doing math within the args
print("We can even do math inside too: ")
cheese_and_crackers(10+20, 5+6)
#combination of math and variable within the args
print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers)
