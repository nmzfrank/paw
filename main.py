import sinaLogin
import urllib2
from StringIO import StringIO
from multiprocessing.dummy import Pool as ThreadPool

conn=httplib.HTTPSConnection("weibo.cn")
user = "nmz110@126.com"
password = "BFFF96FFA6"

def getPages(url):
	l = sinaLogin.login(user,password)
	header = l.getHeader()
	conn.request("GET",url,'', header)
	
	response = self.conn.getresponse()

	data = response.read()
	buff = gzip.GzipFile(fileobj=StringIO(data))
	data = buff.read()
	print data


pool = ThreadPool(4)
results = 