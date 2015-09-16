# -*- coding: utf-8 -*-
import sys 
import re
import urllib3
from urllib3 import Retry
import BeautifulSoup

def prefetch():
	http = urllib3.PoolManager()
	r = http.request('POST', 'http://login.weibo.cn/login/?')
	content = r.data
	soup = BeautifulSoup.BeautifulSoup(content)
	formParamPattern = re.compile('action="(?P<address>.+?)"')
	vkParamPattern = re.compile('name="vk" value="(?P<vk>.+?)"')
	form = soup.body.renderContents()
	address = formParamPattern.search(form)
	vk = vkParamPattern.search(form)
	return address.group('address'), vk.group('vk')


def fetch():
	address, vk = prefetch()
	t_address = 'http://weibo.cn/login/' + address
	print t_address,vk
	http = urllib3.PoolManager()
	header = {	'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate',
				'Accept-Language':'zh-CN,zh;q=0.8',
				'Cache-Control':'max-age=0',
				'Connection':'keep-alive',
				'Content-Type':'application/x-www-form-urlencoded',
				'Host':'login.weibo.cn',
				'Origin':'https://login.weibo.cn',
				'Referer':'https://login.weibo.cn/login/?',
				'Upgrade-Insecure-Requests':'1',
			}
	param = {	
				'mobile':'nmz110@126.com',
				'password_5647':'happyending',
				'remember':'on',
				'backURL':'http%3A%2F%2Fweibo.cn%2F',
				'backTitle':u'微博',
				'tryCount':'',
				'vk':vk,
				'submit':u'登录',
		}
	r = http.request('POST', t_address, param, header, retries = False)
	content = r.data
	print r.get_redirect_location()
	r = http.request('POST', t_address, param, header, retries = False)
	print r.getheader('location')
	return content


print fetch()
