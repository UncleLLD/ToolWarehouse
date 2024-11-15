import time
import psutil
from datetime import datetime

from get_iphost import get_host_name
from email_notice import send_email


LOCAL_IP = get_host_name()
MAX_CPU_TH = 0.99
MAX_MEMORY_TH = 0.9
MAX_DISK_TH = 0.85
WAIT_TIME = 30  # 30 seconds

# monitor config
PIDS = ["pid1", "pid2"]
PID_NAMES = ['nginx', 'rabbitmq-server']
EMAILS = ["yourEmail"]


class Monitor:
    def __init__(self):
        # 获取 CPU 使用率
        self.cpu_percent = psutil.cpu_percent() / 100

        # 获取内存使用情况
        self.memory_info_percent = psutil.virtual_memory().percent / 100

        # 获取磁盘使用情况
        self.disk_info_percent = psutil.disk_usage('/').percent / 100

        # 获取进程信息
        self.processes = psutil.process_iter()
        self.pids = []
        self.pid_names = []
        for process in self.processes:
            self.pids.append(process.pid)
            self.pid_names.append(process.name())

    def monitor_res(self):
        if self.cpu_percent > MAX_CPU_TH:
            for email in EMAILS:
                send_email('平台通知', LOCAL_IP+' cpu负载过高!', email)
        if self.memory_info_percent > MAX_MEMORY_TH:
            for email in EMAILS:
                send_email('平台通知', LOCAL_IP+' 内存负载过高!', email)
        if self.disk_info_percent > MAX_DISK_TH:
            for email in EMAILS:
                send_email('平台通知', LOCAL_IP+' 硬盘内存负载过高!', email)
        for pid in PIDS:
            if pid not in self.pids:
                for email in EMAILS:
                    send_email('进程号通知', ' '.join([LOCAL_IP, str(pid), 'not alive!']), email)
        for pid_name in PID_NAMES:
            if pid_name not in self.pid_names:
                for email in EMAILS:
                    send_email('进程名字通知', ' '.join([LOCAL_IP, pid_name, 'not alive!']), email)
        return None


if __name__ == '__main__':
    mit = Monitor()
    # print(mit.cpu_percent)
    # print(mit.memory_info_percent)
    # print(mit.disk_info_percent)
    # print(mit.pids)
    # print(mit.pid_names)
    while True:
        print(datetime.now())
        mit.monitor_res()
        time.sleep(WAIT_TIME)
