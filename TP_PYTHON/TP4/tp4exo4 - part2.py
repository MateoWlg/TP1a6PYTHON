def most_frequent(lst):
    max_num = max(set(lst), key=lst.count)
    max_count = lst.count(max_num)
    
    print(f"Le nombre le plus frequent dans la liste est le : {max_num} ({max_count} x)")

liste_exemple = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]
most_frequent(liste_exemple)

