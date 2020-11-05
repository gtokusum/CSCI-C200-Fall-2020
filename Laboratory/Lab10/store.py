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
        self.name = itemName
        self.amount = typeAmount
        self.quantity = quantity
        

    def showInfo(self):
        """
        RETURN the item information
        so it is displayed as such:
        Item name: name
        Item amount: amount
        """

        return 'Item name: {} \nItem Amount: {}'.format(self.name,self.amount)

    def __str__(self):
        """
        Present the information from `showInfo` by it a string
        output: same as showInfo
        """
        return 'Item name: {} \nItem Amount: {}'.format(self.name,self.amount)

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
        self.name = name
        self.ID = transactionID
        self.bank = bankAmount

    
    ### GETTERS and SETTERS ###
    def getName(self):
        """
        Returns the name of the person
        """
        return self.name

        
    def getTransactionID(self):
        """
        Returns the transaction identifier
        """
        return self.TransactionID

    def getBankAmount(self):
        """
        Returns the amount in the account
        """
        return self.bank

    def setBankAmount(self,newAmount):
        """
        sets the bankAmount to newAmoutn
        """
        self.bank = newAmount
    ### USEFUL METHODS ###
    def increaseBudget(self, amount):
        """
        increase how much you are willing to spend!
        output: the updated bankAmount value
        """
        self.bank += amount
        return self.bank
    def donateEverythingAndBeHomeless(self):
        """
        This will set the bankAmount to zero
        output: the updated bank amount
        """
        self.bank = 0
        return self.bank
    def __str__(self):
        """
        Returns a string representing the Person
        Expected:
        Person - {name} ({transaction ID})
        Example:
        Person - George Fred (100010)
        """
        return "Person - {} ({})".format(self.name,self.ID)

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
        self.person = person
        self.store = store
    
    def addItem(self, item):
        """
        add an item to the receipt--must be an object for item param
        output: item formatted as a string
        """
        self.item = []
        self.item.append(item)
        # print(self.item)
        for i in self.item:
            return i

    def purchase(self):
        """
        A method that returns the total cost of the items from the receipt account
        output: value of total
        """
        for i in self.item:
            return i
        
    def removeItem(self,item):
        """
        given an item name delete that account
        output: item formated as a string
        """
        self.person.pop(item)
        return str(item)

    def editItem(self, index, name, amount, quantity):
        """
        given an index, edit the item attributes 
        if any value is none do not edit the attribute
        attributes that are not being changed should be none
        output: editted item as a string
        """
        
        pass
    def __str__(self):
        """
        This will print the receipt
        output: object as a string
        \t\tReceipt \n transactionID ... person name \nitem name ... item amount \n (looped for all items)\ntotal cost
        """
        return "\t\tReceipt \n {} ... {} \n{} ... {}\n".format(Person.self.ID,Person.self.name, Item.self.item,Item.self.amount)
        

if __name__ == "__main__":
   """
   
   """
   print("You need to run `main.py`")