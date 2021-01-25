from io import StringIO
import csv, pytz
from datetime import datetime

def to_db(date):
    file_csv = StringIO(date)
    reader = csv.reader(file_csv)
    first_line = True

    for row in reader:
        if first_line:
            first_line = False
            continue
        purchase = {
            'customer': row[0],
            'item': row[1],
            'total': int(row[2]),
            'quantity': int(row[3]),
            'date': datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f')
        }
        yield purchase

if __name__ == '__main__':
    with open('deals.csv') as f:
        for item in to_db(f.read()):
            print(item)


