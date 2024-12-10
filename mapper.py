import sys

for line in sys.stdin:
    data = line.strip().split(',')
    cholesterol = data[4]  # Cholesterol is the fifth column
    heart_disease = data[11]  # Heart disease diagnosis is the twelfth column
    if heart_disease == '1':
        print(f"disease\t{cholesterol}")
    else:
        print(f"no_disease\t{cholesterol}")
