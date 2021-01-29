import urllib.request

infile = urllib.request.urlopen('https://ko.wikisource.org/wiki/3%C2%B71%EB%8F%85%EB%A6%BD%EC%84%A0%EC%96%B8%EC%84%9C')
print(infile.read().decode())
