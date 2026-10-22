def is_valid_move(board, i, j):
    if 0 <= i < len(board) and 0 <= j < len(board):
        return True
    return False
#verificam daca o mutare este valida

def count_visitable_cells(board):
    return sum(1 for row in board for cell in row if cell != 0 and cell != 2)
#numaram cate celule sunt vizitabile

def backtracking(board, i, j, visited_cells, end_i, end_j, visitable_cells):

    if visited_cells == visitable_cells and i == end_i and j == end_j:
        return True
    #daca am ajuns la destinatie si am vizitat toate celulele vizitabile, atunci am gasit drumul

    if is_valid_move(board, i, j):
        board[i][j] = 0
        #marcam noua celula ca fiind vizitata
        moves = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        #pentru a nu face verificari suplimentare pentru mutarile de doua patratele la nebun, deoarece
        #aceastea ar fi posibile doar daca patratica de pe diagonala la o casuta distanta este neocupata,
        #am ales sa reduc problema la a putea muta nebunul doar o patratica pe diagonala
        new_moves = []
        for move in moves:
            i_next = i + move[0]
            j_next = j + move[1]
            new_moves.append((i_next, j_next))
        #generam toate mutarile posibile

        for move in new_moves:
            i_next = move[0]
            j_next = move[1]
            if is_valid_move(board, i_next, j_next) and board[i_next][j_next] in {1, 2, 3}:
                copy_board = [row[:] for row in board]
                if backtracking(copy_board, i_next, j_next, visited_cells + 1, end_i, end_j, visitable_cells):
                    return True
        #apelam recursiv functia pentru fiecare mutare posibila valida si incrementam numarul de celule vizitate

    return False

board = [
    [0, 1, 0, 0],
    [1, 0, 0, 3],
    [0, 1, 2, 0],
    [1, 0, 0, 0]
]

start_i, start_j = 2, 2
end_i, end_j = 1, 3


visitable_cells = count_visitable_cells(board)
visited_cells = 0

result = backtracking(board, start_i, start_j, visited_cells, end_i, end_j, visitable_cells)
if result:
    print("Drum gasit!")
else:
    print("Drumul nu a fost gasit!")


#Complexitate algoritm: O(12^n)