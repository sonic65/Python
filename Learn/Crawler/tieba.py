from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

def get_html(url):
    headers = { 
        "User-Agent": UserAgent().chrome
    }
    request = Request(url,headers=headers)
    response = urlopen(request)
    # print(response.read().decode())
    return response.read()


def save_html(filename,html_bytes):
    with open(filename,"wb") as f:
        f.write(html_bytes)

def main():
    content = input("input your name of tieba :")
    num = input("下载的页数:")
    base_url ="https://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args = {
            "pn":pn*50,
            "kw":content
        }
    filename = "百度贴吧第" + str(pn)+ "页.html"
    args = urlencode(args)
    print(base_url.format(args))

    print("正在下载" + filename)
    # https://tieba.baidu.com/f?ie=utf-8&pn=0&kw=%E9%AD%94%E5%8D%A1%E5%B9%BB%E6%83%B3
    
    html_bytes = get_html(base_url.format(args))
    save_html(filename,html_bytes)

if __name__ == "__main__":
    main()