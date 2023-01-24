import requests
from bs4 import BeautifulSoup as bs

# Get morning messages

print("Searching...")

# use headers to make the page know we're not robots
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

url = "https://andro4all.com/whatsapp/frases-de-buenos-dias"
# Make and get the request from the webpage

response = requests.get(url, headers)

soup = bs(response.text, "lxml")

# Look for the messages
message_sections = soup.find("main", class_= "mrf-article-body m-article")
messages = message_sections.find_all("ul")[5]

# Append all the messages in the empty list
morning_list = []
for li in messages.find_all("li"):
    morning_list.append(li.get_text())

print(morning_list)

# Get the night messages
print("Searching...")

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

url2 = "https://andro4all.com/whatsapp/whatsapp-las-mejores-frases-e-imagenes-para-dar-las-buenas-noches"

response2 = requests.get(url2, headers)

# Create the soup object to parse the webpage
soup = bs(response2.text, "lxml")

# Parse the webpage
message_sections = soup.find("main", class_= "mrf-article-body m-article")
messages = message_sections.find_all("ul")[4]

# Create and empty list and get the text from the list of messages

night_messages = []

for li in messages.find_all("li"):
    night_messages.append(li.get_text())

print(night_messages)


# Save the program into a txt file

with open("Morning.txt", "w") as mor:
    for message in morning_list:
        mor.write(f"{message}\n")


with open("Night.txt", "w") as ni:
    for message in night_messages:
        ni.write(f"{message}\n")
