import os
import shutil
import datetime
import locale
import requests
from bs4 import BeautifulSoup
import csv


# url = "https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html"

def func(url, cout):
    response = requests.get(url)
    response.encoding = 'utf-8'

    # print(response.text)

    # tmp_list = url.split("/")
    # file_name = tmp_list[len(tmp_list)-1]
    # print(f"{file_name}を作成")
    # with open(file_name, "w", encoding="UTF-8", newline="") as f:
    #     print(response.text, file=f)
    # shutil.move(file_name, dir_name)

    # BeautifulSoupを用いて取得したHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')
    # HTMLに書かれたaタグ（要素）のテキストとリンク情報を取得
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        if href:
            func(href, cout)
    title = soup.find("title").string
    cout.writerow({"url": url, "title": title})



with open("title.csv", "w", encoding="UTF-8", newline="") as f1:
    cout = csv.DictWriter(f1, ["url", "title"])
    cout.writeheader()
    func("https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html", cout)

# locale.setlocale(locale.LC_ALL, "ja_JP.UTF-8")
# now = datetime.datetime.now()
# dir_name = now.strftime("%Y%m%d")
# if os.path.isdir(dir_name):
#     print("ディレクトリはすでに存在します")
# else:
#     os.mkdir(dir_name)
