import math

points = [(1, 2), (4, 6), (7, 8), (3, 5)]
distances = []
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


for i in range(len(points)-1):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)

print("En küçük mesafe:" , min_distance)
