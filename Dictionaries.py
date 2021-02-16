print()
print("Greetings! And welcome to your stock price checker.")
print()
#Create a new dictionary with 10 ticker symbols and their prices
program_dict = {"BPYU": 17.05, 'NRG': 41.93, 'NLOK': 20.66, "BIO": 588.34, "XRX": 20.75, 'ZM': 391.83, 'BDN': 11.45, 'ROK': 260.85, 'AGCO': 112.14, 'UNVR': 19.81}
#Allow user to input their stock ticker symbol to see price
userstock = input("To check the price of a stock, please enter its ticker symbol: ")
print()
if userstock in program_dict:
    print("The price for", userstock, "is: ", program_dict[userstock])
    print()
else:
    print('Stock ticker symbol wasn’t found. Please try again!')
    print()