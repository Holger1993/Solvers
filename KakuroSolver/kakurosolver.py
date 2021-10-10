

def solve(acr, down):
    emptyKakuro = acr
    for i in range(len(acr)):
        for j in range(len(acr[0])):
            if acr[i][j] == '0' and down[i][j] == '0':
                emptyKakuro[i][j] = 0
            else:
                emptyKakuro[i][j] = '.'
    return emptyKakuro
