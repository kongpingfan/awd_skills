import requests


def submit_flag(flag):
    platform = input("[*]please input your platform url:")
    cookie = input("[*]please give me your cookies:").split(";")
    cookies = {}
    for i in range(len(cookie)):
        cookie1 = cookie[i].split("=")
        cookies[cookie1[0]] = cookie1[1]
    for i in flag:
        try:
            submit = requests.post(url=platform, cookies=cookies, data=i)
            print(submit.content)
        except:
            print("[*] sorry,submit flag error!")
