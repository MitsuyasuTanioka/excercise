# Sell_start_day(開始日)の方がSell_finish_day(終了日)よりも早い日にちになるように定める
Sell_start_day = 24
Sell_finish_day = 30

if Sell_start_day < Sell_finish_day < 10 or 15 < Sell_start_day < Sell_finish_day:
    print("重複はありません")
else:
    print("注意、重複があります！")
