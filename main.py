# coding : utf-8
# 文字コードの宣言
#買い物プログラム

# 残金
money = 0


# 商品毎の単価
# りんご
apple = ["りんご", 500]

#  = {"name": "", "price": }

# バナナ
banana = ["バナナ", 400]

# ぶどう
grape = ["ぶどう", 300]

# 果物のリスト
fruits = [apple, banana, grape]
print(fruits)

# 個数
count = 0

#
# 計算
# 

# 所持金を設定
money = input("金額を入力してください")
money = int(money)
# 購入する商品を選択
item = input("商品を選択してください（りんご：０、バナナ：１、ブドウ：２）")
item = int(item)

# 購入する個数を選択
count = input("購入する個数を入力してください")
count = int(count)

# 合計金額
fruit = fruits[item]
total_price = fruit[1] * count

# 結果を表示する
# 合計金額が残金より小さい場合
if total_price < money:
    print(str(fruits[item][0]) + "を" + str(count) + "個買いました")
    print("残金は" + str(money - total_price) + "です")
# 合計金額が残金と等しい場合
elif total_price == money:
    print(str(fruits[item][0]) + "を" + str(count) + "個買いました")
    print("残金は０です")   
# 合計金額が残金より大きい場合
elif total_price > money:
    print("今の所持金では買えません")