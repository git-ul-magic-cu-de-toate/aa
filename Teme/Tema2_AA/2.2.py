def find_cycle(A, n, cycle):
    for i in range(n):
        for j in range(n):
            for k in  range(n):
                if A[i][j] == 1 and A[j][k] == 1 and A[k][i] == 1:
                    cycle.append((i, j, k))
                    break
            if len(cycle) == 0:
                break
        if len(cycle) == 0:
            break
    for i in range(n):
        if i not in cycle:
            for j in range(len(cycle)):
                if A[cycle[j]][i] == 1 and A[i][cycle[(j + 1) % len(cycle)]] == 1:
                    first_part = cycle[:(j + 1)]
                    second_part = cycle[(j + 1):]
                    cycle = first_part + [i] + second_part
                    break
        

cycle = []
find_cycle(A, n, cycle)

#Complexitate algoritm: O(n^3)