from task import intersection, union

print("--- Пример из задания ---")
print("Intersection:", intersection(1, 2, 3, 0, 2, 3, 5, 1))
print("Union:", union(1, 2, 3, 0, 2, 3, 5, 1))

print("\n--- Пример 1 (не пересекаются) ---")
print("Intersection:", intersection(0, 5, 2, 0, 3, 5, 5, 0))
print("Union:", union(0, 5, 2, 0, 3, 5, 5, 0))

print("\n--- Пример 2 (один внутри другого) ---")
print("Intersection:", intersection(0, 10, 10, 0, 2, 8, 4, 6)) 
print("Union:", union(0, 10, 10, 0, 2, 8, 4, 6))