from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pyautogui as pg
import os

# URL 입력 받기
url,tier,tier2 = pg.prompt("Link in bio").split()
tier = tier + " " + tier2
# Chrome 드라이버 설정
chrome_driver_path = r'C:\Users\pork8\Documents\dds\files\chromedriver\chromedriver-win64\chromedriver.exe'
chrome_options = Options()
#aschrome_options.add_argument('--headless')  # 브라우저를 화면에 표시하지 않고 실행
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 페이지 열기
    driver.get(url)
    
    # 명시적 대기를 통해 요소가 나타날 때까지 기다리기 (최대 10초)
    wait = WebDriverWait(driver, 10)

    # 문제 이름 가져오기
    problem_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="problem_title"]')))
    problem_name = problem_name_element.text.strip()
    print(f'문제 이름: {problem_name}')

    # 문제 링크 및 번호 가져오기
    problem_link = driver.current_url
    problem_number = int(problem_link.split('/')[-1])  # URL에서 문제 번호 추출
    print(f'문제 링크: {problem_link}')
    print(f'문제 번호: {problem_number}')

finally:
    driver.quit()

# 파일 수정 부분
leftnumber = 1000
path = r'C:\Users\pork8\Documents\GitHub\baekjoon'

for filename in os.listdir(path):
    if filename.endswith('.md'):
        file_path = os.path.join(path, filename)
        
        # 파일 열기
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 수정할 날짜 업데이트
        now = datetime.now()
        new_date = now.strftime('%Y-%m-%d %H:%M:%S')
        lines[6] = f"마지막 수정 일자 : {new_date}\n"

        # 문제 정보 업데이트
        for idx, line in enumerate(lines):
            if line.startswith('| ['):
                number = int(line.split("]")[0].split("[")[1])
                if problem_number == number:
                    lines[idx] = f"| [{problem_number}]({problem_link}) | {problem_name} | {tier} |\n"
                    break
                if problem_number > leftnumber and problem_number < number:
                    lines.append("")
                    for i in range(len(lines) - 1, idx, -1):
                        lines[i] = lines[i - 1]
                    lines[idx] = f"| [{problem_number}]({problem_link}) | {problem_name} | {tier} |\n"
                    break
                if len(lines)-1 == idx :
                    lines.append(f"| [{problem_number}]({problem_link}) | {problem_name} | {tier} |\n")
                leftnumber = number

        # 파일 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
