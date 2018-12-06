

def flag_submit(flag):
    """提交flag"""
    import requests

    burp0_url = ""
    burp0_cookies = {"PHPSESSID": "30bnlp2apsc9acu5g1qf650es4"}
    burp0_headers = {"Accept": "*/*", "Origin": "http://100.100.100.200", "X-Requested-With": "XMLHttpRequest",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"answerVal": flag}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)