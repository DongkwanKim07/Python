import matplotlib.pyplot as plt
import csv

# This class will make a chart using csv file.
# Author : Dongkwan Kim
x = []
y = []

with open('NAFO-4TVN-Atlantic-Cod-otoliths.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(row[0])
        y.append(int(row[5]))

plt.bar(x, y, color='g', width=0.72, label="number")
plt.xlabel('source')
plt.ylabel('Month')
plt.title('Source by Month, Program by Dongkwan Kim')
plt.legend()
plt.show()

# plt.style.use('bmh')
# df = pd.read_csv('NAFO-4TVN-Atlantic-Cod-otoliths.csv')
#
# x = df['source']
# y = df['number']
#
# plt.pie(y, labels=x, radius=1.2, autopct='%0.01f%%', shadow=True, explode=[.05, .2, .05, .2])