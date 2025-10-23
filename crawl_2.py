import requests
import time
from crawl_1 import crawl

BASE_URL = "http://quotes.toscrape.com/api/quotes"
i = 1
while True:
    url = f"{BASE_URL}?page={i}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print(f"\n[오류] 사이트 접속에 실패했습니다: {e}")
        break

    data = response.json()
    # url request로 받아서 나머지 데이터 처리하기



    quotes = data["quotes"]
    for quote in quotes:
        quote_text = quote["text"]
        author = quote["author"]["name"]
        print(f"명언: {quote_text} 작성자 : {author}")
    print(f"---------------{i}번째 페이지 크롤링 완료!------------")

    i+=1
    time.sleep(1)
    if not data["has_next"]: break
    # no page, break