def JumpHop(start, end, jump):
    if start >= end:
        return 0
    
    distance = end - start
    return distance // jump + distance % jump
print(JumpHop(0, 9, 4))