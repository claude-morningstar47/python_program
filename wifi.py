import subprocess

process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-I'], stdout=subprocess.PIPE)
out, err = process.communicate()
process.wait()
print(out)


a = [12, 33, 44, 43, 10, 343]
a.sort()
print(a[0:4])