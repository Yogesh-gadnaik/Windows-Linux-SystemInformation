from model.dictinory import getWindowsInfo, getLinuxInfo


def sys_windows(info):
    sys_info = getWindowsInfo()
    if info == "allinfo":
        return sys_info
    else:
        result={info:sys_info[info]}
        return result


def sys_linux(info):
    sys_info = getLinuxInfo()
    if info == "allinfo":
        return sys_info
    else:
        result={info:sys_info[info]}
        return result
