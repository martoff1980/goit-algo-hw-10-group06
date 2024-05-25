import pulp

# Ініціалізація моделі
model = pulp.LpProblem("MaxProductivity", pulp.LpMaximize)

# Визначення змінних
# Кількість продукту "Лимонад"
A = pulp.LpVariable('Limonad', lowBound=0, cat='Integer')
# Кількість продукту "Фруктовий сік"
B = pulp.LpVariable('FructJuice', lowBound=0,  cat='Integer')

# Функція цілі (Максимізація виробницства)
model += A + B, "Productivity"

# Додавання обмежень
model += 2*A + 1*B <= 100, "Water"  # Вода
model += 1*A+0*B <= 50, "Sugar"  # Сахар
model += 1*A+0*B <= 30, "LimonJuice"  # Лімоний сік
model += 0*A+1*B <= 40, "FructPure"  # Фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Виробляти продукт {A.name} в кількості: {A.varValue}")
print(f"Виробляти продукт {B.name} в кількості: {B.varValue}")
