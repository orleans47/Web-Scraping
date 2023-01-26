import requests
from bs4 import BeautifulSoup

url = "https://file-examples.com/index.php/sample-documents-download/sample-xls-download/"
headers = {
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
}

response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, "lxml")

# Store the urls from the pages
urls = []

# Get the urls
downloads =soup.find_all("a",class_ = 'download-button')

for download in downloads:
    urls.append(download["href"])


# download the files within those urls
for i, url in enumerate(urls):
    files = requests.get(url, allow_redirects= True)
    file_name = "./excel_files/" + str(i) + ".xls"
    output = open(file_name, "wb")
    output.write(files.content)
    output.close()
