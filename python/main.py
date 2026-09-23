import pandas as pd

df = pd.read_excel(r"data\ConnectTel Customer Service Call Centre Analysis .xlsx")

print("**********************Data Cleaning**********************")

#Checking missing values
print ("=" *50)
print("MISSING VALUES")
print("=" *50)
print(df.isnull().sum())

# Remove columns that are completely empty
df = df.dropna(axis = 1, how = "all")
print(df.columns)
print(df.shape)

# Display the last 20 rows
print(df.tail(20))

# Show only rows where column .1 has data
print(df[df[" .1"].notna()])

# Remove summary columns
df = df.drop(columns = [" .1", " .2", " .3"])

# Display the final dataset information
print(df.info())

print("\nDataset Shape:")
print(df.shape)

# Save the cleaned dataset
df.to_excel("outputs/cleaned_call_center_data.xlsx", index=False)

print("\n✅ Cleaned dataset saved successfully!")
