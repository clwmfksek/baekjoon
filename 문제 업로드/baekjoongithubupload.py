from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pyautogui as pg
import os
import time

urllist = []
tierlist = []
namelist = []
linklist = []
numlist = []

# URL 입력 받기
txtpath = r"C:\Users\pork8\Documents\dds\test.txt"
with open(txtpath, 'r', encoding='utf-8') as fi:
    txtlines = fi.readlines()

# Chrome 드라이버 설정
chrome_driver_path = r'C:\Users\pork8\Documents\dds\files\chromedriver\chromedriver-win64\chromedriver.exe'
chrome_options = Options()
#chrome_options.add_argument('--headless')  # 브라우저를 화면에 표시하지 않고 실행
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    for ind, detail in enumerate(txtlines):
        url = detail.split()[0]
        tier = detail.split()[1] + " " + detail.split()[2]
        try:
            # 페이지 열기
            driver.get(url)
            
            # 명시적 대기를 통해 요소가 나타날 때까지 기다리기 (최대 10초)
            wait = WebDriverWait(driver, 10)

            # 문제 이름 가져오기
            problem_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="problem_title"]')))
            namelist.append(problem_name_element.text.strip())

            # 문제 링크 및 번호 가져오기
            problem_link = driver.current_url
            linklist.append(problem_link)
            numlist.append(int(problem_link.split('/')[-1]))  # URL에서 문제 번호 추출

            urllist.append(url)
            tierlist.append(tier)
        except Exception as e:
            print(f"Error processing {url}: {e}")
finally:
    driver.quit()
    time.sleep(3)

# 파일 수정 부분
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
        leftnumber = 1000  # 파일별로 초기화
        for tier, problem_number, problem_link, problem_name in zip(tierlist, numlist, linklist, namelist):
            inserted = False
            for idx, line in enumerate(lines):
                if line.startswith('| ['):
                    number = int(line.split("]")[0].split("[")[1])
                    if problem_number == number:
                        lines[idx] = f"| [{problem_number}]({problem_link}) | {problem_name} | {tier} |\n"
                        inserted = True
                        break
                    if problem_number > leftnumber and problem_number < number:
                        lines.insert(idx, f"| [{problem_number}]({problem_link}) | {problem_name} | {tier} |\n")
                        inserted = True
                        break
                    leftnumber = number
            if not inserted:
                lines.append(f"| [{problem_number}]({problem_link}) | {problem_name} | {tier} |\n")

        # 파일 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
