from lxml import html
import requests

url_base = "https://www.firstinspires.org/team-event-search/team?program=FTC&year=2018&number="
team_number = 5975
full_url = url_base+str(team_number)

xpath = """//*[@id="+"teamDetail"+"]/div/div/div[1]/h2"""

page = requests.get(full_url)
tree = html.fromstring(page.content)

team_name = tree.xpath(xpath)

print(team_name)
