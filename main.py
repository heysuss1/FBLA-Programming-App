import time, os, random
# from user import *

#creates a function to clear the console of text
clear = lambda: os.system('cls')

#Creates the class that keeps track of all user attributes
class User:
    def __init__(self, name):
        self.name = name
    def urmom(self, mom):
        self.mom = mom
    def set_occupation(self):
        pass
    def set_current_job(self, job):
        self.job = job

def stagger_text(text):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.1)
    print('')
jobs = ["McDonalds cashier", "Publix stocker"]
# jobs_degree = {}

print("Welcome, aspiring entrepreneur\n")

time.sleep(1)
#asks user for name and changes the first letter to uppercase
name = input("Please enter your name to begin: ")
10
name = name.replace(f"{name[0]}", f"{name[0].upper()}", 1)


player = User(name)
player.set_current_job(random.choice(jobs))



time.sleep(1)
clear()
