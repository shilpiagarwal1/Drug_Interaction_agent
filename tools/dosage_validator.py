def verify_dosage(drug, dosage, age, weight):
    if drug.lower() == "paracetamol":
        if dosage > weight*15:
            return "Overdose risk"
    return "Dosage OK"
