import math

points = [(1, 2), (3, 5), (6, 7), (9, 12), (11, 15)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance:.2f}")
