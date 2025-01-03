import pandas as pd
import sys
sys.path.append(r"D:\UPG_Machine_Learning\Kaggle_Projects\HeartCheck-Predicting-Cardiovascular-Risks-with-MapReduce")
from mrjob_scripts.average_cholesterol import AverageCholesterol
from io import StringIO
from mrjob.job import MRJob

# Prepare input CSV file path
input_file = r"D:\UPG_Machine_Learning\Kaggle_Projects\HeartCheck-Predicting-Cardiovascular-Risks-with-MapReduce\preprocessed_heart_disease_dataset.csv"

# Initialize the MRJob
mr_job = AverageCholesterol(args=[input_file])

# Run the MRJob and capture output
results = []
output_buffer = StringIO()
with mr_job.make_runner() as runner:
    runner.run()
    for raw_line in runner.cat_output():
        #key, value =  mr_job.parse_output(raw_line.decode('utf-8').split('\t')
        #results.append((key, value))
        results.append(raw_line.decode('utf-8').strip('\t'))

# Initialize an empty list to store the processed results
processed_results = []

for item in results:
    if item:  # Check if the item is not an empty string
        key, value = item.strip().split('\t')
        processed_results.extend([int(key), float(value)])


# Convert the list into a DataFrame
df = pd.DataFrame(
    [processed_results[i:i+2] for i in range(0, len(processed_results), 2)],
    columns=["HeartDisease", "AverageCholesterol"]
)

print(df.to_string(index=False))

# Save to a CSV or visualize (optional)
#df.to_csv("average_cholesterol_output.csv", index=False)


# Bar plot visualization
df['HeartDisease'] = df['HeartDisease'].map({0: 'No Disease', 1: 'Heart Disease'})
cmap = get_cmap('tab10')  # Use the 'tab10' colormap
colors = [cmap(i) for i in range(len(df))]  # Assign different colors to each bar

plt.figure(figsize=(6, 4))
bars = plt.bar(df['HeartDisease'], df['AverageCholesterol'], color=colors)

# Add value labels on top of the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height,
             f'{height:.1f}', ha='center', va='bottom')

plt.xlabel('Condition')
plt.ylabel('Average Cholesterol Level')
plt.title('Average Cholesterol Levels for Heart Disease Conditions')
plt.tight_layout()
plt.show()

