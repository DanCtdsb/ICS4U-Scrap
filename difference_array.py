# learning difference array
def difference_array(n, L, R):

    # Declaration of a difference array
    diff = [0] * (n + 2)
    
    # Define the range using a difference array
    diff[L] += 1
    diff[R + 1] -= 1 # Stop adding AFTER R which means it INCLUDES R