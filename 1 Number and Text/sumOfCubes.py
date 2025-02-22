from tqdm import tqdm #progress bar

def sums_of_cubes(max_index):
    valid_solutions = []
    i = 0
    for i in tqdm(range(max_index), desc="Searching for solutions"): # just a basic for loop but with fancy progress bar wrapping tqdm logic
        d_squared = i**3
        for j in range(0, i+1):
            for k in range(0, j+1):
                for m in range (0, k+1):
                    if j**3 + k**3 + m**3 == d_squared:
                        valid_solutions.append([j,k,m,i])
    return valid_solutions

with open("/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/1 Number and Text/output.csv", 'w') as file:
    file.truncate(0) # clear the file
    max_index = 300
    output = sums_of_cubes(max_index)
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