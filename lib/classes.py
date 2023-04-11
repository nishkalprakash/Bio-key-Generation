## Contains database related classes and functions

from lib.globals import get_datasets
from pathlib import Path
import random

class DS:
    """
    Dataset class
    Usage:  from lib.classes import DS
            ## Default Init
            ds = DS()
            print(ds.ds_name) # Defaults to FVC2000_Db4_a

            ## Method 2
            ds = DS()
            print(*ds.ds_names())
            ds.set_ds('FVC2000_Db1_a')
            
            ## Method 3
            ds = DS('FVC2000_Db1_a')
    """

    def __init__(self,ds_name = None ):
        """Initialize the dataset class
        Args:
            ds_name (str, optional): Gets one of the datasets defined in globals.py. Defaults to FVC2000_Db4_a.
        """
        self.all_ds = self.get_all_ds()
        self.set_ds(ds_name)        
    
    def get_all_ds(self):
        """ Generates the datasets dictionary from globals.py
        Returns: (dict): Dictionary with the dataset name as key and the DS Path as value
        """
        # all_ds=dict()

        # for d in datasets:
        #     all_ds[d.replace('/','_').replace('\\','_')] = Path(data_path)/Path(d)
        # return all_ds
        return get_datasets()

    def set_ds(self,ds_name):
        """Sets the dataset to be used by the class methods
        Args:
            ds_name (str): Dataset name. Must be one of the keys in self.all_ds
        
        Returns: None
        """
        if ds_name is None:
            # Choose a random dataset
            self.ds_name = random.choice(list(self.all_ds.keys()))
            # self.ds_name = self.all_ds.keys()
        else:
            assert self.ds_name in (n:=self.all_ds.keys()), f"DB: {self.ds_name} not found.\nPlease enter one of {' '.join(n)}"
            self.ds_name = ds_name
        self.current_ds = self.all_ds[self.ds_name]
        print(f"DB: \"{self.ds_name}\" selected.\nTo change, please invoke obj.set_ds('DS_NAME').\nTo see all available dataset names, invoke obj.ds_names().")
        

    def glob_ds(self):
        """Returns the path to the dataset folder"""
        return Path(self.current_ds['path']).glob(f'*.{self.current_ds.get("ext","*")}')
    
    def get_one(self,seed=None):
        """Returns Path to one seeded random image from the selected dataset path"""

        if seed is not None:
            random.seed(seed)
        return random.choice(list(self.glob_ds()))

    def get_all(self):
        """Returns a generator for all the images in the selected dataset path"""
        return self.glob_ds()
        

    
    

