import json
# jsonファイルが読めるようにインポート

def main():
    with open("data.json", encoding="UTF-8") as f:
        data = json.load(f)
# fにjsonファイル入れて、pythonデータに変換してdataに入れる

    result = {}
# 空の辞書をrerultにセット

    for item in data:
        if item["category"] not in result:
            result[item["category"]] = []
# categoryがまだresultにセットされてなければTrue
# resultのcategory用の空のリストを用意

        if item["price"] >= 1000:
            result[item["category"]].append(item["name"])
# 1000円以上のやつはTRUE
# そのcategoryに名前を追加

    for k in result:
        print(k)
        for v in result[k]:
            print(" - " + v)
# kはカテゴリ名で
# カテゴリ別に商品をひとつずつ表示

if __name__ == "__main__":
    main()