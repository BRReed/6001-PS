# house hunting

def forever():
    try:
        annual_salary = int(input('What is your annual salary?\n>'))
    except ValueError:
        print('You must enter a number')
        return
    monthly_salary = int(annual_salary / 12)
    try:
        portion_saved = float(input('What would you like to save?\n>'))
    except ValueError:
        print('You must enter a number')
        return
    try:
        total_cost = int(input('What is the total cost of your home?\n>'))
    except ValueError:
        print('You must enter a number')
        return
    try:
        semi_annual_raise = float(input('What is your semi-annual raise?\n>'))
    except ValueError:
        print('You must enter a number')
        return
    r = .04
    portion_down_payment = total_cost * .25
    current_savings = 0
    months = 0
    while current_savings < portion_down_payment:

        current_savings += int((monthly_salary * portion_saved) + (current_savings * (r / 12)))
        months += 1
        if months % 6 == 0:
            annual_salary += int(annual_salary * semi_annual_raise)
            monthly_salary = int(annual_salary / 12)


    print(f'Annual salary: {annual_salary}')
    print(f'Percent of your salary to save: {portion_saved}')
    print(f'Cost of your dream home: {total_cost}')
    print(f'Number of months: {months}')

forever()