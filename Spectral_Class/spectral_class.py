def get_spectral_class(temp):
    if 30000 <= temp <= 60000:
        return "O"
    elif 10000 <= temp < 30000:
        return "B"
    elif 7500 <= temp < 10000:
        return "A"
    elif 6000 <= temp < 7500:
        return "F"
    elif 5000 <= temp < 6000:
        return "G"
    elif 3500 <= temp < 5000:
        return "K"
    elif 2000 <= temp < 3500:
        return "M"
    else:
        return None

try:
    temp = int(input("Enter the star's temperature in Kelvin: "))
    spectral_class = get_spectral_class(temp)
    
    if spectral_class:
        print(f"The spectral class is {spectral_class}.")
    else:
        print("Temperature out of known spectral class range.")
except ValueError:
    print("Invalid input. Please enter a numeric temperature.")


