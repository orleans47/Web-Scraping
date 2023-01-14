#! python3
# download_skcd.py # Downloads every single XKCD comic


import requests, os, bs4

url = "https://xkcd.com/" # starting url
os.makedirs("xkcd", exist_ok=True) # store comics in /xkcd


while not url.endswith("#"):
    # Download the page
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")
    # Find the URL of the comic image
    ComicElem = soup.select("#comic img")
    if ComicElem == []:
        print("Could not find comic image")
    else:
        comic_url = "https:" + ComicElem[0].get("src")

    # Download the image
    print(f"Downloading image {comic_url}")
    res = requests.get(comic_url)
    res.raise_for_status()

    # Save the image to /skcd
    with open(os.path.join("xkcd", os.path.basename(comic_url)),"wb") as image_file:
        for chunk in res.iter_content(100000):
            image_file.write(chunk)

    # Get the prev button's URL
    prev_link = soup.select('a[rel = "prev"]')[0]
    url = "https://xkcd.com" + prev_link.get("href")

print("Done")
