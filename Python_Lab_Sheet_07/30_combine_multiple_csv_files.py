# Question 30: Write a program to combine multiple CSV files into one single file.
# Put input CSV files in the same folder and list their names in input_files.
import csv

input_files = ["students.csv", "students_extra.csv"]
output_file = "combined_students.csv"

try:
    with open(output_file, "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        header_written = False
        for filename in input_files:
            try:
                with open(filename, "r", newline="", encoding="utf-8") as source:
                    reader = csv.reader(source)
                    header = next(reader, None)
                    if header is None:
                        continue
                    if not header_written:
                        writer.writerow(header)
                        header_written = True
                    for row in reader:
                        writer.writerow(row)
            except FileNotFoundError:
                print(f"Skipping missing file: {filename}")
    print(f"Combined CSV data saved to {output_file}.")
except OSError as error:
    print(f"File error: {error}")
