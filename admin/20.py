#Video game character power-up simulation using lists to pass data between functions
def drink_potion(stats):
    name, power = stats
    print(f"{name} drank a Magic Potion!")
    return [name, power + 10]

def wear_suit(stats):
    name, power = stats
    print(f"{name} put on Spiderman suit!")
    return [name, power + 5]

def make_hero(stats):
    name, power = stats
    return f"FINAL HERO: {name} (Power Level: {power})"

# The "Manager" function
def adventure_start(hero_name, starting_power):
    # We package the data into a list
    # drink_potion([hero_name, starting_power])
    # wear_suit([hero_name, starting_power])
    # result = make_hero([hero_name, starting_power])
    current_hero = [hero_name, starting_power]
    
    # # Passing the list through different functions (The Pipeline)
    current_hero = drink_potion(current_hero)
    current_hero = wear_suit(current_hero)
    
    result = make_hero(current_hero)
    print(result)

# Launch the game
adventure_start("Arnold", 50)



# #Higher order functions example
# def multiply(a, b):
#     return a * b

# def power(a, b):
#     return a ** b

# def run_operation(func, x, y):
#     """Takes a function as an argument and applies it."""
#     return func(x, y)

# # Usage
# print(run_operation(multiply, 5, 4)) # Result: 20
# print(run_operation(power, 2, 3))    # Result: 8

# #Recursive function example
# def countdown(n):
#     # 1. Base Case
#     if n <= 0:
#         print("You have reached the end!")
#     # 2. Recursive Step
#     else:
#         print(n)
#         countdown(n - 1)

# countdown(5)


# def factorial(n):
#   # Base case
#   if n == 0 or n == 1:
#     return 1
#   # Recursive case
#   else:
#     return n * factorial(n - 1)

# print(factorial(5))

#Fibonacci sequence using recursion
# def fibonacci(n):
#   if n <= 1:
#     return n
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(7))

