# coding : utf-8
# 文字コードの宣言
#買い物プログラム

# 残金
money = 0


# 商品毎の単価
# りんご
apple = {"name": "りんご", "price": 500}

#  = {"name": "", "price": }

# バナナ
banana = {"name": "バナナ", "price": 400}

# ぶどう
grape = {"name": "ぶどう", "price": 300}

# 果物のリスト
fruits = {"apple":apple, "banana":banana, "grape":grape}
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
options = ["apple", "banana", "grape"]

item = input("商品を選択してください（りんご：0、バナナ：1、ブドウ：2）")
print(options[int(item)])
item = int(item)

# 購入する個数を選択
count = input("購入する個数を入力してください")
count = int(count)

# 合計金額
total_price = fruits[options[int(item)]]["price"] * count

# 結果を表示する
# 合計金額が残金より小さい場合
if total_price < money:
    print(fruits[options[item]]["name"] + "を" + str(count) + "個買いました")
    print("残金は" + str(money - total_price) + "です")
# 合計金額が残金と等しい場合
elif total_price == money:
    print(str(fruits[options[item]]["name"]) + "を" + str(count) + "個買いました")
    print("残金は０です")   
# 合計金額が残金より大きい場合
elif total_price > money:
    print("今の所持金では買えません")