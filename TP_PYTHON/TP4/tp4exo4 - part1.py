def most_frequent(lst):
    count_dict = {}
    
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_num = max(count_dict, key=count_dict.get)
    max_count = count_dict[max_num]
    
    print(f"Le nombre le plus frequent dans la liste est le : {max_num} ({max_count} x)")

liste_exemple = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]
most_frequent(liste_exemple)

