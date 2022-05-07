import schedule
import requests

def dailytasks():
    to_do = {
        '06:30': 'Go jogging',
        '10:00': 'Become an Expert',
        '15:00': 'Challenge yourself',
        '20:00': 'Do something different',
        '23:30': 'Back to the Earth',
            }

    print("Day's tasks")
    for k, v in to_do.items():
        print(f'{k} - {v}')

    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"

    print(btc_price)


def main():

    #schedule.every(4).seconds.do(dailytasks)
	#schedule.every(5).minutes.do(dailytasks)
	#schedule.every().hour.do(dailytasks)
    #schedule.every().day.at('15:45').do(dailytasks)
    #schedule.every().thursday.do(dailytasks)
    #schedule.every().saturday.at('19:59').do(dailytasks)

    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()
