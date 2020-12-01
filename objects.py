




class Tree(object):
    """
    docstring
    """
    def __init__(self, weight, char):
        """
        docstring
        """
        self.weight = weight 
        self.char = char
        self.right_child = 0
        self.left_child = 0

    def make_right(self, tree):
        """
        docstring
        Methode qui permet de faire le fils droit d'un arbre
        """
        self.right_child = tree

    def __gt__(self, other):
        """
        docstring
        """
        return self.weight>other.weight

    def __lt__(self, other):
        """
        docstring
        """
        return self.weight<other.weight

    def __eq__(self, other):
        """
        docstringand
        """
        return self.weight==other.weight
        
    def make_left(self, tree):
        """
        docstring
        Methode qui permet de faire le fils droit d'un arbre
        """
        self.left_child = tree

    def encoding_table(self, table, code = None, ):
        """
        docstring
        Methode qui descend de façon recursive pour  atteindre les feuilles de l'arbre et ainsi formé une table de codage 
        """
        t1 = {}
        t2 = {}
        if code == None :
            t1 =  self.right_child.encoding_table(table, code = "0") 
            t2 =  self.left_child.encoding_table(table, code = "1")
        else:

            if isinstance(self.right_child, Tree) : 
                t1 = self.right_child.encoding_table(table, code + "0")
            if isinstance(self.left_child, Tree) : 
                t2 = self.left_child.encoding_table(table, code + "1") 
            if not isinstance(self.left_child, Tree) and  not isinstance(self.right_child, Tree):
                table[self.char] = code
                return table
        return {**t1, **t2}


    def __str__(self):
        """
        docstring
        """
        if isinstance( self.left_child , Tree)  and  isinstance(self.right_child, Tree):
            return " weight : {} \n char : {} \n left --> [ \n {} ] \n right --> [ \n {} ] ".format(self.weight, self.char, self.left_child, self.right_child)
        else : 
            return " [ weight : {}  char : {}  left --> [ None ]  right --> [ None ] ]".format(self.weight, self.char)


