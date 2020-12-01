import argparse
import functions
import time

parser = argparse.ArgumentParser()

#On ajoute le cas path pour spécifier le chémin vers le fichier entrant
parser.add_argument("input", help="specifies the path to file to be compress", type=str)

#On ajoute le cas path pour spécifier le chémin vers le fichier entrant
parser.add_argument("output", help="specifies the path to file resulting in compression", type=str)

#On ajoute le cas path pour spécifier le chémin vers le fichier entrant
parser.add_argument("-d", "--decompress", help="specifies the path to file resulting in compression", action="store_true")



args = parser.parse_args()

if args.decompress:
    #Case decompression
    table_occurence = functions.read_occurence_table(args.input,)
    tree = functions.build_tree(table_occurence)
    #print(table_occurence)
    compressed = functions.read_compressed_text(args.input)

    text = functions.decompress(tree, compressed)
    functions.save_data_in(text, args.output)

else:
    #Case compression

    begin = time.time()

    file_in = open(args.input, "r")

    table = functions.make_table(args.input,)
    functions.save_data_in(table, args.output)
    a = functions.build_tree(table)
    encoding_table =  a.encoding_table({})

    functions.compress(args.input, args.output, encoding_table)

    end = time.time()
    print("Ratio : {} %".format( int(functions.size_of(args.output)/functions.size_of(args.input) * 100 )))
    print("Operation Time : {}".format(end - begin))


