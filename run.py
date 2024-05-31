from Core.data import Data
from Core.config import Column
data = Data()
data.read('Data/SBIN.NS.csv')
data.clean_data()
print(Column.OPEN.value)
data.print_head()
data.print_description()
data.normalize()
data.visualize(Column.OPEN.value)
data.visualize(Column.CLOSE.value)