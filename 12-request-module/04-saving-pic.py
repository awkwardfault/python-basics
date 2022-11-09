import requests  # we need to import request module first

# then wew need to write down the target image
img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/GitHub_logo_2013.svg/220px-GitHub_logo_2013.svg.png'

r = requests.get(img_url)  # we are going to identify the whole process as 'r'

with open('pybook.png', 'wb') as f:  # 'with' is a saved statement in python look in 00
    f.write(r.content)
