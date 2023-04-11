## Path to the dataset base folder
from pathlib import Path

_data = Path("data/")


## Individual datasets in the dataset folder
def get_datasets():
    DATASET_MORE_INFO = {
        "FVC2000": {
            "URL": "http://bias.csr.unibo.it/fvc2000/databases.asp",
            "naming": "{Person_id:3d}_{Impr_id:1d}",
            "res": "500dpi",
            "ext": "tif",  # Required
            "Dbs": {
                "Db1": {
                    "width": 300,  # Required
                    "height": 300,  # Required
                    "desc": 'FVC2000 Db1\nLow-cost optical sensor "Secure Desktop Scanner" by KeyTronic',
                },
                "Db2": {
                    "width": 256,  # Required
                    "height": 364,  # Required
                    "desc": 'FVC2000 Db2\nLow-cost capacitive sensor "TouchChip" by ST Microelectronics',
                },
                "Db3": {
                    "width": 448,  # Required
                    "height": 478,  # Required
                    "desc": 'FVC2000 Db3\nOptical sensor "DF-90" by Identicator Technology',
                },
                "Db4": {
                    "width": 240,  # Required
                    "height": 320,  # Required
                    "desc": "FVC2000 Db4\nSynthetic Generator",
                },
            },
            "CITE": "F. Roli, M. Cristani, M. Poggi, and G. Tesei. Fingerprint verification competition (FVC2000). In Proceedings of the 2nd International Conference on Biometrics: Theory, Applications and Systems (BTAS 2000), pages 1-8, 2000.",
        }
    }
    DATASETS_INFO = dict()
    for db, info in DATASET_MORE_INFO.items():
        dbs = info.pop("Dbs")
        for sub_db, sub_info in dbs.items():
            part_info = {}
            for part in ['a', 'b']:
                part_info['path']=Path(_data)/db/'Dbs'/f'{sub_db}_{part}'
                part_info['nf']=100 if part=='a' else 10
                part_info['ni']=8
                part_info['n']=part_info['ni']*part_info['nf']

                DATASETS_INFO[f"{db}_{sub_db}_{part}"] = {
                    **part_info,
                    **sub_info,
                    **info,
                }

    return DATASETS_INFO
