import json
import os

with open("articles.json", "r", encoding="utf-8") as file:
    articles = json.load(file)

print("==============================")
print(" Project Sakura 記事管理")
print("==============================")

print()

print("==============================")
print(" Project Sakura 記事管理ツール")
print("==============================")

print("1. 記事一覧")
print("2. 記事を追加")
print("3. 記事を検索")
print("4. 記事を編集")
print("5. 記事を削除")
print("6. 記事本文を見る")
print("7. 記事本文を編集")
print()
print("0. 終了")

print("==============================")

print()
choice = input("操作を選択してください：")

if choice == "1":
    print()
    print("----- 記事一覧 -----")

    print("ID | タイトル | カテゴリー | 状態")
    print("-----------------------------------------------")

    for article in articles:
        print(
            f'ID: {article["id"]} | '
            f'タイトル: {article["title"]} | '
            f'カテゴリー: {article["category"]} | '
            f'状態: {article["status"]}'
        )

elif choice == "2":
    print()
    print("----- 記事を追加 -----")

    new_id = max(article["id"] for article in articles) + 1

    title = input("記事タイトルを入力してください：")
    category = input("カテゴリーを入力してください：")

    new_article = {
    "id": new_id,
    "title": title,
    "category": category,
    "status": "draft",
    "url": "",
    "content_file": f"articles/article_{new_id:03}.md"
}

    articles.append(new_article)

    with open("articles.json", "w", encoding="utf-8") as file:
        json.dump(articles, file, ensure_ascii=False, indent=2)

    filename = f"articles/article_{new_id:03}.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"# {title}\n\n")
        file.write(f"カテゴリー：{category}\n\n")
        file.write("## 概要\n\n")
        file.write("ここに記事の概要を入力します。\n\n")
        file.write("## 本文\n\n")
        file.write("ここに記事本文を入力します。\n\n")
        file.write("## まとめ\n\n")
        file.write("ここに記事のまとめを入力します。\n")

    print("記事を登録しました。")
    print(f"記事本文ファイルを作成しました：{filename}")

elif choice == "3":
    print()
    print("----- 記事を検索 -----")

    keyword = input("検索キーワードを入力してください：")

    print()
    print("----- 検索結果 -----")

    found = False

    for article in articles:
        if (
            keyword.lower() in article["title"].lower()
            or keyword.lower() in article["category"].lower()
        ):
            print(
                f'ID: {article["id"]} | '
                f'タイトル: {article["title"]} | '
                f'カテゴリー: {article["category"]} | '
                f'状態: {article["status"]}'
            )
            found = True

    if not found:
        print("該当する記事はありません。")

elif choice == "4":
    print()
    print("----- 記事を編集 -----")

    edit_id = int(input("編集する記事IDを入力してください："))

    found = False

    for article in articles:
        if article["id"] == edit_id:
            print("記事が見つかりました。")
            print(f'タイトル：{article["title"]}')
            print(f'カテゴリー：{article["category"]}')
            print(f'現在の状態：{article["status"]}')

            new_status = input("新しい状態を入力してください（draft / published）：")

            if new_status == "draft" or new_status == "published":
                article["status"] = new_status
            else:
                print("無効な状態です。draft または published を入力してください。")
                found = False
                break

            found = True
            break

    if found:
        with open("articles.json", "w", encoding="utf-8") as file:
            json.dump(articles, file, ensure_ascii=False, indent=2)

        print("記事を更新しました。")

    else:
        print("指定した記事は見つかりません。")

elif choice == "5":
        print()
        print("----- 記事を削除 -----")

        delete_id = int(input("削除する記事IDを入力してください："))

        target_article = None

        for article in articles:
            if article["id"] == delete_id:
                target_article = article
                break

        if target_article:
            print()
            print(f"記事タイトル：{target_article['title']}")

            confirm = input("この記事を削除しますか？ (y/n)：")

            if confirm.lower() == "y":
                content_file = target_article.get("content_file")

                articles.remove(target_article)

                with open("articles.json", "w", encoding="utf-8") as file:
                    json.dump(articles, file, ensure_ascii=False, indent=2)

                if content_file:
                    try:
                        os.remove(content_file)
                        print("本文ファイルも削除しました。")
                    except FileNotFoundError:
                        print("本文ファイルは見つかりませんでした。")

                print("記事を削除しました。")

            else:
                print("削除をキャンセルしました。")

        else:
            print("指定した記事が見つかりません。")

elif choice == "6":
    print()
    print("----- 記事本文を見る -----")

    view_id = int(input("記事IDを入力してください："))

    filename = None

    for article in articles:
        if article["id"] == view_id:
            filename = article.get("content_file")
            break

    if filename:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            print()
            print("----- 記事本文 -----")
            print(content)

        except FileNotFoundError:
            print("指定した記事本文が見つかりません。")

    else:
        print("指定した記事の本文ファイル情報がありません。")

elif choice == "7":
    print()
    print("----- 記事本文を編集 -----")

    edit_id = int(input("編集する記事IDを入力してください："))

    target_article = None

    for article in articles:
        if article["id"] == edit_id:
            target_article = article
            break

    if target_article:
        content_file = target_article.get("content_file")

        if content_file:
            try:
                with open(content_file, "r", encoding="utf-8") as file:
                    content = file.read()

                print()
                print("現在の本文：")
                print("--------------------")
                print(content)
                print("--------------------")

                print()
                print("新しい本文を入力してください。")
                print("入力を終了するには、空行を2回入力してください。")

                lines = []

                while True:
                    line = input()

                    if line == "":
                        if lines and lines[-1] == "":
                            break

                    lines.append(line)

                new_content = "\n".join(lines[:-1])

                if not new_content.strip():
                    print("本文が空のため、更新を中止しました。")
                else:
                    with open(content_file, "w", encoding="utf-8") as file:
                        file.write(new_content)

                    print("記事本文を更新しました。")

            except FileNotFoundError:
                print("本文ファイルが見つかりません。")

        else:
            print("本文ファイルが設定されていません。")

    else:
        print("指定した記事が見つかりません。")
        
elif choice == "0":
    print("終了します。")

else:
    print("正しい番号を入力してください。")