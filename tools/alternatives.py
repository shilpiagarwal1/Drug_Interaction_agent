def suggest_alternatives(drug):
    return {"aspirin":["clopidogrel"]}.get(drug.lower(), ["consult doctor"])
