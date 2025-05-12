import pandas as pd
import re
import os

# ----------------------------
# Step 1: Extract allowed student names from the Excel workbook
# ----------------------------

excel_path = "teachers_students.xlsx"

# Read all sheets from the Excel file into a dictionary
sheets_dict = pd.read_excel(excel_path, sheet_name=None)

allowed_student_names = set()
for sheet_name, sheet_df in sheets_dict.items():
    # Normalize column names (strip and lower-case)
    sheet_df.columns = [col.strip().lower() for col in sheet_df.columns]
    if "student" in sheet_df.columns:
        # Extract unique names from the "student" column, stripping extra whitespace
        names = sheet_df["student"].dropna().astype(str).str.strip().unique()
        allowed_student_names.update(names)

if not allowed_student_names:
    print("Warning: No student names found in the Excel file under column 'student'.")
else:
    print("Allowed student names from Excel:")
    print(sorted(allowed_student_names))


# ----------------------------
# Step 2: Load the CSV file
# ----------------------------

csv_path = "grouped_email_info.csv"
csv_df = pd.read_csv(csv_path)

# Normalize CSV column names (strip extra spaces)
csv_df.columns = [col.strip() for col in csv_df.columns]

if "email_content" not in csv_df.columns:
    raise ValueError("The CSV file does not have an 'email_content' column.")

# ----------------------------
# Step 3: Process each "email content" cell to filter student names
# ----------------------------

def filter_email_content(content, allowed_names):
    """
    Given a multi-line string (content) with each line having the pattern:
       "Section <number>: Student1, Student2, ..."
    This function will filter the student names so that only names in allowed_names are kept.
    Lines without any remaining names are dropped.
    """
    # Split the content by newlines into separate lines
    lines = content.splitlines()
    filtered_lines = []
    for line in lines:
        # Use a regex to capture the section header and the list of student names.
        # This pattern assumes a colon separates the section header from the names.
        match = re.match(r"^(Section\s+\S+\s*:\s*)(.*)$", line)
        if match:
            header = match.group(1)
            students_str = match.group(2)
            # Split the student names by comma
            student_names = [s.strip() for s in students_str.split(",") if s.strip()]
            # Filter out names that are not in allowed_names
            filtered_names = [name for name in student_names if name in allowed_names]
            # If there are any names left, reassemble the line
            if filtered_names:
                new_line = header + ", ".join(filtered_names)
                filtered_lines.append(new_line)
        else:
            # If the line doesn't match the pattern, keep it as is.
            filtered_lines.append(line)
    # Reassemble all non-empty lines (if none remain, return an empty string)
    return "\n".join(filtered_lines).strip()

# Apply the filter to every row in the CSV's "email content" column.
csv_df["email_content"] = csv_df["email_content"].astype(str).apply(lambda x: filter_email_content(x, allowed_student_names))

# ----------------------------
# Step 4: Save the filtered CSV as "grouped_emailv.2.csv"
# ----------------------------

output_csv = "grouped_emailv.2.csv"
csv_df.to_csv(output_csv, index=False)

if os.path.exists(output_csv):
    print(f"Filtered CSV successfully saved as '{output_csv}'.")
else:
    print("Error: The filtered CSV file was not saved.")
