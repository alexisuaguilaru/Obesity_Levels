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