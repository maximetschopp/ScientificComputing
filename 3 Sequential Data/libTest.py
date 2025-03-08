import numpy as np
import lib as customLibrary

print(customLibrary.filter(('', 1, 2, ' ', 1.0, 2.0), ['', ' ']))

print(customLibrary.find([1, 2, 3, 2, 1], 2))

print(customLibrary.common((1, 2, 3, 4), [6,4,2]))


filtered = customLibrary.filter(np.array([3, 8, 8, 3, 5, 4, 4, 9, 5, 4, 10]), [9])
print(f"Test 1: {[int(x) for x in filtered ]}")

print(f"Test 2: {customLibrary.find((4, 7, 10, 8, 9, 10, 6, 9, 4, 3, 9), 9)}")
print(f"Test 3: {customLibrary.find([3.2, 6.6, 0.7, 8.3, 3.6, 9.3, 2.9, 6.6, 1.3, 9.8], 6.6)}")
print(f"Test 4: {customLibrary.common([4, 7, 10, 8, 9, 10, 6, 9, 4, 3, 9], [3, 8, 8, 3, 5, 4, 4, 9, 5, 4, 10])}")


a = [' ', ' ', 99, 75, 28, 43, 68, 29, 97, 51, 76, 93, 55, 90, 64, 95, 12, 32, 50, ' ', 53, 31, 21]
b = [72, ' ', 53, 67, 44, 93, 96, 38, 46, 51, 78, 65, ' ', 47, 18, 91, 87, 90, 71, ' ', 97, 61, 19]

largest_common = max(customLibrary.common(customLibrary.filter(a, [' ']), customLibrary.filter(b, [' '])))

print(f"Test 5: LCM {largest_common}. At index {customLibrary.find(a, largest_common)} in a and {customLibrary.find(b, largest_common)} in b")