def calculate_julian_day(year:int, month:int, day:int):
    # Adjustment for January and February
    if month == 1 or month == 2:
        month += 12  # January → 13, February → 14
        year -= 1

    julian = (36525 * year) // 100 + (306001 * (month + 1)) // 10000 + day + 1720981
    return julian

try:
    # Ask the user for year, month, and day as integers
    year = int(input("Enter year (e.g., 2008): "))
    month = int(input("Enter month (1=Jan-12=Dec): "))
    day = int(input("Enter day of the month: "))

    julian_day = calculate_julian_day(year, month, day)
    print(f"The Julian day is: {julian_day}")

except ValueError:
    print("Invalid input. Please enter integer values for year, month, and day.")






