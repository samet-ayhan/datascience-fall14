import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

import pandas as pd
import numpy as np

reader = DataFileReader(open("countries.avro", "r"), DatumReader())

df = pd.DataFrame(columns=('name', 'country_id', 'area_sqkm', 'population'))

for country in reader:
	s = pd.Series(country, index=['name', 'country_id', 'area_sqkm', 'population'])
	df = df.append(s, ignore_index=True)

print df.groupby(df['population'] > 10000000).size()
#print df[df['population'] > 10000000].count()
reader.close()
