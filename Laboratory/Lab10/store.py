"""
Going to the grocery store w/ OOP concepts

NOTE: You are allowed to use (or name) whatever instance variables you want, 
as the test code only calls functions
"""


class Item:
    """
    class that defines an individual bank account
    """

    def __init__(self, itemName, typeAmount, quantity):
        """
        constructor function

        You are given:
        - itemName: name of the item
        - typeAmount: Cost for an item
        - quantity: Amount in the store
        """

    def showInfo(self):
        """
        RETURN the item information
        so it is displayed as such:
        Item name: name
        Item amount: amount
        """

    def __str__(self):
        """
        Present the information from `showInfo` by it a string
        output: same as showInfo
        """
        return ""

class Person:
    """
    This will contain the name of the person, their transaction ID and how much money they have to spend
    """

    def __init__(self, name, transactionID, bankAmount):
        """
        constructor function

        You are given:
        - name: Name of the person
        - transactionID: an identifier for a transaction
        - bankAmount: Amount in the account
        """
    
    ### GETTERS and SETTERS ###
    def getName(self):
        """
        Returns the name of the person
        """

        
    def getTransactionID(self):
        """
        Returns the transaction identifier
        """


    def getBankAmount(self):
        """
        Returns the amount in the account
        """


    def setBankAmount(self,newAmount):
        """
        sets the bankAmount to newAmoutn
        """

    ### USEFUL METHODS ###
    def increaseBudget(self, amount):
        """
        increase how much you are willing to spend!
        output: the updated bankAmount value
        """

    def donateEverythingAndBeHomeless(self):
        """
        This will set the bankAmount to zero
        output: the updated bank amount
        """
    
    def __str__(self):
        """
        Returns a string representing the Person
        Expected:
        Person - {name} ({transaction ID})
        Example:
        Person - George Fred (100010)
        """
        return ""

class Receipt:
    """
    class that keeps track of all items being bought
    """
    def __init__(self, person, store):
        """
        constructor function

        You are given:
        - person: The person the receipt belongs to
        - store: the store the receipt is from

        You need to keep track of the stuff bought on the receipt. 

        You need to keep track of the transaction identifier that corresponds to a person
        """
    
    def addItem(self, item):
        """
        add an item to the receipt--must be an object for item param
        output: item formatted as a string
        """

    def purchase(self):
        """
        A method that returns the total cost of the items from the receipt account
        output: value of total
        """
        
    def removeItem(self,item):
        """
        given an item name delete that account
        output: item formated as a string
        """
        

    def editItem(self, index, name, amount, quantity):
        """
        given an index, edit the item attributes 
        if any value is none do not edit the attribute
        attributes that are not being changed should be none
        output: editted item as a string
        """

    def __str__(self):
        """
        This will print the receipt
        output: object as a string
        \t\tReceipt \n transactionID ... person name \nitem name ... item amount \n (looped for all items)\ntotal cost
        """
        return ""

if __name__ == "__main__":
   """
   
   """
   print("You need to run `main.py`")