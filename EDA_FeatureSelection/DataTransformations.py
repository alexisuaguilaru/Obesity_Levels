import pandas as pd

def NumericalCategoricalLabels(Dataframe:pd.DataFrame) -> tuple[list]:
    """
        Function to return numerical and categorical 
        labels from a dataframe

        -- Dataframe : pandas.DataFrame :: Dataframe 
        from which will be gotten its numerical and 
        categorical labels
    """
    NumericalLabels = []
    CategoricalLabels = []
    for label in Dataframe.columns:
        dtypeLabel = Dataframe[label].dtype
        if dtypeLabel == int or dtypeLabel == float:
            NumericalLabels.append(label)
        else:
            CategoricalLabels.append(label)
    return NumericalLabels , CategoricalLabels

def CategoricalIntoNumerical(Dataframe:pd.DataFrame,CategoricalLabel:str,NumericalValues:dict):
    """
        Function to convert categorical values 
        (strings) into numerical values using 
        a given dict with categorical to 
        numerical value

        -- Dataframe : pd.DataFrame :: Dataframe 
        where is applied this conversion
        -- CategoricalLabel : str :: Dataframe's 
        label which is applied this conversion
        -- NumericalValues : dict :: Numerical 
        values which replace categorical values
    """
    NumericalMap = lambda value: NumericalValues[value]
    Dataframe[CategoricalLabel] = Dataframe[CategoricalLabel].apply(NumericalMap)