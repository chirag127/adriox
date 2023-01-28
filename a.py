import requests
from bs4 import BeautifulSoup

def download_file(url):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        file_name = url.split('/')[-1]

        # 120px-Flag_of_the_Republic_of_the_Congo.svg.png

        file_name = file_name.replace('120px-','')

        file_name = file_name.replace('.svg.png','.png')

        file_name = file_name.replace('.svg','.png')

        file_name = file_name.replace('.png.png','.png')
        with open(file_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        print('Image Couldn\'t be retrieved',url)

page = requests.get("https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags")
soup = BeautifulSoup(page.content)

for e in soup.select('img[src*="/Flag_of"]'):
    download_file('https:'+e.get('src'))