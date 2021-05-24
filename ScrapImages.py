import requests
url = "https://authoraditiagarwal.com/wpcontent/uploads/2018/05/MetaSlider_ThinkBig-1080x180.jpg"
r = requests.get(url) 
with open("ThinkBig.png",'wb') as f:
   f.write(r.content) 

   #After running the above Python script, 
   # we will get a file named ThinkBig.png,
   #  which would have the downloaded image.

