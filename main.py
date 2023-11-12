import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from graph import  Point
from vis_graph import VisGraph


# Define obstacles
polys = [[Point(0.0, 1.0), Point(3.0, 1.0), Point(3.0, 8.0), Point(1.5, 4.0)],
         [Point(4.0, 4.0), Point(7.0, 4.0), Point(8.5, 7), Point(10.2, 8.0), Point(5.5, 12.0)]]

# Build visibility graph
g = VisGraph()
g.build(polys)


# Find the shortest path
shortest_path = g.shortest_path(Point(1.5, 0.0), Point(9.4, 11.9))
print(shortest_path)
print(g.graph.edges)
# g.save("example_graph.graph")
# print('Saved visibility graph to file: {}'.format("example_graph.graph"))

# Extract x and y coordinates for obstacles
obstacle_coords = [[point.x, point.y] for poly in polys for point in poly]

# Extract x and y coordinates for the shortest path
path_coords = [[point.x, point.y] for point in shortest_path]

# Plot obstacles
fig, ax = plt.subplots()
for poly in polys:
    poly_coords = [[point.x, point.y] for point in poly]
    polygon = Polygon(poly_coords, edgecolor='black', facecolor='gray')
    ax.add_patch(polygon)

# Plot shortest path
path_line, = ax.plot(*zip(*path_coords), marker='o', color='blue', label='Shortest Path')

# Mark start and end points
ax.plot(path_coords[0][0], path_coords[0][1], marker='o', color='red', label='Start Point')
ax.plot(path_coords[-1][0], path_coords[-1][1], marker='o', color='green', label='End Point')

# Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

# Show the plot
plt.show()
