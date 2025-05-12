import os
import re
import argparse
import zipfile
import csv
from io import BytesIO

def remove_iniciar_aplicacion_function(content):
    return re.compile(r"^def\s+iniciar_aplicacion\(\)\s*->\s*None:\s*\n(?:(?:[ \t]+.*\n)|(?:[ \t]*\n))+", re.MULTILINE).sub("", content)

def remove_while_ejecutando_line(content):
    return re.compile(r"^\s*while\s+ejecutando.*\n?", re.MULTILINE).sub("", content)

def extract_student_from_path(file_path):
    parts = re.split(r"[\\/]", file_path)
    for part in parts:
        match = re.search(r"Mache\s*-\s*(.*?)\s*-\s*tazo", part, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ""

def extract_seccion(file_path):
    match = re.search(r'proyectos/[^/]*?_(\d+)_N2_PROY', file_path, re.IGNORECASE)
    if match:
        return match.group(1)
    return ""

def clean_file_name(file_path):
    return re.sub(r"^/Users/ardila/Downloads/", "", file_path)

def search_patterns(content, patterns):
    content = remove_iniciar_aplicacion_function(content)
    content = remove_while_ejecutando_line(content)
    lines = content.splitlines()
    matches = {}
    for key, pattern in patterns.items():
        match_results = []
        for m in pattern.finditer(content):
            line_number = content[:m.start()].count('\n')
            line_text = lines[line_number].strip() if line_number < len(lines) else ""
            match_str = f"{m.group().strip()} -> {line_text}"
            match_results.append(match_str)
        if match_results:
            matches[key] = match_results
    return matches

def process_file(content, file_identifier, patterns, report):
    matches = search_patterns(content, patterns)
    if matches:
        record = {
            "file_name": clean_file_name(file_identifier),
            "student": extract_student_from_path(file_identifier),
            "seccion": extract_seccion(file_identifier),
            "lambda_expressions": "",
            "list_comprehensions": "",
            "try": ""
        }
        for key in ["lambda_expressions", "list_comprehensions", "try"]:
            if key in matches:
                record[key] = " | ".join(matches[key])
        print(f"File: {file_identifier}")
        for key in ["lambda_expressions", "list_comprehensions", "try"]:
            if record[key]:
                print(f"  {key}: {record[key]}")
        print('-' * 40)
        report.append(record)

def process_plain_file(filepath, patterns, report):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return
    process_file(content, filepath, patterns, report)

def process_zip_file(zip_file, patterns, report, parent_path=None):
    try:
        with zipfile.ZipFile(zip_file) as z:
            for zinfo in z.infolist():
                if zinfo.is_dir():
                    continue
                if parent_path:
                    file_identifier = f"{parent_path}::{zinfo.filename}"
                else:
                    identifier_source = zip_file if isinstance(zip_file, str) else "nested_zip"
                    file_identifier = f"{identifier_source}::{zinfo.filename}"
                if zinfo.filename.endswith('.py'):
                    try:
                        with z.open(zinfo) as f:
                            content = f.read().decode('utf-8')
                    except Exception as e:
                        print(f"Error reading file {file_identifier}: {e}")
                        continue
                    process_file(content, file_identifier, patterns, report)
                elif zinfo.filename.endswith('.zip'):
                    base_name = os.path.splitext(zinfo.filename)[0]
                    if re.fullmatch(r'\d+', base_name):
                        continue
                    try:
                        with z.open(zinfo) as f:
                            data = f.read()
                        nested_zip = BytesIO(data)
                        process_zip_file(nested_zip, patterns, report, parent_path=file_identifier)
                    except Exception as e:
                        print(f"Error processing nested zip {file_identifier}: {e}")
    except Exception as e:
        print(f"Error opening zip file {zip_file}: {e}")

def search_code(folder):
    patterns = {
        "lambda_expressions": re.compile(r'\blambda\b'),
        "list_comprehensions": re.compile(r'\[\s*[^]]*\s+for\s+[^]]*\s+in\s+[^]]*\]'),
        "try": re.compile(r'\btry\s*:', re.IGNORECASE)
    }
    report = []
    for root, dirs, files in os.walk(folder):
        print(f"Searching in directory: {root}")
        dirs[:] = [d for d in dirs if not re.fullmatch(r'\d+', d)]
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.py'):
                process_plain_file(file_path, patterns, report)
            elif file.endswith('.zip'):
                base_name = os.path.splitext(file)[0]
                if re.fullmatch(r'\d+', base_name):
                    continue
                process_zip_file(file_path, patterns, report)
    return report

def save_report_csv(report, output_csv='report.csv'):
    fieldnames = ["file_name", "student", "seccion", "lambda_expressions", "list_comprehensions", "try"]
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
    parser = argparse.ArgumentParser("")
    parser.add_argument("folder", nargs='?', default="C:/Users/fuque/Pictures/CupiPlagio/FuquenFinal", help="")
    args = parser.parse_args()
    print(args)
    print(f"Searching in folder: {args.folder}")
    if not os.path.exists(args.folder):
        print(f"Folder {args.folder} does not exist.")
        exit(1)
    report = search_code(args.folder)
    save_report_csv(report)
