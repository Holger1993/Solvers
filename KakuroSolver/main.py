import kakurosolver as ks

def main():
    with open('Kakuros/kakuro1.txt') as f:
        lines = f.read().splitlines()
    f.close()
    across = []
    down = []
    acr = True
    for line in lines:
        if line == '':
            acr = False
            continue
        lin = line.split(',')
        row = []
        for l in lin:
            row.append(l)
        if acr:
            across.append(row)
        else:
            down.append(row)
    
    kakuro = ks.solve(across, down)
    for row in kakuro:
        print(row)

if __name__ == '__main__':
    main()