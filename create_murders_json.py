import pandas as pd
import numpy as np
from csvIn import df
import json
import datetime

dfmurd = df[["OFNS_DESC","CMPLNT_FR_DT","CMPLNT_FR_TM",
	"BORO_NM","Latitude","Longitude"]][
		df["OFNS_DESC"].str.contains("murd",case=False,na=False)]

dfmurd = dfmurd.assign(HOUR = 
	[int(x[:2]) for x in dfmurd["CMPLNT_FR_TM"]])

dfmurd = dfmurd.assign(DATE = 
	[datetime.datetime(int(x[6:]),int(x[:2]),int(x[3:5])).isoformat()
		for x in dfmurd["CMPLNT_FR_DT"]])

dfmurd["BORO_NM"] = dfmurd.BORO_NM.str.title()

j = dfmurd.to_json(orient='records')

with open("murders.json",'w') as file:
	file.write(j)
