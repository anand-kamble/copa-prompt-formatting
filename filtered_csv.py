#%%
import pandas as pd
# %%
df = pd.read_csv('~/copa/data-filtering/TABLES_ADD_20240515/ISDP LOGBOOK REPORT.csv',encoding="latin1")
# %%
newdf = df[['FAULT_NAME','FAULT_SDESC','ATA']]
# %%
newdf.to_csv('faults.csv',index=False)
# %%
