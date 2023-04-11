# # Main file that runs the entire pipeline

#%% Importing the necessary libraries
from lib.classes import DS

#%% Initializing the dataset class
ds1=DS()

# %%
ds1.get_one()
# %%
len(list(ds1.get_all()))
# %%
# ds1.set_ds('FVC2000_Db1_b')
# %%
ds1.current_ds
# %%
