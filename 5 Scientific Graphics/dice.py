import numpy as np
import matplotlib.pyplot as plt


with open("/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/5 Scientific Graphics/dice.txt", 'r') as f:
    data = f.readlines()

    # Plot 1
    numEntries = 100
    table1 = []
    for line in data[:numEntries] :
        table1.append(sum(map(int, line.split())))
    xRange = np.linspace(1, numEntries, numEntries)
    plt.plot(xRange, table1, label='Sum of dice rolls', linestyle='', marker='o', color='b')
    plt.xlabel('Dice roll (#)')
    plt.ylabel('Sum')
    plt.title('Sum of dice rolls')
    plt.show(block=False)

    # Plot 2 Distribution of 10000 dice rolls
    sums = [sum(map(int, line.split())) for line in data]
    bins = np.arange(3, 19) # 3 to 18
    counts, edges = np.histogram(sums, bins)
    bin_centers = (edges[:-1] + edges[1:]) / 2 # array of center points to plot errorbars
    errors = np.sqrt(counts)

    plt.figure(figsize=(10, 5))
    plt.hist(sums, bins=bins, alpha=0.6, edgecolor='black', label='Histogram')
    plt.errorbar(bin_centers, counts, yerr=errors, fmt='o', capsize=4, label='Error bars')
    plt.xticks(range(2, 19))
    plt.xlabel("Sum of 3 dice")
    plt.ylabel("Count")
    plt.title("Distribution of Dice Sums (Histogram + Error Bars)")
    plt.legend()
    plt.grid(True)
    plt.show()