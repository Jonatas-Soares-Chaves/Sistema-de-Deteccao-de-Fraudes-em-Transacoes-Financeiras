def calcular_risco(row):
    score = 0

    if row["valor"] > 3000:
        score += 50

    if row["local"] != "BR":
        score += 20

    return score


def classificar(score):
    if score >= 50:
        return "ALTO_RISCO"
    elif score >= 20:
        return "MEDIO_RISCO"
    return "BAIXO_RISCO"