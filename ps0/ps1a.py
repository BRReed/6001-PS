# house hunting

# total_cost
# portion_down_payment = total_cost * .25
# current_savings = 0
# r = .04
# annual_salary
# portion_saved = .1
# monthly_salary = annual_salary / 12

def forever():
    try:
        annual_salary = int(input('What is your annual salary?\n>'))
    except ValueError:
        print('You must enter a number')
    monthly_salary = int(annual_salary / 12)
    try:
        portion_saved = float(input('What would you like to save?\n>'))
    except ValueError:
        print('You must enter a number')
    try:
        total_cost = int(input('What is the total cost of your home?\n>'))
    except ValueError:
        print('You must enter a number')
    r = .04
    portion_down_payment = total_cost * .25
    current_savings = 0
    months = 0
    while current_savings < portion_down_payment:
        current_savings += (monthly_salary * portion_saved) + (
                            current_savings * (r / 12))
        months += 1

    print(f'Annual salary: {annual_salary}')
    print(f'Percent of your salary to save: {portion_saved}')
    print(f'Cost of your dream home: {total_cost}')
    print(f'Number of months: {months}')

forever()