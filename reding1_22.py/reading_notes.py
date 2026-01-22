import json
# jsonファイルが読めるようにインポート

def main():
    with open("data.json", encoding="UTF-8") as f:
        data = json.load(f)
# 文字コードUTF-8でjsonファイル読むよ、名前はf

    result = {}
# jsonファイルのデータを引数無しでresultにセット

    for item in data:
        if item["category"] not in result:
            result[item["category"]] = []
# if not がどうなってるの？

        if item["price"] >= 1000:
            result[item["category"]].append(item["name"])
# 1000円以上のやつはTRUE、カテゴリーと名前で表示できるようにしておく

    for k in result:
        print(k)
        for v in result[k]:
            print(" - " + v)
# jsonファイルの中身表示と、-つけてkの中身全部表示して

if __name__ == "__main__":
    main()