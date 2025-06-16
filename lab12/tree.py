from math import radians
from Tree.core import Tree
from PIL import Image

background_color = (200, 240, 250)
leaf_color = (254, 154, 0)
trunk_width = 30
base_trunk_color = (50, 40, 0)
small_branch_color = (125, 107, 30)
branch_gradient = (*base_trunk_color, *small_branch_color)

trunk_length = 200
first_branch_line = (0, 0, 0, -trunk_length)
scales_and_angles = [(0.5, radians(-30)), (0.5, radians(30))]
age = 4

tree = Tree(pos=first_branch_line, branches=scales_and_angles, sigma=(0.2, 0.2))
tree.grow(age)
tree.move_in_rectangle()
image = Image.new("RGB", tree.get_size(), background_color)
tree.draw_on(image, branch_gradient, leaf_color, trunk_width)
image.show()