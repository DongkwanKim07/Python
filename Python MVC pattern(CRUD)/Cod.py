# This is second assignment for Program language research project.
# Need to create a record object that uses column names from the dataset
# as part of the source code.
# Also need to follow the tasks - variable names, accessors/mutators names,
# File-IO, array or list structure, and loop.
# Also Need to implement MVC design pattern.


# Course : CST8333 Programming Language Research Project
# Author : Dongkwan Kim

import csv

# Create class CodFish to define record object
# Variable names are from dataset('NAFO-4TVN-Atlantic-Cod-otoliths.csv')
# Author : Dongkwan Kim
class CodFish:
    def __init__(self, source, latin_name, english_name, french_name, year, month, number_otoliths):
        self._source = source
        self._latin_name = latin_name
        self._english_name = english_name
        self._french_name = french_name
        self._year = year
        self._month = month
        self._number_otoliths = number_otoliths

# This part shows getter and setter.
# In Python, can use @property for getter and setter.
    # Author : Dongkwan Kim
    # Accessor and Mutator for source
    @property
    def source(self): return self._source
    @source.setter
    def source(self, val): self._source = val
    # Accessor and Mutator for latin_name
    @property
    def latin_name(self): return self._latin_name
    @latin_name.setter
    def latin_name(self, val): self._latin_name = val
    # Accessor and Mutator for english_name
    @property
    def english_name(self): return self._english_name
    @english_name.setter
    def english_name(self, val): self._english_name = val
    # Accessor and Mutator for french_name
    @property
    def french_name(self): return self._french_name
    @french_name.setter
    def french_name(self, val): self._french_name = val
    # Accessor and Mutator for year
    @property
    def year(self): return self._year
    @year.setter
    def year(self, val): self._year = val
    # Accessor and Mutator for month
    @property
    def month(self): return self._month
    @month.setter
    def month(self, val): self._month = val
    # Accessor and Mutator for number_otoliths
    @property
    def number_otoliths(self): return self._number_otoliths
    @number_otoliths.setter
    def number_otoliths(self, val): self._number_otoliths = val

# This is Method for display result
    # Author : Dongkwan Kim
    def toString(self):
        print('source =', self._source, ',',
              'latin_name =', self._latin_name, ',',
              'english_name =', self._english_name, ',',
              'french_name =', self._french_name, ',',
              'year =', self._year, ',',
              'month =', self._month, ',',
              'number_otoliths =', self._number_otoliths)
        return ''


# This part includes File-IO for reading the values from dataset and Exception handling.
# If importing dataset file is fail, exception handling will shows message.
# Also include loop over the data structure.
# Author : Dongkwan Kim
def load_data(filename):
    dataList = list()
    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
        #     for row in csv_reader:
        #         dataList.append(CodFish(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            try:
                for i in range(100):
                    row = next(csv_reader)
                    dataList.append(CodFish(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            except StopIteration:
                pass
    except IOError:
        print("No file")
    # If it is success to access dataset, this message will print out.
    else:
        print("Program by Dongkwan Kim")
    return dataList


# This is the method that write a csv file
# Use this method for make a new csv file.
def contents_list(dataList, filename):
    with open(filename + '.csv', 'w') as csv_file:
        write = csv.writer(csv_file)
        write.writerow(['source', 'latin_name', 'english_name', 'french_name', 'year', 'month', 'number_otoliths'])
        for value in dataList:
            write.writerow([value.source, value.latin_name, value.english_name, value.french_name,
                            value.year, value.month, value.number_otoliths])


