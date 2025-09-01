import pandas as pandas

# 엑셀 파일 불러오기
data = pandas.read_excel("HAEZIMVO.xlsx", sheet_name = "운임", header = 1, engine = "openpyxl")

# JSON으로 저장
data.to_json("HAEZIMVO.json", orient = "records", force_ascii = False, indent = 2)

print("변환 완료!")