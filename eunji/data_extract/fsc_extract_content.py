import re
import pandas as pd

def extract_main_content(text):
    # 주요 내용 추출 정규식 패턴 (3번 항목 유무에 따른 처리)
    pattern_with_opinion = r"2\.\s*주요\s*내용\s*(.*?)\s*3\.\s*의견제출"
    pattern_to_end = r"2\.\s*주요\s*내용\s*(.*?)\s*3\."  # 문서 끝까지 추출하는 패턴

    # 3번 항목이 있는 경우
    match = re.search(pattern_with_opinion, text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # 3번 항목이 없을 경우
    match = re.search(pattern_to_end, text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # 주요 내용이 없을 경우
    return "주요 내용을 찾을 수 없습니다."

def extract_reason(text):
    # '개정이유' 또는 '개정이유 및 주요내용'을 처리하는 정규식 패턴
    pattern = r"1\.\s*(제정이유|개정이유(?: 및 주요내용)?)\s*(.*?)\s*2\."


    # 정규식 매칭
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(2).strip()  # 주요 내용만 추출
    else:
        return "개정이유를 찾을 수 없습니다."



# 데이터 불러오기
df = pd.read_csv("./fsc_announcements.csv")

# '내용' 열에 결측치가 있는지 확인 후 처리
df['내용'] = df['내용'].fillna('')  # 결측치를 빈 문자열로 대체

# 테스트용 텍스트
text = df['내용'][49]

# 주요 내용 추출 및 출력
main_content = extract_main_content(text)
print(main_content)
print("-----------------------------------")
# 개정이유 추출 및 출력
print(extract_reason(text))

print(df.head())


# # '내용' 열에서 주요 내용 추출 후 '주요내용' 열에 저장
df['개정이유'] = df['내용'].apply(extract_reason)

# # '내용' 열에서 주요 내용 추출 후 '주요내용' 열에 저장
df['주요내용'] = df['내용'].apply(extract_main_content)

# # CSV 파일로 저장 (옵션)
df.to_csv('fsc_announcements_extract.csv', index=False, encoding='utf-8')