import webbrowser
import random
import time
import sys
from tqdm import tqdm

# デフォルトのサービス名リスト
services = ['SCS-C02', 'SAA-C03', 'SOA-C02', 'SAP-C02', 'ANS-C01', 'その他（手動入力）']

# サービスの選択
print("以下のテストサービスから選択してください：")
for idx, service in enumerate(services):
    print(f"{idx + 1}. {service}")

service_choice = int(input("番号を入力してください: "))

if service_choice == len(services):
    service_name = input("サービス名を入力してください: ")
else:
    service_name = services[service_choice - 1]

# 質問の取得方法を選択
print("\n質問をどのように取得しますか？")
print("1. ランダムな質問を取得")
print("2. 質問範囲を指定して取得")

method_choice = int(input("番号を入力してください: "))

questions = []

if method_choice == 1:
    total_questions = int(input("取得したい質問の総数を入力してください: "))
    max_question_number = int(input("質問番号の最大値を入力してください（例：200）: "))
    questions = random.sample(range(1, max_question_number + 1), total_questions)
else:
    start_question = int(input("開始する質問番号を入力してください: "))
    end_question = int(input("終了する質問番号を入力してください: "))
    questions = list(range(start_question, end_question + 1))

# 最初のページをテストで開く
test_question = questions[0]
search_query = f"examtopics {service_name} question {test_question}"
print(f"\nテストとして以下の検索結果を開きます：\n{search_query}")

# Google検索URLを生成
search_url = f"https://www.google.com/search?q={search_query}"

# デフォルトのブラウザで開く
webbrowser.open(search_url)

# ユーザーに確認
is_correct = input("正しく開けていますか？ (y/n): ")

if is_correct.lower() != 'y':
    print("プログラムを終了します。")
    sys.exit()

# 質問リストを開く
print("\n質問を開いています...")

for question in tqdm(questions):
    search_query = f"examtopics {service_name} question {question}"
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)
    time.sleep(0.1)  # 負荷を避けるために少し待機

print("\nThanks. Do your best.")

