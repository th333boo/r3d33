import wget

url = 'https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.6.0-amd64-netinst.iso'
filename = wget.download(url)
print(filename)