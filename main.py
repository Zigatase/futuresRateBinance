import requests
import datetime


# Класс Binance Api хранит в себе хедер запроса и ссылку к апи
class BinanceApi:
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    url = "https://www.binance.com/fapi/v1/ticker/price?symbol=ETHUSDT"


# Дергаем Binance Api и получаем прайс фьючерса на пару ETH-USDT
def get_price_eth_usdt():
    response = requests.get(url=BinanceApi.url, headers=BinanceApi.headers).json()["price"]

    return response


def data_analysis():
    # Делаем try -> except обертку на случай возникновения ошибок при сборе
    try:
        # Запоминаем время входа на рынок
        ENTRY_POINT_TIME = datetime.datetime.now()

        # Запоминаем прайс входа на рынок
        ENTRY_POINT_PRICE = float(get_price_eth_usdt())

        # Выводим в консоль Прайс и Время входа
        print(f"--- Data: {ENTRY_POINT_TIME} ---"
              f"\n--- Price ETH-USDT: {ENTRY_POINT_PRICE} ---")

        while True:
            # Записываем цену в моменте получения данных
            moment_price_eth_usdt = float(get_price_eth_usdt())

            # Если цена поднялась, то мы выводи сообщение об этом
            if moment_price_eth_usdt > (ENTRY_POINT_PRICE * 1.01):
                print(f"\n\n --- Прайс вырос на 1 процент от точки входа: {moment_price_eth_usdt} ---\n\n")

            # Если цена не поднялась, то мы пишем об этом (можно выключить для оптимизации программы)
            else:
                print(f"\n --- Прайс не вырос на 1 процент от точки входа: {moment_price_eth_usdt} ---")

    # Ловим и выводим ошибку если она появляется (Сделал except общего вида)
    except Exception as ex:
        print(f"\n\n !!! Ошибка !!!\n\n"
              f"{ex}")


def main():
    data_analysis()


if __name__ == '__main__':
    main()
