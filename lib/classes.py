## Contains database related classes and functions

from lib.globals import *
from pathlib import Path

def all_ds():
    ds=dict()

    ## FVC2000 Db4
    ds['FVC2000_Db4_a'] = "data/FVC2000/Dbs/Db4_a"
    ds['FVC2000_Db4_b'] = "data/FVC2000/Dbs/Db4_b"

    ## FVC2002 Db1
    ds['FVC2002_Db1_a'] = "data/FVC2002/Dbs/Db1_a"
    ds['FVC2002_Db1_b'] = "data/FVC2002/Dbs/Db1_b"

    return ds


class DB:
    def __init__(self):
        self.all_ds = all_ds()
    
    def ds_names(self):
        return self.all_ds.keys()

    def get(self, name):
        assert name in (n:=self.all_ds.keys()), f"DB: {name} not found.\nPlease enter one of {' '.join(n)}"
        return Path(self.all_ds[name])
    
    

