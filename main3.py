# coding : utf-8
# 文字コードの宣言
#買い物プログラム
# クラスの応用
# 関数の応用

# 残金
money = 0

# 商品毎の単価
class Product():
    def __init__(self, name, price):
        self.name = name 
        self.price = price

# りんご
apple = Product("りんご", 500)

# バナナ
banana = Product("バナナ", 400)

# ぶどう
grape = Product( "ぶどう",300)

# 果物のリスト
fruits = {"apple":apple, "banana":banana, "grape":grape}
fruits = [apple, banana, grape]


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
item = int(item)
print(fruits[item].name + " ￥" + str(fruits[item].price))

# 購入する個数を選択
count = input("購入する個数を入力してください")
count = int(count)

# 合計金額
total_price = fruits[item].price * count
print(total_price)

# 結果を表示する
# 合計金額が残金より小さい場合
if total_price < money:
    print("残金は" + str(money - total_price) + "です")
# # 合計金額が残金と等しい場合
elif total_price == money:
    print("残金は０です")
# # 合計金額が残金より大きい場合
elif total_price > money:
    print("今の所持金では買えません")