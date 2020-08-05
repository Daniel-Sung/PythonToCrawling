from selenium import webdriver
from bs4 import BeautifulSoup

base_url ="https://www.athome.co.jp"
url = f"{base_url}/ag/"

#웹 페이지내 버튼을 눌러줘야 해서 크롬 웹드라이버를 다운로드 받고 임포트
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)

#페이지 더보기 버튼의 xpath를 취득


btn = driver.find_element_by_xpath("""//*[@id="btn-readmore"]/a""")
btn.click()
# ? btn 눌러주고 왜 print(len(courses)) 로 데이터 취득이 안되는지...

#드라이버에서 읽어 들인 페이지를 뷰티풀스프를 이용하여 html 파싱
bs = BeautifulSoup(driver.page_source, features="html.parser")

#코스 정보 취득
courses = bs.select("div.archive_list-box")
print(len(courses))

courseList = []

#for 문으로 웹페이지내 코스 정보 획득
# for c in courses:
#     link = c.attrs["href"]
#     title = c.select_one("h4").getText().strip()
#     desc = c.select_one("p").getText().strip()
#     #print(link , title, desc)
#     courseList.append({"link":link, "title":title, "desc":desc})

# for c in courseList:
#     driver.get(f"{base_url}{c['link']}")
#     bs_detail = BeautifulSoup(driver.page_source, features="html.parser")
    
#     chapters = bs_detail.select_one("ol.chapters")
#     chapters_elem = chapters.select("li.chapter")

#     chapter_list = []
#     for chap in chapters_elem:
#         chap_title = chap.select_one("h4.chapter__title").getText().strip()
#         chap_description = chap.select_one("p.chapter__description").getText().strip()
#         chap_detail_elem = chap.select("H5.chapter__exercise-title")

#         chap_detail_titles = []
#         for cd in chap_detail_elem:
#             cd_title = cd.getText().strip()
#             chap_detail_titles.append(cd_title)

#         chapter_detail = {"title":chap_title, "desc":chap_description, "details":chap_detail_titles}
#         #print(chapter_detail)
#         chapter_list.append(chapter_detail)
#     c["chapter_detail"] = chapter_list
    
# print(courseList)
# print(len(courseList))

