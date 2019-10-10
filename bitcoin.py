import requests
def main():

    bitcoins = getCoins()
    rate = getBitcoinRate()
    usdWorth = convert(rate, bitcoins)



    print(f'{bitcoins} bitcoin is/are worth {usdWorth:.2f} in USD')


def getBitcoinRate():
    data2 = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    rate = data2['bpi']['USD']['rate']
    return rate

def convert(rate, bitcoins):
    try:
        commas_removed = float(rate)
    except:
        commas_removed = float(rate.replace(',', ''))
    usdWorth = (bitcoins * commas_removed)
    return usdWorth
def getCoins():
    while True:
        try:
            bitcoins = float(input("Enter the number of bitcoins you would like to calculate to USD"))
            break
        except:
            print("Enter a number")
    return bitcoins
if __name__ == '__main__':
    main()

##this program gets a user input for number of bitcoins to convert, pulls the rate in usd from an api
##and calculates the usd value for the amount of bitcoins