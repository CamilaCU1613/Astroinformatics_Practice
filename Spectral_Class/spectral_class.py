def get_spectral_class(temp):
    """
    Determines the spectral class of a star based on its surface temperature. This function classifies stars into spectral types based on their effective surface temperature (in Kelvin). The classification follows the standard OBAFGKM scheme, ranging from hot, massive stars to cool, low-mass stars.
    
    Arguments:
    temp (int): The star's surface temperature in Kelvin.
    
    Returns:
    str or None: The spectral class as a single-letter string ("O", "B", ..., "M"),
    or None if the temperature is outside the known classification range.
    
    Spectral Classification:
    - O: 30,000–60,000 K
    - B: 10,000–29,999 K
    - A: 7,500–9,999 K
    - F: 6,000–7,499 K
    - G: 5,000–5,999 K
    - K: 3500–4999 K
    - M: 2000–3499 K
    
    Command-line usage:
    The script prompts the user to enter the stellar temperature via standard input:
    Enter the star's temperature in Kelvin: 5800
    → The spectral class is G.
    
    Notes:
    - If the input temperature is less than 2000 K or greater than 60,000 K, the function returns "None", indicating that the star lies outside the main spectral sequence.
    - The input must be a valid integer. Invalid (non-numeric) input is handled with an error message.
    ""

    
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


