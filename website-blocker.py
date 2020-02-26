import time
from datetime import datetime as dt
host_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["facebook.com","google.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12):
        print("Working hour....")
        with open("hosts","r+") as host:
            content = host.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    host.write(redirect+" "+website+"\n")
    else:
        with open("hosts","r+") as host:
            content = host.readlines()
            host.seek(0) # put the cursor at 0 position
            for line in content:
                if not any(website in line for website in website_list):
                    host.write(line)
            host.truncate() # Delete all the lines below

    time.sleep(5)
