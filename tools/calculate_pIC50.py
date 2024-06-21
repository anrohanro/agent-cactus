from langchain.tools import BaseTool
from molfeat.calc import FPCalculator
from molfeat.trans import MoleculeTransformer
import numpy as np
import pickle
DESC = """
Use this tool when you need to calculate the pIC50 value for the input compound and you have SMILES string as input
"""


class Calculate_pIC50(BaseTool):
    name = "Calculate_pIC50"
    description = DESC

    def _run(self, compound_smiles: str) -> float:
        # Convert SMILES string to fingerprint
        # Load the trained model from the file
        print(compound_smiles + "---------------------------------------------")
        with open(r'C:\Users\Rohan KumarMishra\Desktop\cactus\cactus\src\cactus\tools\trained_model.pkl', 'rb') as file:
            model = pickle.load(file)
        calc = FPCalculator("ecfp")
        trans = MoleculeTransformer(calc)
        
        fp = trans.transform([compound_smiles])
    
        # Predict pIC50 value using the model
        pIC50 = model.predict(np.stack(fp))
    
        return pIC50[0] 
    

    async def _arun(self, compound_smiles: str) -> float:
        """Use the Calculate_pIC50 tool asynchronously."""
        raise NotImplementedError()
