import csv


class ReadingError(Exception):
    def __init__(self,string):
        self.string = string

    def __str__(self):
        return repr(self.string)


# Read data from .csv file
# Values are converted to float if possible,
# if not, left as strings
# Input:
#   - file path : string
# Output:
#   - data : dict
#       key: column name from file header
#       value: column values in a list
class DataReader:

    def __init__(self, file):
        self.file = file

    def read_to_dict(self):
        header = ''
        data = {}
        with open(self.file) as f:
            rdr = csv.reader(f)
            header = next(rdr)
            for i in range(0,len(header)):
                data[header[i]] = []
            count = 1
            for row in rdr:
                count += 1
                if len(row) != len(header):
                    raise ReadingError('Invalid number of values on row '+str(count))
                for i in range(0,len(row)):
                    try:
                        data[header[i]].append(float(row[i]))
                    except ValueError:
                        data[header[i]].append(row[i])
        return data
