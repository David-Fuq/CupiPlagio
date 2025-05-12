import os
import re
import argparse
import zipfile
import csv
from io import BytesIO

def extract_student_from_path(file_path):
    parts = re.split(r"[\\/]", file_path)
    for part in parts:
        match = re.search(r"Mache\s*-\s*(.*?)\s*-\s*tazo", part, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ""

def extract_seccion(file_path):
    match = re.search(r'proyectos[\\/]\d+_[A-Z]+\d+_(\d+)_N3_PROY', file_path, re.IGNORECASE)
    if match:
        return match.group(1)
    return ""

def clean_file_name(file_path):
    # Normalize path by replacing backslashes with forward slashes
    normalized_path = file_path.replace("\\", "/")
    # Remove the fixed prefix
    cleaned_path = re.sub(r"^C:/Users/fuque/Pictures/CupiPlagio/FuquenFinal/proyectos/", "", normalized_path)
    # Restore backslashes for consistency
    return cleaned_path.replace("/", "\\")

def load_patterns(file_path):
    """Load patterns from a given text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            patterns = [re.compile(line.strip()) for line in file if line.strip()]
        return patterns
    except Exception as e:
        print(f"Error loading patterns from {file_path}: {e}")
        return []

def remove_patterns(content, remove_patterns):
    """Remove content that matches any pattern from the remove_patterns list."""
    for pattern in remove_patterns:
        content = pattern.sub("", content)
    return content

def search_patterns(content, search_patterns):
    """Search for patterns in the content and collect matches."""
    lines = content.splitlines()
    matches = {}
    for key, pattern in search_patterns.items():
        match_results = []
        for m in pattern.finditer(content):
            line_number = content[:m.start()].count('\n')
            line_text = lines[line_number].strip() if line_number < len(lines) else ""
            match_str = f"{m.group().strip()} -> {line_text}"
            match_results.append(match_str)
        if match_results:
            matches[key] = match_results
    return matches

def process_file(content, file_identifier, search_patterns, remove_patterns, report):
    """Process a single file content."""
    # Remove specified patterns
    content = remove_patterns(content, remove_patterns)

    # Search for specified patterns
    matches = search_patterns(content, search_patterns)

    if matches:
        record = {
            "file_name": clean_file_name(file_identifier),
            "student": extract_student_from_path(file_identifier),
            "seccion": extract_seccion(file_identifier),
        }
        for key in search_patterns.keys():
            record[key] = " | ".join(matches.get(key, []))
        print(f"File: {file_identifier}")
        for key in search_patterns.keys():
            if record.get(key):
                print(f"  {key}: {record[key]}")
        print('-' * 40)
        report.append(record)

def process_plain_file(filepath, search_patterns, remove_patterns, report):
    """Read and process a plain .py file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        process_file(content, filepath, search_patterns, remove_patterns, report)
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")

def process_zip_file(zip_file, search_patterns, remove_patterns, report, parent_path=None):
    """Process zip files, including nested ones."""
    try:
        with zipfile.ZipFile(zip_file) as z:
            for zinfo in z.infolist():
                if zinfo.is_dir():
                    continue
                file_identifier = f"{parent_path}::{zinfo.filename}" if parent_path else zinfo.filename
                if zinfo.filename.endswith('.py'):
                    with z.open(zinfo) as f:
                        content = f.read().decode('utf-8')
                    process_file(content, file_identifier, search_patterns, remove_patterns, report)
    except Exception as e:
        print(f"Error processing zip file {zip_file}: {e}")

def search_code(folder, search_patterns, remove_patterns):
    """Search for code files in the given folder."""
    report = []
    for root, dirs, files in os.walk(folder):
        print(f"Searching in directory: {root}")
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.py'):
                process_plain_file(file_path, search_patterns, remove_patterns, report)
            elif file.endswith('.zip'):
                process_zip_file(file_path, search_patterns, remove_patterns, report)
    return report

def save_report_csv(report, output_csv='report.csv'):
    """Save the report as a CSV file."""
    fieldnames = ["file_name", "student", "seccion"] + list(report[0].keys())[3:]
    try:
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in report:
                writer.writerow(row)
        print(f"Report saved to {output_csv}")
    except Exception as e:
        print(f"Error saving report to CSV: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Folder to search for code files")
    parser.add_argument("remove_patterns", help="File containing patterns to remove")
    parser.add_argument("search_patterns", help="File containing patterns to search")
    args = parser.parse_args()

    # Load patterns from the specified files
    remove_patterns = load_patterns(args.remove_patterns)
    search_patterns = {f"pattern_{i+1}": re.compile(line.strip()) for i, line in enumerate(open(args.search_patterns))}

    if not os.path.exists(args.folder):
        print(f"Folder {args.folder} does not exist.")
        exit(1)

    # Perform the search
    report = search_code(args.folder, search_patterns, remove_patterns)

    # Save the result to CSV
    save_report_csv(report)
