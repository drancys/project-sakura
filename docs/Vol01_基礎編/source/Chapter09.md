# Project Sakura 第9章
## Pythonによる記事データ管理

### 第9章の目的

これまでProject Sakuraでは、ブログやデジタル資産を作っていくための基礎を積み上げてきました。

第9章では、そこから一歩進んで、

> **「記事に関する情報をPythonで整理・管理できるようにする」**

ことを目指します。

例えば記事について、

- 記事タイトル
- URL
- カテゴリ
- 公開状態
- 作成日
- 更新日
- キーワード
- メモ

などの情報を整理しておけば、記事数が増えても管理しやすくなります。

最終的には、

```text
記事データ
   ↓
Pythonで読み込む
   ↓
検索・追加・変更・一覧表示
   ↓
データとして保存
```

という仕組みを作ります。

---

# 第1節　なぜ記事データを管理するのか

最初は記事が数本しかないため、

「記事タイトルを覚えている」

「ファイルを見れば分かる」

という状態でも問題ありません。

しかし、記事が10本、50本、100本と増えてくると話が変わります。

例えば、

> 「Pythonの記事だけ一覧にしたい」

> 「公開済みの記事だけ確認したい」

> 「まだ書き終わっていない記事は何本ある？」

といったことを毎回手作業で確認するのは大変です。

そこで、記事の情報を一定の形式で保存しておきます。

これが**記事データ管理**です。

---

# 第2節　今回作る仕組み

第9章では、まず大きなシステムを作りません。

最初はシンプルに、

```text
articles.json
```

というファイルに記事情報を保存します。

イメージは次のようなものです。

```text
articles.json
│
├─ 記事1
│   ├─ タイトル
│   ├─ カテゴリ
│   ├─ ステータス
│   └─ URL
│
├─ 記事2
│   ├─ タイトル
│   ├─ カテゴリ
│   ├─ ステータス
│   └─ URL
│
└─ 記事3
    ├─ タイトル
    ├─ カテゴリ
    ├─ ステータス
    └─ URL
```

Pythonからこのデータを読み書きできるようにします。

---

# 第3節　JSONとは何か

ここで新しい言葉が出てきます。

**JSON（ジェイソン）**です。

難しく考える必要はありません。

JSONは、

> **コンピューターが扱いやすい形でデータを保存する方法**

の一つです。

例えば、

```json
{
  "title": "Pythonによる記事データ管理",
  "category": "Python",
  "status": "draft"
}
```

というデータを保存できます。

人間が見ても、ある程度意味が分かります。

Pythonからも簡単に読み込めます。

そのため、第9章ではJSONを利用します。

---

# 第4節　PythonからJSONを扱う

Pythonには、JSONを扱うための機能が標準で用意されています。

そのため、今回の基本部分では新しい有料ソフトやサービスは必要ありません。

Pythonで、

```python
import json
```

と書くことでJSONを扱えるようになります。

これはProject Sakuraの

> **原則無料で進める**

という方針にも合っています。

---

# 第5節　記事データを作る

まず、記事データをPythonで用意します。

```python
articles = [
    {
        "id": 1,
        "title": "Project Sakura 第9章",
        "category": "Python",
        "status": "draft",
        "url": ""
    },
    {
        "id": 2,
        "title": "Project Sakuraについて",
        "category": "Project Sakura",
        "status": "published",
        "url": ""
    }
]
```

ここでは2件の記事を登録しています。

重要なのは、

**記事そのものを保存しているわけではない**

という点です。

保存しているのは、

> **記事を管理するための情報**

です。

---

# 第6節　JSONファイルへ保存する

次にPythonのデータをJSONファイルに保存します。

```python
import json

articles = [
    {
        "id": 1,
        "title": "Project Sakura 第9章",
        "category": "Python",
        "status": "draft",
        "url": ""
    },
    {
        "id": 2,
        "title": "Project Sakuraについて",
        "category": "Project Sakura",
        "status": "published",
        "url": ""
    }
]

with open("articles.json", "w", encoding="utf-8") as file:
    json.dump(articles, file, ensure_ascii=False, indent=2)

print("記事データを保存しました。")
```

このプログラムを実行すると、

```text
articles.json
```

が作成されます。

---

# 第7節　JSONからデータを読み込む

今度は逆です。

保存したJSONファイルをPythonで読み込みます。

```python
import json

with open("articles.json", "r", encoding="utf-8") as file:
    articles = json.load(file)

for article in articles:
    print(article["title"])
```

実行すると、登録されている記事タイトルが表示されます。

```text
Project Sakura 第9章
Project Sakuraについて
```

これで、

**保存 → 読み込み**

という基本的な流れが完成しました。

---

# 第8節　記事を追加する

次は新しい記事を追加します。

```python
import json

with open("articles.json", "r", encoding="utf-8") as file:
    articles = json.load(file)

new_article = {
    "id": 3,
    "title": "AIを使った記事制作",
    "category": "AI",
    "status": "draft",
    "url": ""
}

articles.append(new_article)

with open("articles.json", "w", encoding="utf-8") as file:
    json.dump(articles, file, ensure_ascii=False, indent=2)

print("記事を追加しました。")
```

これで、

```text
articles.json
```

に新しい記事が追加されます。

---

# 第9節　記事を検索する

記事が増えてくると、検索機能が欲しくなります。

例えば「Python」というカテゴリの記事だけ探す場合です。

```python
import json

with open("articles.json", "r", encoding="utf-8") as file:
    articles = json.load(file)

keyword = "Python"

for article in articles:
    if keyword.lower() in article["category"].lower():
        print(article["title"])
```

このような仕組みを発展させれば、

- タイトル検索
- カテゴリ検索
- 公開状態検索
- キーワード検索

などができるようになります。

---

# 第10節　記事データ管理ツールへ発展させる

ここまでできれば、次の段階へ進めます。

最終的には、

```text
========================
 Project Sakura
 記事データ管理
========================

1. 記事一覧
2. 記事追加
3. 記事検索
4. 記事編集
5. 記事削除
6. 公開済み一覧
7. 下書き一覧
0. 終了
```

のような管理画面をPythonで作ることができます。

ここまで来ると、単なるPythonの練習ではありません。

**実際にProject Sakuraで使えるツール**になります。

---

# 第11節　この章で重要な考え方

第9章で覚えてほしいのは、JSONの書き方だけではありません。

重要なのは、

> **「データを整理しておけば、後からコンピューターに仕事をさせられる」**

という考え方です。

例えば記事が100本になったとき、

人間が100本を一つずつ確認するのではなく、

```text
Python
 ↓
articles.json
 ↓
条件検索
 ↓
必要な記事だけ表示
```

とすればいい。

これが**仕組み化**の第一歩です。

---

# 第12節　DranCysとの関係

この章は、DranCysの理念である、

> **Dream. Create. Systemize.**  
> **未来を描く。自ら創る。仕組みに変える。**

ともつながります。

### Dream

記事やデジタル資産を増やしていく。

↓

### Create

Pythonを使って管理する仕組みを自分で作る。

↓

### Systemize

記事が増えても管理できる状態にする。

つまり第9章は、

**「Systemize」へ進むための最初の実践章**

という位置付けになります。

---

# 第13節　将来的な発展

今回作る仕組みは、ここで終わりではありません。

将来的には、

```text
JSON
 ↓
Python
 ↓
記事管理
 ↓
CSV
 ↓
WordPress
 ↓
自動投稿
 ↓
アクセスデータ
 ↓
分析
```

という方向へ発展させることができます。

さらに、

**AI × Python × WordPress**

を組み合わせれば、Project Sakura独自のコンテンツ制作・管理システムへ発展する可能性があります。

ただし、**第9章ではそこまで一気に作りません。**

まずは、

> **「記事データを保存できる」**

> **「読み込める」**

> **「追加できる」**

> **「検索できる」**

という基本部分を確実に完成させます。

---

# 第14節　この章のゴール

第9章を終了した時点で、次の状態を目指します。

- PythonからJSONを扱える
- 記事情報を保存できる
- 保存した記事情報を読み込める
- 記事を追加できる
- 記事を検索できる
- 記事の状態を管理できる
- Project Sakuraで実際に利用できる
- 将来的な自動化につなげられる

そして何より、

> **Pythonを「勉強した」ではなく、Pythonで「自分の仕組みを一つ作った」**

というところまで進みます。

---

# 第9章の位置付け

```text
第1章～第8章
       ↓
Project Sakuraの基礎・設計
       ↓
第9章
Pythonによる記事データ管理
       ↓
「データを管理する」
       ↓
第10章以降
さらなる自動化・効率化
       ↓
Project Sakura独自の仕組み
       ↓
将来的なデジタル資産
```

**第9章はここから「実際に手を動かして作る章」に入ります。**

そして、ここは今までと少し違う進め方にします。

いきなり大量のコードを渡すのではなく、**あなたのPCで実際に `articles.json` を作り、Pythonから保存・読み込みができるところまで、一つずつ確認しながら進めます。**

「完了」と言ってもらったら次へ進む、という今までの方式でいきましょう。
