import json
from itertools import combinations

def load_data():
    with open("data/medical_knowledge/drug_interactions.json") as f:
        return json.load(f)

def check_interactions(drugs):
    data = load_data()
    results = []
    for d1, d2 in combinations(drugs, 2):
        for r in data:
            if {d1.lower(), d2.lower()} == {r["drug_1"], r["drug_2"]}:
                results.append(r)
    return results if results else "No known interactions found."
