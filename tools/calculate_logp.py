from langchain.tools import BaseTool
from rdkit import Chem
from rdkit.Chem import Descriptors

DESC = """
Use this tool when you need to calculate the log of the partition coefficient (LogP) of a compound.
"""


class CalculateLogP(BaseTool):
    name = "CalculateLogP"
    description = DESC

    def _run(self, compound_smiles: str) -> float:
        """
        RdKit descriptor module to calculate LogP from the atom based Crippen approach
        https://www.rdkit.org/docs/source/rdkit.Chem.Descriptors.html
        https://www.rdkit.org/docs/source/rdkit.Chem.Crippen.html
        """
        mol = Chem.MolFromSmiles(compound_smiles)
        return Descriptors.MolLogP(mol)

    async def _arun(self, compound_smiles: str) -> float:
        """Use the calculate_logp tool asynchronously."""
        raise NotImplementedError()
