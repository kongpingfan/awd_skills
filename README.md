
## 修改密码

* ssh密码

* mysql密码

* 网站应用的密码


## 下载web目录
* Scp

* FileZilla

## 扫描预留后门

将整个web目录下载到本地后，使用D盾扫描。

发现后门后，第一时间删除，同时利用这个漏洞发起第一波攻击，如果利用菜刀连，显然不够优雅，还没连完，人家估计都删的差不多了，因此这个漏洞虽然是送分，但拼的是手速，因此得提前准备好脚本

自写敏感功能。主办方可能已经把CMS本身的漏洞补全了，并自写了一些敏感功能，如上传、包含界面..，这时候需要自己手动去发现（利用seay代码审计工具可快速定位、ls -t按修改时间来看最新被修改的文件），分析，删除，利用；


## 日志记录


## 端口扫描及主机发现


* httpscan.py

我将其更改为python3版本了，不过这个工具真的难用……

Usage：./httpscan IP/CIDR –t threads

Example:
```
python3 httpscan.py 10.20.30.0/24 –t 10
```

* Nmap

```shell
nmap –sn 192.168.71.0/24
```



## 一句话木马
* php

* jsp

* aspx




