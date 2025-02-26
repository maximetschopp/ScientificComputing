from tqdm import tqdm # progress bar
import time

def sums_of_cubes(max_index):
    valid_solutions = []
    i = 0
    for i in tqdm(range(max_index), desc="Searching for solutions"): # just a basic for loop but with fancy progress bar wrapping tqdm logic
        d_cubed = i**3
        for j in range(1, i+1):
            j_cubed = j**3
            for k in range(1, j+1):
                k_cubed = k**3
                j_k_sum = j_cubed + k_cubed
                if j_k_sum > d_cubed:
                    break
                for m in range (1, k+1):
                    if j_k_sum + m**3 == d_cubed:
                        valid_solutions.append([j,k,m,i])
    return valid_solutions

with open("/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/1 Number and Text/output.csv", 'w') as file:
    file.truncate(0) # clear the file
    max_index = 300
    times_start = time.time()
    output = sums_of_cubes(max_index)
    time_end = time.time()
    if not output:
        print("Unsuccessful")
    else:
        print("-------------------------------------------")
        print(f"Success || found {len(output)} solutions for max_index {max_index}")
        print("-------------------------------------------")

    # write to the csv file.
    file.write("a, b, c, d\n")
    for solution in output:
        file.write(", ".join(map(str, solution)) + "\n")

    print(f"Time taken: {time_end - times_start} seconds\n")