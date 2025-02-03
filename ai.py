import pandas as pd

# Childhelp PAN number 
valid_childhelp_pan = 'AABTC2577M'
def check_childhelp_pan(unique_id):
    if unique_id == valid_childhelp_pan:
        return True
    return False

path = "C:\\Users\\mamidala.venkate\\Downloads\\validated_data1.csv"  
df = pd.read_csv(path)
if "Unique Identification Number" not in df.columns:
    raise ValueError("The dataset does not contain a 'Unique Identification Number' column.")
df['Valid PAN'] = df['Unique Identification Number'].apply(lambda x: check_childhelp_pan(x))

df['Validation Comments'] = df['Valid PAN'].apply(lambda valid: 'Valid Childhelp PAN' if valid else 'Invalid Childhelp PAN')

print("Updated DataFrame with Validation Results:")
print(df)
