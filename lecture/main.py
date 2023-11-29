# SELELIUM
 # pip install selenium
 # pip install webdriver_manager

 # ** Selenium을 사용하는 이유?
 # - Requests는 현재 URL의 정적 페이지 소스코드만 수집 가능
 #  -> "더보기" 버튼 클릭과 같이 동적인 동작 불가!
 # - Selenium은 전용 브라우저를 사용해서 동작
 #  -> 따라서 chrome 드라이버와 같이 브라우저 설정 반드시 필요!

# Selenium 사용방법 2가지
# 1.직접 다운로드
#   URL :
# 2.실시간(코드) 다운로드

import math
import re
import time
from bs4 import BeautifulSoup
from db.movie_dao import add_review
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timedelta

# 1.Selenium
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2.URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=146084"
driver.get(url)
time.sleep(2)

# 3.페이지 전체 코드 가져오기
doc_html = driver.page_source

# 4.Selenium -> BeautifulSoup
doc = BeautifulSoup(doc_html, "html.parser")

# 5.영화 제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()
print(f"영화 제목 : {movie_title}")

# 6.전체 리뷰 출력("평점 더보기" 클릭)
# - 다음 영화 최초 페이지 -> 10개
# - "평점 더보기" 클릭 -> 30개
# ? "평점 더보기" 몇번 클릭? -> 전체 리뷰 출력

# ex) 전체 리뷰 : 187개
# 수식 : 올림((187-10) / 30 = 5.9)

# 6-1.전체 리뷰 수집
total_review_cnt = doc.select("span.txt_netizen")[0].get_text()
print(total_review_cnt)

# 6-2. 전체 리뷰에서 숫자만 추출
# - 문자열 슬라이싱
# 예) (187명)
# print(total_review_cnt[1:-2])
# - 정규식 -> 숫자만 추출
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))

# 6-3."평점 더보기" 클릭 횟수 계산
click_cnt = math.ceil((num_review-10) / 30)

# 7.Selenium을 통해서 "평점 더보기" 클릭
for i in range(click_cnt):
    # "평점 더보기" 클릭
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(1)

# 8.전체 소스코드 가져오기
doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("ul.list_comment > li")

print(len(review_list))

for item in review_list:
    print("=" * 100)
    review_score = item.select("div.ratings")[0].get_text()
    print(f"  - 평점: {review_score}")
    review_content = item.select("p.desc_txt")[0].get_text()
    # \n : 한 줄 개행
    # 수집한 리뷰가 개행 -> 문자열 안에 \n 포함
    review_content = re.sub("\n", "", review_content)
    print(f"  - 리뷰: {review_content}")
    review_writer = item.select("a.link_nick > span")[1].get_text()  # [댓글 작성자, 작성자, 댓글 모아보기]
    print(f"  - 작성자: {review_writer}")

    # 다음영화 리뷰 날짜 표기법 4가지
    #  1. 조금전 : 현재시간(분) - 1분
    #  2. ?분전  : 현재시간(분) - ?
    #  3. ?시간전 : 현재시간(시간) - ?
    #  4. 2023. 11. 29. 14:18 : 그대로


    # 24시간 이내에 작성된 글은 날짜 -> 예: 21시간전, 17시간전
    # 실제 날짜 표기법 -> 2023. 11. 17. 12:15
    # 표기법: 21시간전 -> 2023. 11. 17. 12:15

    review_date = item.select("span.txt_date")[0].get_text()

    # review_date -> 4가지 표기법 중 1개
    if review_date == "조금전":
        review_date = datetime.now() - timedelta(minutes=1)  # 현재시간 - 1분
        review_date = review_date.strftime("%Y. %m. %d. %H:%M")
    elif review_date[-2:] == "분전":
        reg_minute = int(re.sub(r"[^~0-9]", "", review_date))
        review_date = datetime.now() - timedelta(minutes=reg_minute)  # 현재시간 - 1분
        review_date = review_date.strftime("%Y. %m. %d. %H:%M")
        # 1분전 ~ 59분전 -> "분전"
    elif review_date[-3:] == "시간전":
        # 1시간전 ~ 23시간전 -> "시간전"
        reg_hour = int(re.sub(r"[^~0-9]", "", review_date))
        review_date = datetime.now() - timedelta(minutes=reg_hour)  # 현재시간 - 1분
        review_date = review_date.strftime("%Y. %m. %d. %H:%M")
    print(f"  - 날짜: {review_date }")

    # MariaDB에 저장
    #  1)
    data = {
        "title": movie_title,
        "review": review_content,
        "score": review_score,
        "writer": review_writer,
        "reg_date": review_date
    }
    add_review(data)