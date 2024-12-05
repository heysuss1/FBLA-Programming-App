import time, os, random  
clear = lambda: os.system('cls')


#Creates a class to keep track of all user attributes
class User:
    def __init__(self, name):
        self.name = name
    def urmom(self, mom):
        self.mom = mom
    def set_occupation(self):
        pass
    def set_current_job(self, job):
        self.job = job

"""
Params: Text to be displayed by user
Output
"""
def stagger_text(text: str):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.1)
    print('')

companies = ["McDonalds", "Publix", "IBM"]
company_job = {"McDonalds": "cashier", "Publix" : "stocker", "IBM": "data entry clerk"}
# jobs_degree = {}

def show_menu():
    pass

print("Welcome, aspiring entrepreneur")

time.sleep(1)
#asks user for name and changes the first letter to uppercase
name = input("Please enter your name to begin: ")
clear()
name = name.replace(f"{name[0]}", f"{name[0].upper()}", 1)


player = User(name)
player.set_current_job(random.choice(companies)) 

stagger_text(f"Time: 9:00 AM \n\nLocation: {player.job}")

time.sleep(2)

clear()

print(f"You are a {company_job[player.job]} at {player.job}")
time.sleep(1.5)
print("You have spent 5 long, unfulfilling years working at your job")
time.sleep(1.5)
print("As a result, you decide to quit and start your own business")
time.sleep(2)

clear(  )
product_type = input("")
