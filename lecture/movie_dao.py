# 리뷰 데이터 저장
from db.common.connection import connection


def add_review(data):
    pass
    # 1) Connection
    conn = connection()

    try:
        # 2) 일꾼 생성
        curs = conn.cursor()
        # 3) JOB 생성(SQL) -> INSERT, DELETE, UPDATE, SELECT
        sql = """
                INSERT INTO tbl_review(title, review, score, writer, reg_date)
                VALUES(%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s);
              """
        # 4) 작업 시작
        curs.execute(sql, data)
    except Exception as e:
        print(e)