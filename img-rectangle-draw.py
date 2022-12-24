import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

im = Image.open('C:/Users/USER/Pictures/Camera Roll/WIN_20221224_19_32_49_Pro.jpg')

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(im)

input1 = str(input(print("enter first point in x,y format (upper left):")))
input2 = str(input(print("enter width and length:")))


inputs1 = input1.split(",")
inputs2 = input2.split(",")


first_x, first_y = int(inputs1[0]), int(inputs1[1])





# Create a Rectangle patch
rect = patches.Rectangle((first_x, first_y), int(inputs2[0]), int(inputs2[1]), linewidth=1, edgecolor='r', facecolor='none')



# Add the patch to the Axes
ax.add_patch(rect)

plt.show()