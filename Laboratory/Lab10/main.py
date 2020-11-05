"""
Testing file for lab 10
"""
import random as rn
from store import * #change this before finishing


rn.seed(9468523)


if __name__ == "__main__":
    ### dummy test values ###
    items = [Item("Bananas",.50,6), Item("Soup",1.00,10), Item("Onion",1.75,1), Item("Coke",1.75,12), Item("Doritos",3.50,1), Item("MountainDew",2.00,2), Item("Chocolate",12.99,1)]
    
    people = [Person("Larry",rn.randint(10000,99999),1000000000000000), Person("Nick",rn.randint(10000,99999),1), Person("Brady",rn.randint(10000,99999),100), Person("Joe Mama",rn.randint(10000,99999),100)]

    store = "Kroger"
    receipts = [Receipt(x, store) for x in people]

    ########################################################################
    # Testing Item
    ########################################################################

    print("~"*60)
    print("testing Item")
    print("testing showInfo()")
    expectedOutput = ['Item name: Bananas \nItemAmount: 0.5', 'Item name: Soup \nItemAmount: 1.0', 'Item name: Onion \nItemAmount: 1.75', 'Item name: Coke \nItemAmount: 1.75', 'Item name: Doritos \nItemAmount: 3.5', 'Item name: MountainDew \nItemAmount: 2.0', 'Item name: Chocolate \nItemAmount: 12.99']
    yourOutput = [item.showInfo() for item in items]
    print()
    print("\tExpected Output")
    for out in expectedOutput:
        print(out)
    print()
    print("\tYour output")
    for out in yourOutput:
        print(out)
        

    

    ########################################################################
    # Testing Person
    ########################################################################

    print("~"*60)
    print("Testing Person")
    print("Testing increaseBudget()")
    increseValues = [rn.randint(234,54622) for _ in range(4)]
    expectedOutput = [1000000000013897, 50264, 26838, 15647]
    yourOutput = [people[i].increaseBudget(increseValues[i]) for i in range(4)]
    print()
    print("Expected Output")
    for out in expectedOutput:
        print(out)
    print()
    print("Your output")
    for out in yourOutput:
        print(out)
    print()
    print("Testing donateEverythingAndBeHomeless")
    expectedOutput = [0,0,0,0]
    yourOutput = [peep.donateEverythingAndBeHomeless() for peep in people]
    print()
    print("\tExpected output")
    for out in expectedOutput:
        print(out)
    print()
    print("\tYour output")
    for out in yourOutput:
        print(out)
    

    ########################################################################
    # Testing Reciept
    ########################################################################
    print("~" * 60)
    print("Testing Reciept class")

    print("Testing addItem")
    expectedOutput = ["Item name: Bananas\nItemAmount: 0.5","Item name: Soup\nItemAmount: 1.0",
                      "Item name: Onion\nItemAmount: 1.75","Item name: Coke\nItemAmount: 1.75"]
    yourOutput = [receipts[i].addItem(items[i]) for i in range(4)]
    print()
    print("\tExpected Output")
    for out in expectedOutput:
        print(out)
    print()
    print("\tYour output")
    for out in yourOutput:
        print(out)
    print()
    print("Testing purchase")
    expectedOutput = [3.0, 10.0, 1.75, 21.0]
    yourOutput = [rec.purchase() for rec in receipts]
    print()
    print("\tExpected output")
    for out in expectedOutput:
        print(out)
    print()
    print("\tYour output")
    for out in yourOutput:
        print(out)
    print()
    print("testing __str__")
    expectedOutput = ['\t\tReceipt \n 12090... Larry\nBananas...0.5\n3.0', '\t\tReceipt \n 95618... Nick\nSoup...1.0\n10.0', '\t\tReceipt \n 58385... Brady\nOnion...1.75\n1.75', '\t\tReceipt \n 58839... Joe Mama\nCoke...1.75\n21.0']
    yourOutput = [str(rec) for rec in receipts]
    print("\tExpected Output")
    for out in expectedOutput:
        print(out)
    print()
    print("\tYour output")
    for out in yourOutput:
        print(out)

