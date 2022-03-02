from django.shortcuts import render

from django.http import JsonResponse
import json

def home(request):
    # POST 요청일 때
    if request.method == 'POST':
        data = json.loads(request.body)
        # do something
        print(data)

        context = {
            'result': data,
        }
        return JsonResponse(context)

# Create your views here.
"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def my_scrap():


    url_1 = "https://www.mohw.go.kr/react/ncov/selclinic04ls.jsp?tabno=4&page="

    # 불러온 페이지마다 다 크롤링해야하니까 이렇게 넣어야지~!

    res = []
    cur_page = 1
    for i in range(1, 65):
        #    print(i, end ="/")
        try:
            url_full = url_1 + str(i)
            # print(url_full)

            driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
            driver.get(url=url_full)

            표_10줄 = driver.find_element(By.CLASS_NAME, 'tb_center')
            trs = 표_10줄.find_elements_by_tag_name('tr')

            for i in range(len(trs)):
                선별td = trs[i].find_elements_by_tag_name('td')[2]
                선별진료소 = 선별td.find_elements_by_tag_name('strong')[0].text.strip("*")
                혼잡도 = trs[i].find_elements_by_tag_name('td')[8].text
                res.append([선별진료소] + [혼잡도])

            driver.close()
        except:
            print(end="")

    return res
"""

# mariadb
import pymysql as m
con = m.connect(host="localhost", user="root", password='1234',
               db="corona_center", charset='utf8')
cur = con.cursor()
cur.execute("select * from center;")
res = cur.fetchall()
con.close()

def coronapage(request):
    return render(
        request,
        'home_page/main_page.html',
    )

def coronapage_en(request):
    return render(
        request,
        'home_page/main_page_en.html',
    )

def coronamap(request):
#    res = my_scrap()
    res = cur.fetchall()
    return render(
        request,
        'main_page/layout.html',
        {
            'res' : res,
        }
    )