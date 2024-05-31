from core.data import Data
from core.config import Column
data = Data()
data.read('data/SBIN.NS.csv')
data.clean_data()
print(Column.OPEN.value)
data.print_head()
data.print_description()
data.normalize()
data.visualize(Column.OPEN.value)
data.visualize(Column.CLOSE.value)