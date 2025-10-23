import requests
from bs4 import BeautifulSoup

# 1단계: 웹페이지 가져오기 (HTTP GET 요청)
# 크롤링할 대상 사이트의 URL입니다.
URL = "http://quotes.toscrape.com" 



def crawl(url):
    print(f"'{url}' 사이트 크롤링을 시작합니다...")

    try:
        response = requests.get(url)
        # HTTP 에러(4xx, 5xx)가 발생하면 예외를 일으킵니다.
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')

        quote_elements = soup.select('span.text')

        author_elements = soup.select('small.author')

        # 4단계: 결과 출력

        for index, (quote_element, author_element) in enumerate(zip(quote_elements, author_elements)):
            quote = quote_element.text
            author = author_element.text
            if quote and author:
                print("\n--- 크롤링 성공! ---")
                print(f"명언: {quote} 작성자 : {author}")
            else:
                print("\n[오류] 명언 또는 작성자를 찾을 수 없습니다. (사이트 구조 변경 가능성)")
                return False
        return True

    except requests.exceptions.RequestException as e:
        print(f"\n[오류] 사이트 접속에 실패했습니다: {e}")
        return False

