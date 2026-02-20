# learning difference array
def difference_array(n, L, R):

    # Declaration of a difference array
    diff = [0] * (n + 2)
    
    # Define the range using a difference array
    diff[L] += 1
    diff[R + 1] -= 1 # Stop adding AFTER R which means it INCLUDES R

    arr = [0] * (n + 1) # Create the final array
    curr = 0

    return arr[1:] # Because L should be >= 1, the result is to simplfy and ensure at L = 1, diff[1] = 1, diff[0] no value 
    