import requests
from bs4 import BeautifulSoup
locate = input("현재 위치를 입력해 주세요: ")
area = locate
html = requests.get(f"https://search.naver.com/search.naver?&query={area}+날씨")
soup = BeautifulSoup(html.text, 'html.parser')
text = soup.find('h2',{'class': 'title'}).text #검색된 날씨 지역명
wichi = text
today_temper = soup.find('div',{'class':'temperature_text'}).text
today_temper = today_temper[6:10]
temper = (today_temper)
yes_weather = soup.find('p',{'class':'summary'}).text
yes_weather = yes_weather[4:13].strip()
yesterday = (yes_weather)
today_weather = soup.find('span',{'class':'weather before_slash'}).text
today = (today_weather)
sense_temper= soup.select('dl.summary_list>div dd')
sense_temper_text = sense_temper[0].text #체감온도
sense = (sense_temper_text)
water = soup.select('dl.summary_list>div dd')
water_text = water[1].text #습도
wind1 = soup.select('dl.summary_list>div dt')
wind1_text = wind1[2].text #풍향
wind11 = (wind1_text)
wind2 = soup.select('dl.summary_list>div dd')
wind2_text = wind2[2].text #풍속
wind22 = (wind2_text)
water1 = (water_text)
dust_info = soup.select('ul.today_chart_list>li')
dust1_info = dust_info[0].find('span',{'class':'txt'}).text #미세먼지 정보
dust2_info = dust_info[1].find('span',{'class':'txt'}).text #초미세먼지 정보
dust1 = (dust1_info)
dust2 = (dust2_info)
sun_info = soup.select('ul.today_chart_list>li')
sun1_info = sun_info[2].find('span',{'class':'txt'}).text #자외선
sun = (sun1_info)
sunup_info = soup.select('ul.today_chart_list>li')
sunup1_info = sunup_info[3].find('span',{'class':'txt'}).text #일출,일몰
sunup = (sunup1_info)
if wind11 == '북풍':
    wind111 = ("바람(북풍⬆️)")
elif wind11 == '북동풍':
    wind111 = ("바람(북동풍↗️)")
elif wind11 == '동풍':
    wind111 = ("바람(동풍➡️)")
elif wind11 == '남동풍':
    wind111 = ("바람(남동풍↘️)")
elif wind11 == '남풍':
    wind111 = ("바람(남풍⬇️)")
elif wind11 == '남서풍':
    wind111 = ("바람(남서풍↙️)")
elif wind11 == '서풍':
    wind111 = ("바람(서풍⬅️)")
elif wind11 == '북서풍':
    wind111 = ("바람(북서풍↖️)")
if sunup < '12: 00':
    sunup1 = '일출시간'
else:
    sunup1 = '일몰시간'
print(f"{area}의 날씨")
print(f"🌡현재온도:{temper}")
print(f"📊어제와 비교:{yesterday}")
print(f"🗓️오늘날씨:{today}")
print(f"🙍‍♂️체감온도:{sense}")
print(f"💧습도:{water1}")
print(f"💨{wind111}:{wind22}")
print(f"😷미세먼지:{dust1}")
print(f"😷초미세먼지:{dust2}")
print(f"☀️자외선:{sun}")
print(f"🌄{sunup1}:{sunup}")