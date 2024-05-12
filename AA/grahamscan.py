import math

def polar_angles(points):
    x1, y1 = points
    angle_radian = math.atan2(y1,x1)
    return math.degrees(angle_radian)

def calculate_crossproduct(prev, curr, next):
    x1, y1 = prev
    x2, y2 = curr
    x3, y3 = next

    crossproduct = (x2-x1)*(y3-y2) - (y2-y1)*(x3-x2)
    return crossproduct


def grahamscan(input_points):
    if len(input_points) < 3:
        return []
    
    sorted_points = sorted(input_points, key=polar_angles)
    stack = [sorted_points[0], sorted_points[1]]

    for i in range(2, len(sorted_points)):
        while len(stack) > 1 and calculate_crossproduct(stack[-2], stack[-1], sorted_points[i]) < 0:
            stack.pop()
        stack.append(sorted_points[i])
    
    return stack


input_points = [(0,0), (1,1), (2,2), (3,3), (4,4), (1,2), (3,1), (0,3)]
convexhull = grahamscan(input_points)
convexhull = sorted(convexhull, key=polar_angles)
print(f'Convex Hull: {convexhull}')