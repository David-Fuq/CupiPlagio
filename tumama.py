import pandas as pd
import os

# --- Step 1: Load the inscritos file and prepare the matching column ---
# This file has columns: "Nombres", "Apellidos", and "Correo Uniandes estudiante"
df_inscritos = pd.read_excel("/Users/ardila/Downloads/2025-01-30_ISIS-1221_ListaInscritos.xlsx")

# Create a normalized student name for matching (lower case, trimmed)
df_inscritos["student_match"] = (df_inscritos["Nombres"].astype(str).str.lower().str.strip() + " " +
                                 df_inscritos["Apellidos"].astype(str).str.lower().str.strip())

# --- Step 2: Load the teachers_students file that has multiple sheets ---
teachers_sheets = pd.read_excel("teachers_students.xlsx", sheet_name=None)

# Dictionary to hold the updated sheets after merging
updated_sheets = {}

# --- Step 3: Process each sheet in the teachers_students workbook ---
for sheet_name, df_sheet in teachers_sheets.items():
    # Check if the sheet contains the "student" column to perform the join
    if "student" in df_sheet.columns:
        # Create a normalized version of the "student" column for matching
        df_sheet["student_norm"] = df_sheet["student"].astype(str).str.lower().str.strip()
        
        # Merge the current sheet with the inscritos DataFrame on the normalized student name
        df_merged = pd.merge(
            df_sheet,
            df_inscritos[["student_match", "Correo Uniandes estudiante"]],
            left_on="student_norm",
            right_on="student_match",
            how="left"
        )
        
        # Create the new "log" column with the email information
        df_merged["log"] = df_merged["Correo Uniandes estudiante"]
        
        # Drop helper columns used for matching
        df_merged.drop(columns=["student_norm", "student_match", "Correo Uniandes estudiante"], inplace=True)
        
        # Store the updated DataFrame in the dictionary
        updated_sheets[sheet_name] = df_merged
    else:
        # If the sheet doesn't have a "student" column, keep it unmodified.
        updated_sheets[sheet_name] = df_sheet

# --- Step 4: Save the updated sheets to a new multi-sheet Excel file ---
output_file = "teachers_students_with_log.xlsx"
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    for sheet_name, df in updated_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Updated workbook with log column has been saved as '{output_file}'.")


