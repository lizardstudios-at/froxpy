from requests.exceptions import *
import requests
import colorama

working_proxies = []
timeout_proxies = []
bad_proxies     = []

def gen_proxy_dict(proxy_list):
    proxy_dict = {}

    for proxy in proxy_list:
        proxy_dict[proxy.split('://')[0]] = proxy

    return proxy_dict

def test_proxies(proxies=[], timeout=15, output=False):
    for proxy in proxies:
        try:
            resp = requests.get('https://www.google.com/', timeout=timeout, proxies={ proxy.split('://')[0]: proxy })
            self.working_proxies.append(proxy)
            if output: print(colorama.Fore.GREEN + f'[+] {proxy} working')
        except ConnectTimeout:
            self.timeout_proxies.append(proxy)
            if output: print(colorama.Fore.RED   + f'[-] {proxy} timeout')
        except:
            self.bad_proxies.append(proxy)
            if output: print(colorama.Fore.RED   + f'[-] {proxy} not working')

    return (working_proxies, bad_proxies, timeout_proxies)
