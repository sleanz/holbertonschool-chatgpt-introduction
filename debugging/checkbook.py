#!/usr/bin/env python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0
        
    def deposit(self, amount):
        # Validate amount is positive
        if amount <= 0:
            print("Erreur: Le montant du dépôt doit être positif.")
            return
            
        self.balance += amount
        print("Dépôt de {:.2f}€".format(amount))
        print("Solde actuel: {:.2f}€".format(self.balance))
        
    def withdraw(self, amount):
        # Validate amount is positive
        if amount <= 0:
            print("Erreur: Le montant du retrait doit être positif.")
            return
            
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Retrait de {:.2f}€".format(amount))
            print("Solde actuel: {:.2f}€".format(self.balance))
            
    def get_balance(self):
        print("Solde actuel: {:.2f}€".format(self.balance))

def main():
    cb = Checkbook()
    print("Bienvenue dans votre carnet de chèques!")
    
    while True:
        action = input("Que souhaitez-vous faire ? (deposer, retirer, solde, quitter): ")
        
        if action.lower() == 'quitter':
            print("Merci d'avoir utilisé votre carnet de chèques. Au revoir!")
            break
            
        elif action.lower() == 'deposer':
            try:
                amount = float(input("Entrez le montant à déposer: "))
                cb.deposit(amount)
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide pour le montant du dépôt.")
                
        elif action.lower() == 'retirer':
            try:
                amount = float(input("Entrez le montant à retirer: "))
                cb.withdraw(amount)
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide pour le montant du retrait.")
                
        elif action.lower() == 'solde':
            cb.get_balance()
            
        else:
            print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
