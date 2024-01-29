# Import the NumPy library and alias it as np
import numpy as np

# Create two 1D NumPy arrays, arr1 and arr2
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Calculate the cross product between arr1 and arr2 using np.cross()
result = np.cross(arr1, arr2)

# Print the result
print(result)

# Use Cases for Cross Product:
# Determining Orthogonality: One of the primary uses of the cross product is to check if two vectors are orthogonal (perpendicular) to each other. If the cross product of two vectors is zero, it means they are orthogonal.
# Calculating Surface Normals: In computer graphics and 3D modeling, the cross product is used to calculate surface normals. Given two edge vectors of a polygon, the cross product provides a vector perpendicular to the polygon's surface, which is important for shading and rendering.
# Torque and Angular Momentum: In physics and engineering, the cross product is used to calculate torque and angular momentum. For example, when a force is applied to an object at a distance from a point, the torque produced can be calculated using the cross product of the force vector and the position vector.
# Magnetic Fields: In electromagnetism, the cross product is used to determine the magnetic field created by a current-carrying wire. The direction of the magnetic field lines is given by the cross product of the current vector and the vector connecting the point of interest to the wire.
# Rotation: In 3D computer graphics and robotics, the cross product can be used to calculate the axis of rotation when performing rotations in 3D space. It's crucial for controlling the orientation of objects.
# Angular Velocity: In rigid body dynamics, the cross product is used to calculate angular velocity when an object is rotating in 3D space.
