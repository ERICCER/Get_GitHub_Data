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

my_style = LS('#333366',base_style = LCS)

#config Begin
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.labels_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 45
my_config.show_y_guides = False
my_config.width = 1000
#config Finish

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Github上热门的Python项目'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')


