import pandas as pd

# Read the wild type sequence
with open('wild_type_sequence.txt', 'r') as f:
    wild_type_sequence = f.read().strip()

# Read the original dataframe
df = pd.read_csv('df.csv')  # Adjust the filename if different

# Create a copy of the dataframe to avoid modifying the original
df_wild = df.copy()

# Replace sequences where clinical_significance is 'normal' with wild type sequence
df_wild.loc[df_wild['clinical_significance'] == 'normal', 'sequence'] = wild_type_sequence

# Save the modified dataframe
df_wild.to_csv('df_wild.csv', index=False)

print("Number of sequences replaced:", (df_wild['clinical_significance'] == 'normal').sum())
print("Total rows in dataframe:", len(df_wild)) 