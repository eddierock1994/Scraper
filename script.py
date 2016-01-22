import urllib.request
import re
import subprocess

page = urllib.request.urlopen('https://www.zomato.com/chennai/mash-besant-nagar')
contents = str(page.read())
#print(contents)

#substring = contents["&zid=":5]

res_id=re.search('&zid=(.+?)&zsource',contents).group(1)
#print(found)















name = "sh execute.sh "
#res_id = "70921"
subprocess.call([name + res_id],shell=True)
