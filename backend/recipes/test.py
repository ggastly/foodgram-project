shopping_list = [('мука', 300, 'г'), ('тыква', 500, 'г')]
result = []
for ingredient in shopping_list:
    result.append(f'{ingredient[0]} ({ingredient[2]}) – {ingredient[1]}\n')
print(*result)