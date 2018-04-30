"""module multipli contenant la fonction table"""
def table_par(nb,min=1,max=9):
    while min<=max:
        print(min , "*", nb, "=", min * nb)
        min+=1
