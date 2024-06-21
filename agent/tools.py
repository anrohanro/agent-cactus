"""Script for loading tools for the Cactus Agent."""

from cactus.tools import (
    BrenkFilter,
    CalculateBBBPermeant,
    CalculateDruglikeness,
    CalculateGIAbsorption,
    CalculateLogP,
    CalculateMolWt,
    CalculateQED,
    CalculateSA,
    CalculateTPSA,
    PainsFilter,
    Calculate_pIC50,
)


def make_tools():
    """Method for aggregating and generating a list of tools for the LLM Agent"""

    all_tools = [
        # InchikeyToSMILES(),
        # NameToSMILES(),
        # CasToSMILES(),
        # ChemblidToSMILES(),
        # CidToSMILES(),
        # MolecularFormulaToSMILES(),
        # ZincIDToSMILES(),
        Calculate_pIC50(),
        CalculateMolWt(),
        CalculateQED(),
        BrenkFilter(),
        CalculateTPSA(),
        CalculateBBBPermeant(),
        CalculateDruglikeness(),
        CalculateGIAbsorption(),
        CalculateLogP(),
        PainsFilter(),
        CalculateSA(),
    ]

    return all_tools
