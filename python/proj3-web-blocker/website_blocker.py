import time
from datetime import datetime as dt

hosts_path = "hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "twitter.com"]

while True:
    if 8 < dt.now().hour < 14:
        print("Work time...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if not website in content:
                    print(website, ": adding to blocked")
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun time...")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                else:
                    print(line.split(" ")[-1].rstrip(), ": unblocking")
            file.truncate()
    time.sleep(5)
