import queue
import objects
import ast


def read_compressed_text(path):
    """
    docstring
    Fonctions qui permet de lire le texte compressé depuis le fichier
    """
    with open(path, 'r') as target:
        text = target.read()
        i = 0
        while True :
            if i< (len(text)-1) and text[i] == "}" and (text[i+1] in "01" ):
                break
            i+=1
        return text[i+1:]
        
    raise Exception("Impossible de trouver le texte compressé !!!")

def decompress(tree, compressed):
    """
    docstring
    Fonction qui permet de  decompresser un fichier 
    """
    text = ""
    root = tree
    for x in compressed:
        if not isinstance(tree.right_child, objects.Tree) and not isinstance(tree.left_child, objects.Tree):
            text+=tree.char
            tree = root
        if x == "1":
            tree = tree.left_child
        else:
            tree = tree.right_child

    return text


def compress(input_file, output_file, encoding_table):
    """
    docstring
    Fonction qui permet de compresser le texte avec la methode de Huffman

    """
    with open(input_file, "r") as target:
        source = target.read()       
    dest = ""
    for x in source : 
        dest+=encoding_table[x]
    with open(output_file, "a") as target:
        target.write(dest)

def build_tree(table):
    """
    docstring
    Fonction qui permet de créer l'arbre de Huffman avec 
    une descente à droite --> 0 et une descente à gauche qui représente 1
    """
    file = queue.PriorityQueue()

    for k,v in table.items() : 
        file.put(objects.Tree(v, k))

    while True : 
        
        left =  file.get()
        right =  file.get()

        tree = objects.Tree(right.weight+ left.weight, left.char + right.char)
        tree.make_left(left)
        tree.make_right(right)


        if  file.empty(): 
            return tree
        file.put( tree)

        
def read_occurence_table(path):
    """
    docstring
    Fonction qui permet de lire la table d'occurence depuis un fichier compressé 
    """
    with open(path, 'r') as target:
        text = target.read()
        inter = ""
        
        for i in range(len(text)) :
            inter+=text[i]
            if i< (len(text)-1) and text[i] == "}" and (text[i+1] in "01" ):
                return ast.literal_eval(inter)
    raise Exception("Impossible de trouver la table de frequence !!!")


def save_data_in(table, path):
    """
    docstring
    Fonction qui permet de suavegarder une donnée dans un 
    fichier donné en paramètre
    """
    with  open(path, "w") as target:
        target.write(str(table))


def make_table(path):
    """
    docstring
    Fonction qui permet de créer la table de fréquence à d'un texte
    """
    text = ""
    with open(path, "r") as target:
        text = target.read()
    count = 0
    table = dict()
    for x in text:
        count+=1
        if x in table.keys():
            table[x]+=1
        else : 
            table[x]=1
    if count == 0 : 
        raise Exception("Aucun texte trouvé dans le fichier !")
    """for k, v in table.items() : 
        table[k] = v/count"""


    return table