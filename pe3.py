import string
import datetime

def encode(input_text, shift):

    alphabet = list(string.ascii_lowercase)
    encoded_text = ""


    for letter in input_text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            encoded_text += alphabet[new_position]
        else:
        
            encoded_text += letter

    return alphabet, encoded_text


def decode(input_text, shift):

    result = encode(input_text, -shift)
    return result[1]


class BankAccount:

    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        if creation_date is None:
            creation_date = datetime.date.today()


        if type(creation_date) is not datetime.date:
            raise TypeError("creation_date must be a datetime.date.")

        if creation_date > datetime.date.today():
            raise Exception("The account creation date cannot be in the future.")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance


    def deposit(self, amount):
        if amount < 0:
            print("Negative deposits are not allowed.")
            return self.view_balance()

        self.balance += amount
        return self.view_balance()

   
    def withdraw(self, amount):
        if amount < 0:
            print("Negative withdrawals are not allowed.")
            return self.view_balance()

        self.balance -= amount
        return self.view_balance()

  
    def view_balance(self):
        print(f"Balance: ${self.balance:.2f}")
        return self.balance



class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount < 0:
            print("Negative withdrawals are not allowed.")
            return self.view_balance()

     
        account_age = (datetime.date.today() - self.creation_date).days

        if account_age < 180:
            print("The savings account must be at least 180 days old to withdraw.")
            return self.view_balance()


        if amount > self.balance:
            print("Insufficient balance for this withdrawal.")
            return self.view_balance()

    
        return super().withdraw(amount)


class CheckingAccount(BankAccount):

    def withdraw(self, amount):
        if amount < 0:
            print("Negative withdrawals are not allowed.")
            return self.view_balance()

     
        self.balance -= amount

      
        if self.balance < 0:
            self.balance -= 30

        return self.view_balance()