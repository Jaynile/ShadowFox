
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}


total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())


print(f"Total expenses for you: ${total_your_expenses}")
print(f"Total expenses for your partner: ${total_partner_expenses}")

if total_your_expenses > total_partner_expenses:
    print("You spent more money overall.")
elif total_your_expenses < total_partner_expenses:
    print("Your partner spent more money overall.")
else:
    print("You and your partner spent the same amount overall.")


categories = set(your_expenses.keys()).union(partner_expenses.keys())
max_difference = 0
max_difference_category = ""

for category in categories:
    your_amount = your_expenses.get(category, 0)
    partner_amount = partner_expenses.get(category, 0)
    difference = abs(your_amount - partner_amount)
    if difference > max_difference:
        max_difference = difference
        max_difference_category = category
print(f"The expense category with the most significant difference is '{max_difference_category}'.")
print(f"Difference in spending: ${max_difference}")
