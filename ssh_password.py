import paramiko
import threading
import logging
import datetime

"""
此脚本可以执行ssh命令，命令执行的结果保存到log中。
默认行为是批量更改每台主机的密码，也可以自定义命令
请更改71-80行，根据实际情况自定义username, password, ip_list等
"""


class SSHCommandExecution:
    def __init__(self, ip_list, cmd, username, password, port):
        """
        username + password + port：根据实际情况填，例如root + 123456
        这个ip_list要自己来填，根据实际情况，把要执行命令的ip往里面塞。
        """
        self.cmd = cmd
        self.USERNAME = username
        self.PASSWORD = password
        self.PORT = port
        self.ip_list = ip_list
        self.logger = SSHCommandExecution.get_logger(level=logging.DEBUG)

    @staticmethod
    def get_logger(level=logging.DEBUG):
        """返回一个logger用来记录日志"""
        logger = logging.getLogger(__name__)
        today = datetime.datetime.today().strftime('%Y-%m-%d')

        fh = logging.FileHandler('SSHExecution-' + today + '.log', 'a')
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        fh.setLevel(level)
        logger.addHandler(fh)

        logger.setLevel(level)
        return logger

    def ssh(self, ip, cmd):  # 批量修改ssh密码/执行命令
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, self.PORT, self.USERNAME, self.PASSWORD, timeout=3)
            for m in cmd:
                stdin, stdout, stderr = ssh.exec_command(m)
                out = stdout.readlines()
                self.logger.debug("IP: " + ip + ", " + "Execute cmd: " + m)
                for o in out:
                    self.logger.debug(o)
                    print(o),
            print('%s\tOK\n' % ip)
            self.logger.debug('%s\tOK\n' % ip)
            ssh.close()
        except:
            self.logger.warning("IP: " + ip + ", " + "Execute cmd: " + " ".join(cmd) + " FAILED!")
            print('%s\tError\n' % ip)

    def ssh_execmd(self):  # 调用ssh函数执行命令
        iplist = self.ip_list
        cmd = self.cmd
        print("Begin......")
        if len(iplist) == 1:
            self.ssh(iplist[0], cmd=cmd)  # 单个IP的情况
        else:
            for i in iplist:
                a = threading.Thread(target=self.ssh, args=(i, cmd))
                a.start()


username = "root"
old_password = "123456"
new_password = "newpassword"
port = 22
change_password_cmd = 'echo "{0}:{1}" | chpasswd'.format(username, new_password)
cmd = [change_password_cmd]

ip_list = []
for i in range(1, 256):  # 实例代码，根据实际情况更改。
    ip_list.append("192.168." + str(i) + ".1")

a = SSHCommandExecution(ip_list, cmd, username, old_password, port)
a.ssh_execmd()
