
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the MySQL database
# And use the query that count sources by source name
# sql : select source, count(*) from atlanticcod group by source;
# Author : Dongkwan Kim
myMyConn = mysql.connector.connect(user='Python', password='Python', host='localhost', port=3308, database='pythonproject')
myMyCursor = myMyConn.cursor()
sql = "select source, count(*) from atlanticcod group by source;"

df = pd.read_sql(sql, myMyConn)

# Print this method to get information from MySQL database
# Can find the numbers of sources for each source
print(df)

# From the output, found sources and values of sources
# Use matplotlib.pyplot plugin to draw a chart
# For the pie chart : plt.pie
# Add some options for better looking of chart (colors and explode)
# Author : Dongkwan Kim
source = ['Commercial', 'Observers', 'RV-4T', 'SENT-4T']
quantity = [508, 16, 64, 14]
my_colors = ['orange', 'lightsteelblue', 'pink', 'lightgreen']
my_explode = (0, 0.1, 0, 0)
# plt.barh(source, quantity)
plt.pie(quantity, labels = source, autopct = '%1.1f%%',startangle=15, shadow=True, colors=my_colors, explode=my_explode)
plt.title('percentage by source, Program by Dongkwan Kim')
plt.axis('equal')
# plt.ylabel('product')
# plt.xlabel('quantity')
plt.show()
# source = df['source']
# source.index = df['DT']
#
# plt.figure(figsize=(11,9))
# source.plot(label='Close Price', title= "Samsung Close Price")
# plt.legend(loc='lower left')
# plt.grid(True)
# plt.show()


# def method_for_chart_graph(sources):
#     figure = plt.figure()
#     axes = figure.add_subplot(1, 1, 1)
#     axes.bar(
#         range(len(sources)),
#         [source[1] for source in sources],
#         tick_lable = [source[0] for source in sources])
#     return figure
#


