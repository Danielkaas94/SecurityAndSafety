import matplotlib.pyplot as plt
from colorama import Fore

# Some sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plotting the data
plt.plot(x, y)

# Displaying the plot
plt.show()
print(Fore.GREEN + "Plot 1 📈")


# Adding labels and title
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')

# Displaying the plot
# plt.show()
print(Fore.CYAN + "Plot 2 📈")



# Customizing line style and color
plt.plot(x, y, linestyle='--', marker='o', color='r')  # Dashed line with red color and circular markers
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')

# Displaying the plot
plt.show()
print(Fore.RED + "Plot 3 📈")



# Plotting multiple lines
plt.plot(x, y, label='Line 1')
plt.plot(x, [val*2 for val in y], label='Line 2')  # Plotting y values multiplied by 2
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines Plot')
plt.legend()  # Adding legend

# Displaying the plot
plt.show()
print(Fore.BLUE + "Plot 4 📈")
