from lxml import html
import requests

url_base = "https://apps-dso.sws.iastate.edu/si/course.php?id="
id_number = 1269
full_url = url_base + str(id_number)

xpath = """//*[@id="content"]/div[2]/text()[1]"""

page = requests.get(full_url)
tree = html.fromstring(page.content)

time = tree.xpath(xpath)

content = page.content

# start_index = content.index("Weekly SI Sessions")
# end_index = content.index("About SI for this Course")

# sessions = page.content[start_index, end_index]

# print(sessions)

my_file = open('SI.txt', 'w+')
