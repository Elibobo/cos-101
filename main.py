#########  mr yusuf

print("MR . YUSUF AND SONS ")
print("To calculate simple interest, enter the required details.")
initial_prinicipal = float(input("Enter your initial prinicipal: "))
interest_rate = float(input("Enter your initial rate: "))
number_of_times_interest_per_time_period = float(input("Enter number of times interest per time period: "))
number_of_time_period_elapse = float(input("Enter your number of time period elapsed: "))

simple_interest = initial_prinicipal *(1 + interest_rate * number_of_times_interest_per_time_period)
compound_interest = initial_prinicipal *(1 +(interest_rate/number_of_time_period_elapse))**number_of_time_period_elapse*number_of_times_interest_per_time_period

print("YUSUF AND SONS COMPANY")
print(f'simple interest : {simple_interest}')
print(f'compound interest : {compound_interest}')