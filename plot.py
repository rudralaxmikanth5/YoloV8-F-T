import matplotlib.pyplot as plt

with open('data.txt', 'r') as file:
    lines = file.readlines()


x_centers = []
y_centers = []

for line in lines:
    parts = line.split()  # Split line by whitespace
    class_label = parts[0]
    x_center = float(parts[1])
    y_center = float(parts[2])
    x_centers.append(x_center)
    y_centers.append(y_center)


plt.scatter(x_centers, y_centers, color='red', marker='o', label='Detections')
plt.xlabel('X Center')
plt.ylabel('Y Center')
plt.title('Center of Detections')
plt.legend()
plt.grid(True)

# Save the image
plt.savefig('detections_plot.png')

# Display the plot
plt.show()
