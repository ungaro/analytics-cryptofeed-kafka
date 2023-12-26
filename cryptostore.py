'''
Copyright (C) 2018-2023 Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from datetime import datetime
from decimal import Decimal

from cryptofeed import FeedHandler
from cryptofeed.defines import GOOD_TIL_CANCELED, L2_BOOK, LIMIT, SELL, TICKER, TRADES
from cryptofeed.exchanges import Binance, BinanceDelivery, BinanceFutures


#info = BinanceDelivery.info()



# Examples of some handlers for different updates. These currently don't do much.
# Handlers should conform to the patterns/signatures in callback.py
# Handlers can be normal methods/functions or async. The feedhandler is paused
# while the callbacks are being handled (unless they in turn await other functions or I/O)
# so they should be as lightweight as possible
'''
async def ticker(t, receipt_timestamp):
    if t.timestamp is not None:
        assert isinstance(t.timestamp, float)
    assert isinstance(t.exchange, str)
    assert isinstance(t.bid, Decimal)
    assert isinstance(t.ask, Decimal)
    print(f'Ticker received at {receipt_timestamp}: {t}')
'''
'''
async def trade(t, receipt_timestamp):
    assert isinstance(t.timestamp, float)
    assert isinstance(t.side, str)
    assert isinstance(t.amount, Decimal)
    assert isinstance(t.price, Decimal)
    assert isinstance(t.exchange, str)
    print(f"Trade received at {receipt_timestamp}: {t}")
'''

async def book(book, receipt_timestamp):
    print(f'Book received at {receipt_timestamp} for {book.exchange} - {book.symbol}, with {len(book.book)} entries. Top of book prices: {book.book.asks.index(0)[0]} - {book.book.bids.index(0)[0]}')
    if book.delta:
        print(f"Delta from last book contains {len(book.delta[BID]) + len(book.delta[ASK])} entries.")
    if book.sequence_number:
        assert isinstance(book.sequence_number, int)



async def abook(book, receipt_timestamp):
    print(f'BOOK lag: {receipt_timestamp - book.timestamp} Timestamp: {datetime.fromtimestamp(book.timestamp)} Receipt Timestamp: {datetime.fromtimestamp(receipt_timestamp)}')

'''
async def ticker(t, receipt_timestamp):
    if t.timestamp is not None:
        assert isinstance(t.timestamp, float)
    assert isinstance(t.exchange, str)
    assert isinstance(t.bid, Decimal)
    assert isinstance(t.ask, Decimal)
    print(f'Ticker received at {receipt_timestamp}: {t}')
'''

async def trades(t, receipt_timestamp):
    assert isinstance(t.timestamp, float)
    assert isinstance(t.side, str)
    assert isinstance(t.amount, Decimal)
    assert isinstance(t.price, Decimal)
    assert isinstance(t.exchange, str)
    print(f"Trade received at {receipt_timestamp}: {t}")

async def ticker(t, receipt_timestamp):
    print("TICKER: ",t)


async def trade(t, receipt_timestamp):
    print("TRADE:",t)
    
    
def main():
    path_to_config = 'config.yaml'
    
    #binance = Binance(config=path_to_config)
    #print(binance.balances_sync())
    #print(binance.orders_sync())
    #order = binance.place_order_sync('BTC-USDT', SELL, LIMIT, 0.002, 80000, time_in_force=GOOD_TIL_CANCELED, test=False)
    #print(binance.orders_sync(symbol='BTC-USDT'))
    #print(order)
    #print(binance.cancel_order_sync(order['orderId'], symbol='BTC-USDT'))
    #print(binance.orders_sync(symbol='BTC-USDT'))

    '''
    binance_delivery = BinanceDelivery(config=path_to_config)
    
    print(binance_delivery.balances_sync())
    print(binance_delivery.orders_sync())
    print(binance_delivery.positions_sync())
    order = binance_delivery.place_order_sync('ETH-USD-PERP', SELL, LIMIT, 0.05, 5000, time_in_force=GOOD_TIL_CANCELED, test=False)
    print(binance_delivery.orders_sync(symbol='BTC-USDT-PERP'))
    print(binance_delivery.orders_sync(symbol='ETH-USDT-PERP'))
    print(order)
    print(binance_delivery.cancel_order_sync(order['orderId'], symbol='ETH-USDT-PERP'))
    print(binance_delivery.orders_sync(symbol='ETH-USDT-PERP'))
    '''
    f = FeedHandler()
    #f.add_feed(Binance(symbols=['BTC-USDT'], channels=[L2_BOOK], callbacks={L2_BOOK: book,  TRADES: trade, TICKER: ticker}))
    f.add_feed(Binance(symbols=['ETH-USDT'], channels=[TRADES, TICKER], callbacks={TICKER: ticker, TRADES: trade}))


    f.run()


if __name__ == '__main__':
    main()