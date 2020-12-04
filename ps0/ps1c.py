# house hunting
# raise .07, annual roi .04, target down .25, house cost 1M
# find the amount you need to save per month in order
# to have 25% of total cost at 36 months



def forever():
    annual_salary = 10000
    monthly_salary = int(annual_salary / 12)
    total_cost = 1000000
    portion_down_payment = total_cost * .25
    roi = .04
    months = 36
    down = round(total_cost * .25, 2)
    total_saved = 0
    bisec_search = 0
    percent_bot = 0
    percent_top = 100
    if monthly_salary * months < portion_down_payment:
        print('It is impossible for you to do this')
        return
    while True:
        bisec_search += 1
        print(bisec_search)
        percent_mid = round((percent_top + percent_bot) / 2, 2)
        total_saved = round((percent_mid / 100) * monthly_salary * 36 + 
                            (total_saved * (roi / 12)), 2)
        print(f'Total saved: {total_saved}')
        if total_saved - down >= -100.00 and total_saved - down <= 100.00:
            print(percent_bot)
            print(percent_mid)
            print(percent_top)
            break
        elif total_saved < down:
            percent_bot = percent_mid
        elif total_saved > down:
            percent_top = percent_mid
        else:
            print(f'saved: {total_saved}')
        print(percent_mid)

    print(f'Annual salary: {annual_salary}')
    print(f'Cost of your dream home: {total_cost}')
    print(f'Number of bisections required: {bisec_search}')
    print(f'total saved - down : {round(total_saved - down, 2)}')





forever()
