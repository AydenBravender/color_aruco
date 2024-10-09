num = 12142432434
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

base5 = 0
if num == 0:
    base5 = 0

if num < 95367431640624 and num >= 0:
    base5_digits = []
    
    # Convert number to base 5
    while num > 0:
        remainder = num % 5
        base5_digits.append(remainder)  # Store as integer
        num = num // 5
    
    base5_digits.reverse()
    
    # Pad the list to 20 digits with 0s
    while len(base5_digits) < 20:
        base5_digits.insert(0, 0)

else:
    raise ValueError("Number is too large for base 5 conversion within the allowed range")


# Split the list into 4 lists of 5 elements each
split_lists = [base5_digits[i:i+5] for i in range(0, len(base5_digits), 5)]

# Count the number of even elements in each list
even_counts = [sum(1 for num1 in sublist if num1 % 2 == 0) for sublist in split_lists]

for i in range(len(even_counts) - 1, -1, -1):
    if even_counts[i] % 2 == 0:
        base5_digits.insert(i * 5 + 5, 0)
    elif even_counts[i] % 2 == 1:
        base5_digits.insert(i * 5 + 5, 1)

base5_digits.insert(0, 5)
array = np.zeros((7, 7))
print(base5_digits)

for row in range(1, 6):  # Rows 1 to 5
    for col in range(1, 6):  # Columns 1 to 5
        array[row, col] = base5_digits[(row - 1) * 5 + (col - 1)]  # Calculate the index for flat list

# Create a custom colormap
cmap = colors.ListedColormap(['black', 'white', 'green', 'red', 'blue', 'yellow'])

# Define the bounds for each color
bounds = [0, 1, 2, 3, 4, 5, 6]  # Specify boundaries for each color

# Normalize the array values so each one corresponds to a specific color
norm = colors.BoundaryNorm(bounds, cmap.N)

# Create the plot
plt.imshow(array, cmap=cmap, norm=norm)

# Remove axis labels
plt.axis('off')

# Save the image as a PNG file
plt.savefig('custom_colored_array.png', bbox_inches='tight', pad_inches=0)

# Show the image (optional)
plt.show()