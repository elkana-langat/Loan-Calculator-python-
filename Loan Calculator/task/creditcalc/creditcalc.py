import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()
args_dict = vars(parser.parse_args())
new_list = []
for obj in args_dict.items():
    if obj[1] != None:
        new_list.append(obj[0])

len_of_arguments = len(new_list)

if len_of_arguments != 4:
    print("Incorrect parameters.")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters.")
else:
    # function to calculate the differentiated payments
    def differentiated_pay(p, n, i):
        i = (i / (12 * 100))
        sum = 0

        for j in range(1, n + 1):
            # payment for each month
            first = (p / n)
            #  print(first)
            second = (p * (j - 1)) / n
            # print(second)
            third = p - second
            # print(third)
            four = (i * third)
            # print(four)
            d = math.ceil(first + four)
            sum += d
            print(f"Month {j}: payment is {d}")

        overpayment = int(sum - args.principal)
        print()
        print(f"Overpayment = {overpayment}")


    # function to calculate the annuity payment
    def annuity_pay(i, j, loan_interest):
        if args.principal is None:
            # nominal interest rate
            interest = (loan_interest / (12 * 100))
            # monthly payment
            x = math.pow((1 + interest), j)
            n = ((interest * x) / (x - 1))
            loan_principal = math.floor(i / n)
            overpayment = math.ceil((i * j) - (i / n))

            print(f"Your loan principal = {loan_principal}!")
            print(f"Overpayment = {overpayment}")
        elif args.payment is None:
            loan_principal = i
            number_of_periods = j
            loan_interest = loan_interest
            # nominal interest rate
            z = (loan_interest / (12 * 100))
            # monthly payment
            x = math.pow((1 + z), number_of_periods)
            n = ((z * x) / (x - 1))
            n *= loan_principal
            n = math.ceil(n)
            overpayment = round((n * number_of_periods) - loan_principal)

            print(f"Your annuity payment = {n}!")
            print(f"Overpayment = {overpayment}")
        elif args.periods is None:
            loan_principal = i
            monthly_payments = j
            loan_interest = loan_interest
            # nominal_interest_rate\
            z = (loan_interest / (12 * 100))
            base = 1 + z
            x = (monthly_payments / (monthly_payments - z * loan_principal))
            # number of months
            n = math.ceil(math.log(x, base))
            years = n // 12
            months = n % 12
            overpayment = round((monthly_payments * n) - loan_principal)

            if months != 0:
                print(f"It will take {years} years and {months} months to repay this loan!")
            else:
                print(f"It will take {years} years to repay this loan!")
            print(f"Overpayment = {overpayment}")


    if args.type == "annuity":
        if args_dict["principal"] is None:
            annuity_pay(args.payment, args.periods, args.interest)
        elif args_dict["payment"] is None:
            annuity_pay(args.principal, args.periods, args.interest)
        elif args_dict["periods"] is None:
            annuity_pay(args.principal, args.payment, args.interest)
    elif args.type == "diff":
        differentiated_pay(args.principal, args.periods, args.interest)
