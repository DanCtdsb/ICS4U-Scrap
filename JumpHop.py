def JumpHop(start, end, jump):
    if start >= end:
        return 0
    
    distance = abs(end - start)
    q = distance // jump
    r = distance % jump
    if r == 0:
        return q
    else:
        return min(distance, q + 1 + (jump - r))
print(JumpHop(0, 16, 27))
