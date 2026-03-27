from langchain.tools import tool
from tools.interaction_checker import check_interactions
from tools.dosage_validator import verify_dosage
from tools.allergy_checker import check_allergies
from tools.alternatives import suggest_alternatives

@tool
def interaction_tool(drugs: list) -> str:
    """Check drug-drug interactions and return severity and description."""
    return str(check_interactions(drugs))


@tool
def dosage_tool(data: dict) -> str:
    """Validate dosage using patient age and weight."""
    return verify_dosage(
        data["drug"],
        data["dosage"],
        data["age"],
        data["weight"]
    )


@tool
def allergy_tool(data: dict) -> str:
    """Check if patient allergies conflict with given drugs."""
    return check_allergies(
        data["drugs"],
        data["allergies"]
    )


@tool
def alternatives_tool(drug: str) -> str:
    """Suggest safer alternative medications."""
    return str(suggest_alternatives(drug))