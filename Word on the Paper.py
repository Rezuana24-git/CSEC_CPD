t=int(input())
for cv in range(t):
    grid=[input() for ch in range(8)]
    word=""
    for i in range(8):
        for j in range(8):
            if grid[i][j] != '.':
                word+=grid[i][j]
                break
    print(word)
