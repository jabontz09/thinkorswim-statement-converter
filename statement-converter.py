import pandas as pd
from io import StringIO

file = '2022-06-21-AccountStatement.csv'

with open(file, 'r') as f:
    string_csv = ' '.join(f.readlines())
    index = string_csv.find("Account Trade History")
    trade_history = string_csv.split("Account Trade History")[1].split(',', 1)[1].split('Profits and Losses')[0]

#df = pd.read_csv(trade_history)

f = StringIO(trade_history)
df = pd.read_csv(f)

df = df.sort_values(by="Exec Time", ascending=True)

print(df)

def calculate_average_price(current_avg, current_quantity, new_price, new_quantity):
  """
  Calculates the updated average close price after a new trade, given the current average and quantities.

  Args:
    current_avg: The current average close price.
    current_quantity: The total quantity of shares before the new trade.
    new_price: The price of the new trade.
    new_quantity: The quantity of shares in the new trade.

  Returns:
    The updated average close price as a float.
  """

  total_cost = current_avg * current_quantity + new_price * new_quantity
  total_shares = current_quantity + new_quantity
  updated_average__price = total_cost / total_shares
  return updated_average__price

def calculate_profit(side, buy_price, buy_qty, sell_price, sell_qty):
    profit = 0
    if side == 'SELL':
        profit = buy_price * buy_qty - sell_price * sell_qty
    else:
        profit = sell_price * sell_qty - buy_price * buy_qty

    return profit

def aggregate_trades(dataframe):
    trades = []

    for index, row in dataframe.iterrows():
        trade_found = False
        # Check if the key exists in any dictionary:
        for index, trade in enumerate(trades):
            if trade["symbol"] == row['Symbol'] and trade['status'] is not 'CLOSED':
                trade_found = True
                if trade["side"] != row["Side"]:
                    trade["avg_close_price"] = calculate_average_price(trade["avg_close_price"], trade["close_quantity"], row["Price"], abs(row["Qty"]))
                    trade["close_quantity"] += abs(row['Qty'])
                    if trade["close_quantity"] == trade["open_quantity"]:
                        trade["close_time"] = row['Exec Time']
                        trade["status"] = 'CLOSED'
                        trade["profit"] = calculate_profit(trade["side"], trade["avg_open_price"], trade["open_quantity"], trade["avg_close_price"], trade["close_quantity"])

                else:
                    trade["avg_open_price"] = calculate_average_price(trade["avg_open_price"], trade["open_quantity"], row["Price"], abs(row["Qty"]))
                    trade["open_quantity"] += abs(row['Qty'])

        if trade_found == False:
            new_trade = {}
            new_trade['open_time'] = row['Exec Time']
            new_trade['status'] = 'OPEN'
            new_trade['side'] = row['Side']
            new_trade['open_quantity'] = abs(row['Qty'])
            new_trade['symbol'] = row['Symbol']
            new_trade['avg_open_price'] = row['Price']
            new_trade['close_quantity'] = 0
            new_trade['avg_close_price'] = 0

            trades.append(new_trade)

    return pd.DataFrame(trades)
                  
aggregated = aggregate_trades(df)

aggregated.to_csv(f'./converted/{file}-aggregated.csv')

print(aggregated)

