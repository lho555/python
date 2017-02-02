import pandas as pd
import　matplotlib.pyplot as plt
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt'
present = pd.read_table(url, sep=' ')
print("",present.shape)
print("",present.columns)
present_year = present.set_index('year')
print("",present_year['boys'].plot())
