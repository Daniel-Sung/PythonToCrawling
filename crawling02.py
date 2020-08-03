from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.datacamp.com/tracks/machine-learning-scientist-with-python"

#웹 페이지내 버튼을 눌러줘야 해서 크롬 웹드라이버를 다운로드 받고 임포트
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)

#페이지 더보기 버튼의 xpath를 취득
btn = driver.find_element_by_xpath("""//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[1]/div/div/div[4]/button""")
btn.click()

#드라이버에서 읽어 들인 페이지를 뷰티풀스프를 이용하여 html 파싱
bs = BeautifulSoup(driver.page_source, features="html.parser")

#코스 정보 취득
courses = bs.select("#gatsby-focus-wrapper > div > div.container.css-93pq91 > div.col-md-8 > div > div > div > div.css-10s95pl > a")
courseList = []

#for 문으로 웹페이지내 코스 정보 획득
for c in courses:
    link = c.attrs["href"]
    title = c.select_one("h4").getText().strip()
    desc = c.select_one("p").getText().strip()
    #print(link , title, desc)
    courseList.append({"link":link, "title":title, "desc":desc})

print(len(courseList))