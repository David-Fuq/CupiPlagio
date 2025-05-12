import pandas as pd

output_file = "teachers_students_with_log.xlsx"

# List (or set) of logins to exclude. We only match the part before "@uniandes.edu.co".
excluded_logins = {
    "c.jaimec",
    "js.rodriguez",
    "v.moremom23",
    "jc.arango",
    "c.oostra",
    "l.londonob2",
    "ay.martinezf1",
    "l.bustosl",
    "s.jaime",
    "w.fajardol",
    "m.bullaa",
    "k.leons",
    "jc.arevalol12",
    "jd.gomez234",
    "s.ramirezr2345",
    "je.ruizb1",
    "jd.ramirezt1",
    "l.triana",
    "m.saenzh2",
    "jj.plata",
    "s.escobarz",
    "da.mendoza",
}

# Read the updated workbook (all sheets) into a dictionary of DataFrames.
df_updated = pd.read_excel(output_file, sheet_name=None)

# Initialize an empty list to collect all valid log entries.
all_logs = []

# Iterate through each sheet and collect log entries.
for sheet_name, df in df_updated.items():
    if "log" in df.columns:
        # Collect all non-null log entries from the 'log' column
        logs = df["log"].dropna().astype(str).tolist()
        
        # Filter out excluded logins (based on the part before '@')
        filtered_logs = []
        for log in logs:
            # Split only once at '@' to get the local part
            local_part = log.split("@", 1)[0].strip()
            # If the local part is *not* in the excluded list, keep this log.
            if local_part not in excluded_logins:
                filtered_logs.append(log)
        
        all_logs.extend(filtered_logs)

# Create a comma-separated string of all remaining log entries.
all_logs_string = ",".join(all_logs)

# Print the result
print("All log entries (comma-separated):")
print(len(all_logs_string.split(",")))

# Print how many logs we have left after exclusion
print(f"Number of log entries after exclusion: {len(all_logs)}")

# Save the log entries to a text file
with open("all_log_entries.txt", "w") as f:
    f.write(all_logs_string)

# Notify the user that the log entries have been saved
print("All log entries have been saved to 'all_log_entries.txt'.")
