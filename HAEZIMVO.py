import pandas as pandas
import time

# 변환 시작 시간 측정
start_time = time.time()

# 엑셀 파일 불러오기
data = pandas.read_excel("HAEZIMVO.xlsx", sheet_name = "운임", header = 1, engine = "openpyxl")

# JSON으로 저장
data.to_json("HAEZIMVO.json", orient = "records", force_ascii = False, indent = 2)

# 변환 소요 시간 측정
end_time = time.time()
elapsed_time = end_time - start_time

print(f"변환 완료! 소요 시간: {elapsed_time:.2f}초")
