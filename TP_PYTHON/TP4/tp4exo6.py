def tri_selection(tab):
    n = len(tab)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tab[j] < tab[i]:
                tab[i], tab[j] = tab[j], tab[i]
                print(tab)

tab = [5, 2, 4, 8, 1, 3]

print(tab)

tri_selection(tab)

