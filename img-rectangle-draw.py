import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

im = Image.open('WIN_20221224_19_32_49_Pro.jpg')

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(im)

print("for defining 4 seats:")


colors = ['r', 'b', 'g', 'y']
for i in range(1,5):
    print()
    print("seat"+str(i))
    input1 = str(input("enter first point in x,y format (upper left):"))
    input2 = str(input("enter width and length:"))

    inputs1 = input1.split(",")
    inputs2 = input2.split(",")

    first_x, first_y = int(inputs1[0]), int(inputs1[1])

    # Create a Rectangle patch
    rect = patches.Rectangle((first_x, first_y), int(inputs2[0]), int(inputs2[1]), linewidth=1, edgecolor=colors[i-1], facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)


print("image with 4 seats drawn:")
plt.show()