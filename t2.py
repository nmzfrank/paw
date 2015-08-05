# -*- coding: utf-8 -*-
import httplib
import urllib
from StringIO import StringIO
import gzip
import re


class login(object):
	"""docstring for login"""
	def __init__(self):
		return 
		


	def prefetch(self):
		addressPattern = re.compile('action="(?P<address>.+?)"')
		vkPattern = re.compile('name="vk" value="(?P<vk>.+?)"')
		pwPattern = re.compile('type="password" name="(?P<pwname>.+?)"')
		self.headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Connection':'keep-alive',	
			'Content-Type':'application/x-www-form-urlencoded',
		}
		self.conn = httplib.HTTPSConnection("login.weibo.cn")
		self.conn.request("GET","https://login.weibo.cn/login/")
		self.response = self.conn.getresponse()
		self.cookie = self.response.getheader("Set-Cookie")
		self.cookie = self.cookie.split(';',1)[0]
		data = self.response.read()
		address = addressPattern.search(data).group('address')
		address = re.sub('&amp;','&',address)
		address = re.sub("vt=1","vt=4",address)
		self.pwname = pwPattern.search(data).group('pwname')
		self.vk = vkPattern.search(data).group('vk')
		self.redirect = "https://login.weibo.cn/login/" + address

	def fetch(self):
		self.prefetch()
		addressPattern = re.compile('action="(?P<address>.+?)"')
		vkPattern = re.compile('name="vk" value="(?P<vk>.+?)"')
		pwPattern = re.compile('type="password" name="(?P<pwname>.+?)"')
		data = {	
				'mobile':'nmz110@126.com',
				self.pwname:'happyending',
				'remember':'on',
				'backURL':'http%253A%252F%252Fweibo.cn',
				'backTitle':'%E6%89%8B%E6%9C%BA%E6%96%B0%E6%B5%AA%E7%BD%91',
				'tryCount':'',
				'vk':str(self.vk),
				'submit':'%E7%99%BB%E5%BD%95'
		}
		header = {	'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate',
				'Accept-Language':'zh-CN,zh;q=0.8',
				'Connection':'keep-alive',	
				'Cache-Control':'max-age=0',
				'Content-Type':'application/x-www-form-urlencoded',				
				'Host':'login.weibo.cn',
				'Origin':'https://login.weibo.cn',
				'Referer':'https://login.weibo.cn/login/?',
				'Cookie': str(self.cookie),
				'Upgrade-Insecure-Requests':1
			}
		data = urllib.urlencode(data)
		self.conn.request("POST",self.redirect,data, header)
		response = self.conn.getresponse()
		print response.status
		cookiePattern = re.compile(r"(?P<cookie>.+?); expires.+?; path.+?; domain.+?; httponly,?")
		cookieList = []
		cookieinfo = response.getheader('set-cookie')
		cookieMatches = cookiePattern.finditer(cookieinfo)
		for match in cookieMatches:
			cookieList.append(match.group('cookie'))
		self.sub = cookieList[0]
		self.gsid = cookieList[1]

		return

	def login(self):
		self.fetch()
		self.cookie = self.cookie + '; '+self.sub + '; ' + self.gsid
		header = {	'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate',
				'Accept-Language':'zh-CN,zh;q=0.8',
				'Connection':'keep-alive',	
				'Cache-Control':'max-age=0',
				'Content-Type':'application/x-www-form-urlencoded',				
				'Host':'weibo.cn',
				'Cookie': str(self.cookie),
				'Upgrade-Insecure-Requests':1
			}
		self.conn=httplib.HTTPSConnection("weibo.cn")
		self.conn.request("GET","http://weibo.cn/2796653044/profile?page=1&vt=4",'', header)
		response = self.conn.getresponse()

		data = response.read()
		buff = gzip.GzipFile(fileobj=StringIO(data))
		data = buff.read()
		print data


l = login()
l.login()

