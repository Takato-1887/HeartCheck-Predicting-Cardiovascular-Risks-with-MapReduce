import sys

current_key = None
total_cholesterol = 0
count = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    value = float(value)
    if current_key and key != current_key:
        avg_cholesterol = total_cholesterol / count
        print(f"{current_key}\t{avg_cholesterol}")
        total_cholesterol = 0
        count = 0
    current_key = key
    total_cholesterol += value
    count += 1

if current_key:
    avg_cholesterol = total_cholesterol / count
    print(f"{current_key}\t{avg_cholesterol}")
