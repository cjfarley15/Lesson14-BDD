import datetime


def date_calc():
    print("Social Security Full Retirement Age Calculator ")

    while 1:
        birth_y = input("\n\nEnter the year of birth or exit: ")
        if birth_y == "":
            print("\nProcess finished with exit code 0")
            break
        else:
            birth_y = int(birth_y)
            birth_m = int(input("\nEnter the month of birth: "))
            current_y = datetime.datetime.now().strftime("%Y")
            if birth_y < 1937 or birth_y == 1937 and birth_y > 1850:
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 65 and 0 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 65))
            elif birth_y == 1938:
                birth_m += 2
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 65 and 2 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 65))
            elif birth_y == 1939:
                birth_m += 4
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 65 and 4 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 65))
            elif birth_y == 1940:
                birth_m += 6
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 65 and 6 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 65))
            elif birth_y == 1941:
                birth_m += 8
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 65 and 8 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 65))
            elif birth_y == 1942:
                birth_m += 10
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 65 and 10 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 65))
            elif birth_y == 1943 or birth_y > 1943 and birth_y == 1954 or birth_y < 1954:
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 66 and 0 months")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 66))
            elif birth_y == 1955:
                birth_m += 2
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 66 and 2 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 66))
            elif birth_y == 1956:
                birth_m += 4
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 66 and 4 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 66))
            elif birth_y == 1957:
                birth_m += 6
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 66 and 6 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 66))
            elif birth_y == 1958:
                birth_m += 8
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 66 and 8 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 66))
            elif birth_y == 1959:
                birth_m += 10
                if birth_m > 12:
                    birth_m -= 12
                    birth_y += 1
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 66 and 10 months ")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 66))
            elif birth_y == 1960 or 1960 and birth_y < int(current_y):
                current_m = datetime.date(1950, birth_m, 1).strftime('%B')
                print("\nYour full retirement age is 67 and 0 months")
                print("\nThis will be in {} of".format(current_m) + " {}.".format(birth_y + 67))


class RetirementCalculator:
    date_calc()
