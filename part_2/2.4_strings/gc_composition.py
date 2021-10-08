genome = input().lower()

gc_count = 0
total = 0
for char in genome:
    if char in ('g', 'c'):
        gc_count += 1
    total += 1

print( gc_count / total * 100)
