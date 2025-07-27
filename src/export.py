# export.py

import csv

def export_interaction_to_csv(data: list, filename: str):
    """
    Saves interaction diagram data to a CSV file.

    Parameters:
    - data (list): List of dicts with 'axial_kN', 'moment_kNm', 'failure_mode'
    - filename (str): Path to output file (e.g. 'exports/diagram.csv')
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['axial_kN', 'moment_kNm', 'failure_mode'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)