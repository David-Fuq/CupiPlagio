import pandas as pd
import os

# Input file path (adjust if necessary)
input_file = "teachers_students_with_log.xlsx"

# Create an output folder to store the separate Excel files.
output_folder = "separated_sheets_log"
os.makedirs(output_folder, exist_ok=True)

# Read all sheets from the input Excel file.
sheets_dict = pd.read_excel(input_file, sheet_name=None)

# Process each sheet and save it as a separate Excel file.
for sheet_name, df in sheets_dict.items():
    # Sanitize sheet name to be used as a valid filename.
    safe_sheet_name = "".join(c if c.isalnum() or c in " -_" else "_" for c in sheet_name)
    
    output_file = os.path.join(output_folder, f"{safe_sheet_name}.xlsx")
    df.to_excel(output_file, index=False)
    print(f"Saved sheet '{sheet_name}' to '{output_file}'")

print("All sheets have been separated into individual Excel files.")
