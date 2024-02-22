import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("sample-data.csv")

# Calculate the count of each unique hobby
hobby_counts = df['Hobby'].value_counts()

# Sort hobbies by count in descending order
hobby_counts = hobby_counts.sort_values(ascending=False)

# Print the results
print(hobby_counts)
