import json, sys
from budget import *
from datetime import datetime

budget = {}
        
budget_raw = {
        "Bills":[
                {"Rent":[365, 0]},
                {"WiFi":[26, 0]}
                ],
        "Personal":[
                {"Self":[100, 60]},
                {"Groceries":[150, 57]}
                ]
}

printBudget(openBudget())

def addExpense(category, budget):
    
    writeBudget(budget)
while True:
    budget = openBudget()

    stdin = versionless_input("Enter a command: ") #uses a function that checks py version to call the built-in input function
    
    if stdin == "exit" or stdin == "e":
        print("Goodbye")
        
        break
    elif stdin == "save":
        writeBudget(budget_raw)
    elif stdin == '-ap' or stdin == "-aa":
        alterExpense(budget, stdin)
    elif stdin == "-add":
        createNewExpense(budget)
    elif stdin == "-p":
        printBudget(budget)
    elif stdin == "-v":
        fetchPythonVersion("list")
        
	
closePy()
