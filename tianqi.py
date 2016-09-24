#coding=utf-8
import requests

def weathe_detail(time,title,a=False):
    if a is not False:
        dic = result[time][a]
        keys = result[time][a].keys()
        print u'天气预报:'
    else:
        dic = result[time]
        keys = result[time].keys()
        print u'昨日天气:'
    list = title
    b=0    
    for i in keys:
        print "         ",list[b],":",dic[i];
        b+=1
    print "\n"

cityname = raw_input('你想查看那个城市的天气?\n')
cityname = cityname.decode('gbk').encode('utf-8') 
url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityname
try:
	r = requests.get(url)
	data = r.json()
	result = data['data']
	forecast_title = [u'风向',u'最高温度',u'风力',u'日期',u'类型',u'最低温度']
	yesterday_title = [u'风向',u'类型',u'最高温度',u'最低温度',u'日期',u'风力']

	try:
		print u'城市:',result['city'];
		weathe_detail(a=0,time='forecast',title=forecast_title);
		weathe_detail(time='yesterday',title=yesterday_title);
		print u'感冒指数:',result['ganmao'];
		print u'温度:',result['wendu'];
		print u'aqi:',result['aqi'];
		b = int(raw_input(u"输入要查询的未来天数(1-5):"))
		if b <= 4 and b >= 0:
		    weathe_detail(a=b-1,time='forecast',title=forecast_title);

		else:
		    exit()
	except:
		print u'查询失败！'
except:
	print u"连接超时或者输入城市有误！"
