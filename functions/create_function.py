""" 
Four Function Categories
1. the one that have no parameters and do not return any value
    def hello():
        print("Hello friends")

2. have no parameters but do return a value
    def get_favorite_food():
        food = input("What's your favorite food?")
        return food

3. have parameters and don't return a value
    def check_grade(grade):
        if grade == "A":
            print("You aced the class")

4. have both parameters and also return a value
    def withdraw_money(current_balance, amount):
        if(current_balance >= amount):
            current_balance = current_balance - amount
        return current_balance

"""

print("~~~ The Shimmy ~~~")

def shimmy():
    print("Take one step to the right and stamp.")
    print("Take one step to the left and stomp.")
    print("Shake those hips!")

shimmy()
shimmy()
shimmy()