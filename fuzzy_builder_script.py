def score(dp, p70, pib, dc, nl):
    final_score = dp + p70 + pib + dc + nl
    if 5 <= final_score <= 7:
        return 1
    elif 8 <= final_score <= 9:
        return 2
    elif 10 <= final_score <= 11:
        return 3
    elif 12 <= final_score <= 13:
        return 4
    elif 14 <= final_score <= 15:
        return 5

densidade_pop = [(1,'baixa', 1), (2,'media', 2), (3,'alta', 3)]
pocentagem_70_pop = [(1,'baixa', 1), (2,'media', 2), (3,'alta', 3)]
pib_per_capita = [(1,'baixa', 3), (2,'media', 2), (3,'alta', 1), (4,'alta', 1)]
doenca_cronica = [(1,'baixa', 1), (2,'media', 2), (3,'alta', 3)]
# testex1000 = [(1,'baixa', 3), (2,'media', 2), (3,'alta', 1)]
num_leitos = [(1,'baixa', 3), (2,'media', 2), (3,'alta', 1)]
logical_and = 1
weight = '(1)'

for dp in densidade_pop:
    for p70 in pocentagem_70_pop:
        for pib in pib_per_capita:
            for dc in doenca_cronica:
                for nl in num_leitos:
                    print(dp[0], p70[0], pib[0], dc[0], nl[0], ',',
                          score(dp[2], p70[2], pib[2], dc[2], nl[2]), weight, ':', logical_and )
