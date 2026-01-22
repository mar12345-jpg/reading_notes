import json

def main():
    with open("data.json", encoding="UTF-8") as f:
        data = json.load(f)

    result = {}

    for item in data:
        if item["category"] not in result:
            result[item["category"]] = []

        if item["price"] >= 1000:
            result[item["category"]].append(item["name"])

    for k in result:
        print(k)
        for v in result[k]:
            print(" - " + v)

if __name__ == "__main__":
    main()