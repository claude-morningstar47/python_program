import speedtest

speed_test = speedtest.Speedtest()

def bytes_to_md(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes/MB)

download_speed = bytes_to_md(speed_test.download())
print("Your Download speed is", download_speed, "MB")