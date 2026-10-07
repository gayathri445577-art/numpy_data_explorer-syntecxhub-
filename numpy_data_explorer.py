# Project 1 - NumPy Data Explorer

# 1. Import NumPy
import numpy as np

print("===== NumPy Data Explorer =====")


# 2. Array Creation
numbers = np.array([10, 20, 30, 40, 50])

print("\n--- Array Creation ---")
print("Array:", numbers)


# 3. Indexing
print("\n--- Indexing ---")
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])


# 4. Slicing
print("\n--- Slicing ---")
print("First three elements:", numbers[:3])
print("Elements from index 1 to 3:", numbers[1:4])


# 5. Mathematical Operations
print("\n--- Mathematical Operations ---")
print("Addition:", numbers + 10)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)
print("Division:", numbers / 2)


# 6. Statistical Operations
print("\n--- Statistical Operations ---")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Standard Deviation:", np.std(numbers))


# 7. Reshaping
print("\n--- Reshaping ---")

data = np.array([1, 2, 3, 4, 5, 6])

reshaped_data = data.reshape(2, 3)

print("Original array:", data)
print("Reshaped array:")
print(reshaped_data)


# 8. Broadcasting
print("\n--- Broadcasting ---")

marks = np.array([60, 70, 80, 90])

bonus = 5

new_marks = marks + bonus

print("Original marks:", marks)
print("Bonus:", bonus)
print("Marks after bonus:", new_marks)


# 9. Save NumPy Array
print("\n--- Saving Array ---")

np.save("numbers.npy", numbers)

print("Array saved successfully.")


# 10. Load NumPy Array
print("\n--- Loading Array ---")

loaded_numbers = np.load("numbers.npy")

print("Loaded array:", loaded_numbers)


# 11. NumPy Array vs Python List
print("\n--- NumPy vs Python List ---")

python_list = [10, 20, 30, 40, 50]
numpy_array = np.array([10, 20, 30, 40, 50])

print("Python List:", python_list)
print("NumPy Array:", numpy_array)

print("NumPy array multiplied by 2:", numpy_array * 2)


# 12. Array Information
print("\n--- Array Information ---")

print("Number of dimensions:", numbers.ndim)
print("Number of elements:", numbers.size)
print("Data type:", numbers.dtype)
print("Shape:", numbers.shape)


# 13. Conclusion
print("\n===== Project Completed =====")
print("We learned NumPy arrays, indexing, slicing,")
print("mathematical operations, statistics, reshaping,")
print("broadcasting, saving/loading, and NumPy vs lists.")