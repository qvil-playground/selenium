from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\qvil1\\Downloads\\chromedriver')

# driver를 만든 후 implicitly_wait 값(초단위)을 넣어주세요.
driver.implicitly_wait(3)

driver.get('https://www.kakaobank.com/')

# 하나만 찾기
title = driver.find_element_by_css_selector('div.intro_main > h3')
# 여러개 찾기
small_titles = driver.find_elements_by_css_selector('div.cont_txt > h3')

print(title.text)

for t in small_titles:
    print(t.text)

driver.quit()