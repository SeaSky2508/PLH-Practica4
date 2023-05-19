from typing import List

class Data:
    """
    =====================================================================================================
    Class Data - Contains methods and attributes to work with the Datasets provided.
    =====================================================================================================

    • ATTRIBUTES
    ------------
        ⮕ datasets // An internal dictionary dataset_name - dataset processed dataset is stored.
    ------------

    • METHODS
    ------------
      ~ MODIFIERS ~
        ⮕ add_data // Adds a processed dataset given its data_name.
        ⮕ process // All preprocessing is hnadled in the function, might consider adding auxiliar functions (not mehtods) for it.


      ~ GETTERS ~
        ⮕ return_dataset // Adds a processed dataset given its data_name.
    ------------
    """
    def __init__(self):
        'Setting up data dictionary to store various processed datasets.'
        self._datasets = {}

    def __str__(self): # Use: print(data: Data)
        'Representation method to see all stored data.'
        res = ''
        for pair in self._datasets.items():
            key, value = pair[0], pair[1]
            res.join(f'Dataset Name: {key}, Number of rows: {len(value)}\n')
        return res

    def add_data(self,data: List[List],data_name: str):
        'Pre: data is a list of lists'
        'Adds a dataset to the internal dictionary of data.'
        self._datasets[data_name] = self.process(data)

    def process(self,data: List[List]):
        'Preprocessing function, returns all data preprocessed in a list of lists format.'
        return(not_implemented)
    
    def get_data(self,data_name: str):
        'Returns a stored dataset'
        if data_name in self._datasets:
            return self._datasets[data_name]
        else:
            raise KeyError("The name provided is not known")
