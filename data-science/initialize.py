# Import library
import pandas as pd

# Read the data from the CSV file
df = pd.read_csv("sample-data.csv")

# Display the column names
print(df.columns.tolist())
