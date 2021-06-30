import requests, random, sys, time
from bs4 import BeautifulSoup


def typing(s, tm=None):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        if tm:
          time.sleep(random.random() * tm)
        else:
          time.sleep(random.random() * 0.1)

def fbdl(url):
    r  = requests.post("https://www.getfvid.com/downloader", data={"url": url}).text
    bs = BeautifulSoup(r, "html5lib")
    htemel = bs.find("div", class_="col-md-4 btns-download")
    url = htemel.find_all("a")
    dataz = {}
    for f in url:
        if "HD" in f.text:
            dataz["hd"] = f["href"]
        if "Normal" in f.text:
           dataz["normal"] = f["href"]
        if "Audio" in f.text:
           dataz["audio"] = f["href"]
    data = {"ststus" : 200, "result": dataz}
    return data

def generate_name(val):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    gen = ''.join(random.choice(abc) for _ in range(val))
    return gen

def downloadUrl(url, ext=None):
    res = requests.get(url, allow_redirects=True)
    if res.status_code == 200:
        content_type = res.headers['Content-Type']
        if ext:
          filename = generate_name(10)+"."+ext
        else:
          filename = generate_name(10)+"."+content_type.split("/")[1]
        with open(filename, 'wb') as f:
          f.write(res.content)
        return filename


print("\n███████╗██╗░░██╗░█████╗░███████╗  ███████╗███████╗")
print("╚════██║██║░░██║██╔══██╗██╔════╝  ╚════██║╚════██║")
print("░░███╔═╝███████║██║░░██║█████╗░░  ░░░░██╔╝░░░░██╔╝")
print("██╔══╝░░██╔══██║██║░░██║██╔══╝░░  ░░░██╔╝░░░░██╔╝░")
print("███████╗██║░░██║╚█████╔╝███████╗  ░░██╔╝░░░░██╔╝░░")
print("╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝  ░░╚═╝░░░░░╚═╝░░░\n")

typing("WELCOME GAYS...\nTHIS IS TOLS FACEBOOK DOWNLOADER")    
url = input("input url : ")
data = fbdl(url)
qwali = [a for a in data["result"]]
print("========================================")
tx = "please type a number"
no = 0
for i in qwali:
  no +=1
  tx += f"\n{no}. {i}"
typing(tx)
inp = input("=>  ")
change = qwali[int(inp)-1]
print("========================================")
typing("PLEASE WAIT ......")
url = data["result"][change]
if change == "audio":
  dl = downloadUrl(url, "mp3")
else: 
  dl = downloadUrl(url)
typing("success download : "+dl)


