import pandas as pd
import re

# Read the CSV file.
df = pd.read_csv("report_with_professor_info.csv")

# Drop any columns that include the word "file" (case-insensitive).
cols_to_drop = [col for col in df.columns if "file" in col.lower()]
df.drop(columns=cols_to_drop, inplace=True)

# Exclude any student whose "loops" column *only* contains "while -> while True:".
if "loops" in df.columns:
    # Use .str.strip() to ignore extra spaces and compare exactly.
    df = df[~(df['loops'].astype(str).str.strip() == "while -> while True:")]

# Ensure the 'seccion' column is numeric.
df['seccion'] = pd.to_numeric(df['seccion'], errors='coerce')

# Define the grouping keys:
# - "professor mail" for the teacher's email,
# - "seccion" for the section number,
# - "student name" for the student.
group_keys = ['professor mail', 'seccion', 'student']

# Define additional student information columns.
# We exclude the grouping keys plus the teacher's name column "profesor".
additional_cols = [col for col in df.columns if col not in group_keys + ['profesor']]

# For duplicate student entries within the same group, aggregate each additional column
# by combining all unique non-null values (separated by commas).
agg_functions = {
    col: lambda x: ", ".join(sorted(set(x.dropna().astype(str))))
    for col in additional_cols
}

# Group by teacher, section, and student name, then aggregate additional student info.
aggregated_df = df.groupby(group_keys, as_index=False).agg(agg_functions)
aggregated_df = aggregated_df.sort_values(by=['professor mail', 'seccion', 'student'])

# Create an Excel workbook where each teacher has its own sheet.
output_excel = "teachers_students.xlsx"
with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
    # Group by teacher email.
    for teacher_email, group in aggregated_df.groupby('professor mail'):
        # Sort the group by section.
        group = group.sort_values(by='seccion')
        # Clean the teacher's email to use as a valid Excel sheet name.
        # Excel sheet names cannot exceed 31 characters and cannot contain: : \ / ? * [ ]
        sheet_name = re.sub(r"[@\.\:\/\?\*\[\]\\]", "_", teacher_email)[:31]
        group.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Excel workbook '{output_excel}' has been created with one sheet per teacher (students with only 'while -> while True:' in loops were excluded).")
