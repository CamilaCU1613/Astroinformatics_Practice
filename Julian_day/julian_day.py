def calculate_julian_day(year:int, month:int, day:int):
    """
    Calculates the Julian day number for a given Gregorian date.
    
    This function converts a Gregorian calendar date (year, month, day) to its corresponding Julian day number using the formula given in Practice 2.
    It automatically adjusts for January and February, treating them as the 13th and 14th months of the previous year.
    
    Arguments:
    year (int): The full year (e.g., 2024).
    month (int): The month number (1 = January, ..., 12 = December).
    day (int): The day of the month.
    
    Returns:
    int: The Julian day number corresponding to the entered date.
    
    Command-line usage:
    The script prompts the user to enter the date via standard input:
    Enter the year (e.g., 2008): 2024
    Enter the month (1 = Jan-12 = Dec): 7
    Enter the day of the month: 2
    
    Notes: This implementation uses a simplified, integer-based version of the Julian day formula, accurate for Gregorian calendar dates.
    ""
    
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






