#Imagine you are building a video game. You need to create a "blueprint" for a character or item. Choose one to build: Robot, Wizard, Dragon, or RaceCar.
Class Name: #(Remember to capitalize the first letter! e.g., class Robot) class ___________________________ :
The __init__ Function (The Maker): # This function sets up your object when it's first created. It needs Attributes (descriptions). Example: If you chose a Car, attributes might be color and speed.
    def __init__(self, _______________, _______________):
        # (Attribute 1)    (Attribute 2)

        self._______________ = _______________
        self._______________ = _______________
________________________________________
Part 2: The Action (Method)
Now, make your object do something! Example: If you chose a Car, the action might be drive().
3. Define a Method: (Pick an action verb like jump, fly, roar, or honk)
Python
    def _______________(self):
        # (Action Name)

        print("__________________________________________")
              # (What does it say or do?)
________________________________________
Part 3: Bringing it to Life (Object)
Now that you have the blueprint, let's make the real thing!
4. Create the Object: (Give your object a variable name, like my_robot or fire_dragon)
____________________ = ____________________( "_______________", _______________ ) 
(Variable Name) 	(Class Name) 		(Value 1) 		(Value 2)
5. Call the Action: (Make your object perform the action you wrote in Part 2)
____________________ . ____________________() 
(Variable Name) 	(Action Name)
________________________________________


class Wizard:
    def __init__(self, name, hat_color):
        # These are like the labels on a folder
        self.name = name
        self.hat_color = hat_color
        print(f"✨ A new wizard named {self.name} has been created!")

    # --- THE ACTION (The Method) ---
    def cast_spell(self):
        print(f"🪄 {self.name} waves their {self.hat_color} hat and casts a spell!")
        print("💥 ZAP! BOOM! Programming is magic!")

# --- BRINGING IT TO LIFE (The Object) ---

# 1. Create a specific wizard (An 'Instance')
my_wizard = Wizard("Gandalf", "Grey")

# 2. Access the attributes (Descriptions)
print(f"This wizard's name is: {my_wizard.name}")

# 3. Tell the wizard to do something (Call the Method)
my_wizard.cast_spell()

# CHALLENGE: Can you create a second wizard with a different name below?
# your_wizard = Wizard("Merlin", "Blue")
# your_wizard.cast_spell()
