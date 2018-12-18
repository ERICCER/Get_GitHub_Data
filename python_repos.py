#coding = UTF-8
#Make of python3
#Web API
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=start'
#将这个网址储存在变量url中
r = requests.get(url)
#向这个url发出get请求 
print("状态码:",r.status_code)

response_dict = r.json()

print("总仓库数:",response_dict['total_count'])
repo_dict = response_dict['items']
print("存储库返回:",len(repo_dict))

#研究第一个仓库

print("关于最受欢迎的仓库信息：")
for repo_dict in repo_dict:
    print("\nName:",repo_dict['name'])
    print("所有者:",repo_dict['owner']['login'])
    print("星标：",repo_dict['stargazers_count'])
    print("URL:",repo_dict['html_url'])
    print("描述:",repo_dict['description'])

