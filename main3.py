# coding : utf-8
# 文字コードの宣言
# 買い物プログラム
# 買い物かごの内容を管理
# 重複した要素の検知

# 買い物かごクラス
class Cart():
    def __init__(self):
        self.contents = []


# 買い物かごの内容のクラス
class Cart_content():
    def __init__(self, product, number):
        self.product = product
        self.number = number

# 商品のクラス
class Product():
    def __init__(self, name, price):
        self.name = name 
        self.price = price

# 残金
money = 0

# 購入した商品のリスト
cart = []

# りんご
apple = Product("りんご", 500)

# バナナ
banana = Product("バナナ", 400)

# ぶどう
grape = Product( "ぶどう",300)

# 果物のリスト
fruits = (apple, banana, grape)

# 個数
count = 0

#
# 計算
# 

# 残金を計算して表示する関数
def balance(money, total_price):
    result = ""
    # 合計金額が残金より小さい場合
    if total_price < money:
        result = "残金は" + str(money - total_price) + "です"

    # 合計金額が残金と等しい場合
    elif total_price == money:
        result = "残金は０です"

    # 合計金額が残金より大きい場合
    elif total_price > money:
        result = "今の所持金では買えません"
    return result

# 所持金を設定
money = input("金額を入力してください")
money = int(money)

# 商品の選択
def select_product():
    # 購入する商品を選択
    item = input("商品を選択してください（りんご：0、バナナ：1、ブドウ：2）")
    item = int(item)
    # 購入する個数を選択
    count = input("購入する個数を入力してください")
    count = int(count)
    # 買い物かごに選んだ商品を追加
    cart_content = Cart_content(fruits[item], count)
    cart.append(cart_content)
    # 買い物かごの内容を表示
    decision = input("購入した商品を確認しますか？　（はい：０、いいえ：１）")
    decision = int(decision)
    if decision == 0:
        for val in cart:
            print(val.product.name + "単価 ￥" + str(val.product.price) + "\n購入数" + str(val.number))

    # 買い物かごから中身を出す
    decision = input("買い物かごの中の商品の購入を中断しますか？　（はい：０、いいえ：１）")
    decision = int(decision)
    if decision == 0:

        num = 0
        for val in cart:
            print(str(num) + val.product.name + "単価 ￥" + str(val.product.price) + "\n購入数" + str(val.number))
            num += 1
        num = 0

        selection = input('''購入を取りやめる商品を選んでください''')
        selection = int(selection)
        del cart[selection]

        num = 0
        for val in cart:
            print(str(num) + val.product.name + "単価 ￥" + str(val.product.price) + "\n購入数" + str(val.number))
            num += 1
        num = 0   

    # 購入を続けるか終わるかを選択する
    decision = input("商品の購入を続けますか？　（はい：０、いいえ：１）")

    if decision == "0":
        select_product()


# 動作確認
select_product()

# 重複する要素の検知
for val1 in cart:
    print(val1)
    print(val1.product.name)
    i = 0
    for val2 in cart:
        print(val2)
        print(val2.product.name)
        if val1.product.name == val2.product.name and val1 != val2:
            print("この要素は重複しています")
            val1.number = val1.number + val2.number
            del cart[i]
            print("重複した要素を統合しました")
        i += 1

for val in cart:
    print(val.product.name + "単価 ￥" + str(val.product.price) + "\n購入数" + str(val.number))

# 合計金額
total_price = 0

for val in cart:
    total_price += val.product.price * val.number

print("合計金額は￥" + str(total_price) + "です")

# 結果を表示する
print(balance(money, total_price))