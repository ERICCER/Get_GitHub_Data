#coding = UTF-8
#Make of python3
#Web API
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=start'
#将这个网址储存在变量url中
r = requests.get(url)
#向这个url发出get请求 
print("状态码:",r.status_code)

response_dict = r.json()

repo_dict = response_dict['items']

names, stars = [], []
for repo_dict in repo_dict:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


