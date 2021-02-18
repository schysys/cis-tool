import csv
import argparse

def csv_read(file):
    print(f"reading csv file {file}")
    with open(file, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i, row in enumerate(csv_reader):
            if i == 0:
                print(f'Column names are {", ".join(row)}')
                exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV Parser")
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()
    csv_read(args.file)

