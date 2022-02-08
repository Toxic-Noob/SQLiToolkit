import requests as r
import os, time, sys
import concurrent.futures as cf

def admin_finder():
    url = open("modules/paths.txt", "r").readlines()
    admin_finder.url = url
    site = input("\n\033[92m    [*] Enter Your Site Domain:> ")
    while "http" not in site:
        print("\n    \033[31m[!] Url Must Contain http:// or https://")
        time.sleep(0.5)
        site = input("\n\033[92m    [*] Enter Your Site Domain:> ")
    admin_finder()
    print("    [*] Scanning Started...\n")
    time.sleep(1)    
    admin_finder.site = site
    start()
    
    
def admin_find(url):
    try:
        site = admin_finder.site
        e = url.strip()
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'}
        res = r.get(site+e, headers = headers)
        code = int(res.status_code)
        if code < 400:
            print("\033[92m[   Found   ] : "+site+e)
        else:
            print("\033[31m[ Not Found ] : "+site+e)
    except Exception as e:
            print(e)

def start():
                url = admin_finder.url
                try:
                    with cf.ThreadPoolExecutor() as executor:
                        executor.map(admin_find,url)
                except:
                    print("\n[!] Network Connection Error!!!")
                    

