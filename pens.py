

def pens_solution(pen_list):
    solution = pen_list[0]
    pens = []
    constraints = []
    for pen in pen_list:
        if len(pen) == 2:
            pens.append(pen)
        else:
            constraints.append(pen)
    for i in range(0, solution[2]):
        pens.sort(key=lambda x: x[1])
        for pen in pens:


            
            



print(pens_solution([(6, 3, 0), (1, 6), (2, 9), (3, 4), (2, 7), (3, 9), (1, 3)]))