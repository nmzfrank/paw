import sys 
import re
import urllib3
import BeautifulSoup

def prefetch():
	http = urllib3.PoolManager()
	r = http.request('POST', 'http://login.weibo.cn/login/?')
	content = r.data
	soup = BeautifulSoup.BeautifulSoup(content)
	formParamPattern = re.compile('action="(?P<address>.+?)"')
	form = soup.body.renderContents()
	match = formParamPattern.search(form)
	return match.group('address')


def fetch():
	address = prefetch()
	t_address = 'http"//weibo.cn/login/' + address
	http = urllib3.PoolManager()
	header = {}
	param = {}
	r = http.request('POST', t_address, param, header)
	content = r.data
	return


fetch()
