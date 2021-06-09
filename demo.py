# @Time : 2021/6/6 8:51 下午
# @Author : Bais
# @Email : 17343001493@163.com
# @File : demo.py
import yaml
f = open("./data/login_data.yaml",encoding="utf8")
data=yaml.load(f,Loader=yaml.FullLoader)
print(data)
phone = data['login'][0]['pass']['case1']['phone']
print(data['login'][0]['pass']['case1']['pwd'])
pwd = data['login'][0]['pass']['case2']['phone']
print(pwd)
print(phone)
f.close()