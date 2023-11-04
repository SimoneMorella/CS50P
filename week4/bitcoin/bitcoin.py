import requests, sys

def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            json_f = r.json()
            bit_value = json_f["bpi"]["USD"]["rate_float"]
            print(f"${n * bit_value:,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
        except requests.RequestException:
            sys.exit("Difficulties in getting the request")
    else:
        sys.exit("Missing command-line argument")


main()