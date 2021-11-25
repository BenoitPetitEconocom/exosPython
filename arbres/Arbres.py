# Exercice de création de structure en arbre

# Exercice de création de structure en arbre

# arbre binaire
class BinaryTree:
    def __init__(self, val = None):
        if val != None:
            self.val = val
        else:
            self.val = None
        self.leftNode = None
        self.rightNode = None
    
    def insertValue(self, value):
        if self.val:
            if value < self.val:
                if self.leftNode is None: self.leftNode = BinaryTree(value)
                else: self.leftNode.insertValue(value)
            if value > self.val:
                if self.rightNode is None: self.rightNode = BinaryTree(value)
                else: self.rightNode.insertValue(value)
        else: self.val = value
    # afficher l'arbre de gauche à droite (ordre crosisant)
    def printValues(self):
        if self.leftNode: self.leftNode.printValues()
        print(self.val)
        if self.rightNode: self.rightNode.printValues()
        