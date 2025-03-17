import requests
import os
import platform
import time
from colorama import Fore

# colors.
CYAN = Fore.CYAN
BLUE = Fore.BLUE
GREEN= Fore.GREEN
RED= Fore.RED
WHITE = Fore.WHITE

# function to clear the terminal.
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
while True:
    print(GREEN+"Welcome to the currency convertor.\n")
    time.sleep(1)
    try:
        currency1 = str(input(GREEN+"Type currency 1: ")).upper()
        time.sleep(0.5)
        currency2 = str(input("Type currency 2: ")).upper()
        time.sleep(0.5)
        qtd_converting = float(input(f"Type how much {currency1} you want to convert to {currency2}: "))  # Use float
        if qtd_converting <= 0:
            print(RED+"Error: Please insert a value more than 0")
            time.sleep(1)
            print("Restarting program...")
            time.sleep(5)
            clear()
            continue
        time.sleep(0.5)
        
        # api what suply currencies.
        api = f"https://economia.awesomeapi.com.br/json/last/{currency1}-{currency2}"
        # take all api data and simplify all.
        api_response = requests.get(api)
        data = api_response.json()
        
        currencies_converting = currency1+currency2
        currencies_converting = currencies_converting.replace(" ","")

        if currencies_converting not in data:
            print(RED+"Error: That currency does not exist or was not found!")
            time.sleep(1)
            print("Restarting program...")
            time.sleep(5)
            clear()
            continue

        currency_convert = float(data[currencies_converting]["bid"])  # Ensure float conversion
        qtd_converted = currency_convert * qtd_converting
        
        print(BLUE+ f"\nOne {CYAN}{currency1}{BLUE}, is equal: {WHITE}{currency_convert:.2f}{BLUE} {CYAN}{currency2}.")
        print(BLUE+ f"{qtd_converting} {currency1} is equal: {qtd_converted:.2f} {currency2}\n\n\n")
        
    except Exception as e:
        print(RED+f"Unexpected error: {e}")
        time.sleep(1)
        print("Restarting program...")
        time.sleep(5)
        clear()
        continue