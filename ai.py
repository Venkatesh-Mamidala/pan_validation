import pandas as pd

# Define the specific Childhelp Foundation PAN number (replace 'AABTC2577M' with your actual PAN number)
valid_childhelp_pan = 'AABTC2577M'

# Function to check if the Unique Identification Number matches the specific Childhelp PAN number
def check_childhelp_pan(unique_id):
    if unique_id == valid_childhelp_pan:
        return True
    return False

# Path to your input CSV file
input_csv = "C:\\Users\\mamidala.venkate\\Downloads\\validated_data1.csv" # Change this to your actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv)

# Check if the "Unique Identification Number" column exists
if "Unique Identification Number" not in df.columns:
    raise ValueError("The dataset does not contain a 'Unique Identification Number' column.")

# Create a new column "Valid PAN" to store whether the Unique ID matches the specific PAN number
df['Valid PAN'] = df['Unique Identification Number'].apply(lambda x: check_childhelp_pan(x))

# Add a new column for comments
df['Validation Comments'] = df['Valid PAN'].apply(lambda valid: 'Valid Childhelp PAN' if valid else 'Invalid Childhelp PAN')

# Show the updated DataFrame
print("Updated DataFrame with Validation Results:")
print(df)

