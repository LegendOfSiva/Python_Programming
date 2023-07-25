import bs4
import requests

baseurl = 'https://windows10spotlight.com/page/'
for num in range(1, 3):
    current_url = baseurl+str(num)
    res = requests.get(current_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    images = soup.select('.thumbnail.wp-post-image')
    for image in images:
        image_url = str(image['src'])
        last_dash_index = image_url.rfind('-')
        image_url = image_url[:last_dash_index]+'.jpg'
        imagecontent = requests.get(image_url).content
        imagename = str(image['alt'])+'.jpg'
        with open(imagename, 'wb') as myimg:
            myimg.write(imagecontent)
