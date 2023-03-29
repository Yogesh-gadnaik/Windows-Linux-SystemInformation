import platform
import psutil
import wmi
import pythoncom
from datetime import datetime


def getWindowsInfo():
    pythoncom.CoInitialize()
    object_wmi = wmi.WMI()
    my_system = object_wmi.Win32_ComputerSystem()[0]
    # crete empty dictionary
    windows_sys = {}

    # inserting all info in dictionary from both platform and psutil module
    windows_sys['system'] = platform.system()
    windows_sys['node'] = platform.node()
    windows_sys['release'] = platform.release()
    windows_sys['version'] = platform.version()
    windows_sys['machine'] = platform.machine()
    windows_sys['processor'] = platform.processor()
    windows_sys['architecture_details'] = platform.architecture()
    windows_sys['platform_details'] = platform.platform()
    windows_sys['virtual_memory'] = psutil.virtual_memory()
    windows_sys['physical_core'] = psutil.cpu_count(logical=False)
    windows_sys['logical_core'] = psutil.cpu_count(logical=True)
    windows_sys['cpu_frequency'] = psutil.cpu_freq().current
    windows_sys['min_frequency'] = psutil.cpu_freq().min
    windows_sys['max_frequency'] = psutil.cpu_freq().max
    windows_sys['cpu_utilization'] = psutil.cpu_percent(interval=1)
    windows_sys['per_cpu_utilization'] = psutil.cpu_percent(
        interval=1, percpu=True)
    windows_sys['manufacturer'] = my_system.Manufacturer
    windows_sys['model'] = my_system. Model
    windows_sys['sysname'] = my_system.Name
    windows_sys['no_processors'] = my_system.NumberOfProcessors
    windows_sys['systemtype'] = my_system.SystemType
    windows_sys['systemfamily'] = my_system.SystemFamily
    return windows_sys


def getLinuxInfo():
    linux_sys = {}
    linux_sys['system'] = platform.system()
    linux_sys['node'] = platform.node()
    linux_sys['release'] = platform.release()

    linux_sys['version'] = platform.version()
    linux_sys['machine'] = platform.machine()
    linux_sys['processsor'] = platform.processor()
    linux_sys['architecture_details'] = platform.architecture()
    linux_sys['platform_details'] = platform.platform()
    with open("/proc/cpuinfo", "r") as f:
        proc = f.readlines()
        list = []
        cpuinfo = [x.strip().split(":")[1] for x in proc if "model name" in x]
        for item in enumerate(cpuinfo):
            list.append(item)
    linux_sys['cpu_info'] = list

    with open("/proc/loadavg", "r") as f:
        load = f.read().strip()
    linux_sys['load'] = load

    mem = []
    with open("/proc/meminfo", "r") as f:
        lines = f.readlines()
        for line in lines:
            mem.append(line)
    linux_sys['memeory'] = mem

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    linux_sys['boottime'] = boot_time

    return linux_sys
