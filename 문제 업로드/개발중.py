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

# URL 입력 받기
url = pg.prompt("Link in bio")
id = 'clwm0217'
pw = 'clwmclwm1@3'
# Chrome 드라이버 설정
chrome_driver_path = r'C:\Users\pork8\Documents\dds\files\chromedriver\chromedriver-win64\chromedriver.exe'
chrome_options = Options()
#chrome_options.add_argument('--headless')  # 브라우저를 화면에 표시하지 않고 실행
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

txtpath = r"C:\Users\pork8\Desktop\test.txt"
with open(txtpath, 'r', encoding='utf-8') as fi:
    txtlines = fi.readlines()

namelist = []
tierlist = []
numberlist = []
linklist = []

try:
    # 페이지 열기
    driver.get("https://www.acmicpc.net/")
    
    # 명시적 대기를 통해 요소가 나타날 때까지 기다리기 (최대 10초)
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div/ul/li[3]/a").click()
    driver.find_element(By.XPATH,'//*[@id="login_form"]/div[2]/input').send_keys(id)
    driver.find_element(By.XPATH,'//*[@id="login_form"]/div[3]/input').send_keys(pw)
    driver.find_element(By.XPATH,'//*[@id="submit_button"]').click()
    time.sleep(10)

    for idx, detail in enumerate(txtlines):
        driver.get(f"{detail}")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)

        # 문제 이름 가져오기
        problem_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="problem_title"]')))
        namelist.append(problem_name_element.text.strip())

        tierlist.append(driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[3]/div/blockquote/span").text())

        # 문제 링크 및 번호 가져오기
        linked = driver.current_url
        linklist.append(linked)
        numberlist.append(int(linked.split('/')[-1]))  # URL에서 문제 번호 추출

        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

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
        i = 0
        # 문제 정보 업데이트
        for idx, line in enumerate(lines):
            i += 1
            if line.startswith('| ['):
                number = int(line.split("]")[0].split("[")[1])
                if numberlist[i] == number:
                    lines[idx] = f"| [{numberlist[i]}]({linklist[i]}) | {namelist[i]} | {tierlist[i]} |\n"
                    break
                if numberlist[i] > leftnumber and numberlist[i] < number:
                    lines.append("")
                    for i in range(len(lines) - 1, idx, -1):
                        lines[i] = lines[i - 1]
                    lines[idx] = f"| [{numberlist[i]}]({linklist[i]}) | {namelist[i]} | {tierlist[i]} |\n"
                    break
                if len(lines)-1 == idx :
                    lines.append(f"| [{numberlist[i]}]({linklist[i]}) | {namelist[i]} | {tierlist[i]} |\n")
                leftnumber = number

        # 파일 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
