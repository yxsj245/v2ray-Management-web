import requests
import json

posturl = 'http://149.104.31.135:5000'
iphost = '149.104.31.135:5000'
apikey = 'vcvQW3SIwqgoSWCyUwq7cokt0sMLyiCd'

def update_node(port,time,internet,type):
    url = f"{posturl}/update/node"

    payload = json.dumps({
        "port": port,
        "time": time,
        "internet": internet,
        "type": type,
        "apikey":apikey
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': iphost,
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return True
    else:
        return False

def update_node_uuid(port):
    url = f"{posturl}/update/node_uuid"

    payload = json.dumps({
        "port": port,
        "apikey":apikey
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': iphost,
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    if response.status_code == 200:
        return True
    else:
        return False

def update_node_port(port,current_port):
    url = f"{posturl}/update/port"

    payload = json.dumps({
        "port": port,
        "current_port":current_port,
        "apikey":apikey
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': iphost,
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    if response.status_code == 200:
        return True
    else:
        return False

def add_node(port,time,internet):
    url = f"{posturl}/add/node"

    payload = json.dumps({
        "port": int(port),
        "time": time,
        "internet": internet,
        "apikey":apikey
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': iphost,
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print(response.text)
        return True
    else:
        return False

def add_node_measure(port,internet):
    url = f"{posturl}/add/node_measure"

    payload = json.dumps({
        "port": int(port),
        "internet": internet,
        "apikey":apikey
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': iphost,
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print(response.text)
        return True
    else:
        return False

def remove_node(port):
    url = f"{posturl}/remove/node"

    payload = json.dumps({
        "port": int(port),
        "apikey":apikey
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': iphost,
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return True
    else:
        return False

def check_node(port):
    url = f"{posturl}/check/node"

    payload = json.dumps({
        "port": int(port),
        "apikey":apikey
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': iphost,
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print(response.text)
        return True
    else:
        return False


print('1.更新信息 \n'
      '2.添加节点 \n'
      '3.删除节点 \n'
      '4.查看节点 \n'
      '5.添加节点(按量) \n'
      '6.更新节点UUID \n'
      '7.更换端口')
xuanze = input()
if xuanze == '1':
    port = input('请输入端口 例如 20002：')
    time = input('请输入到期时间 例如 2025-1-12 23:59:59：')
    internet = int(input('请输入流量KB：'))
    type = input('请输入类型 例如 updateinternet updatetime：')
    if update_node(port,time,internet,type):
        print('请求成功')
    else:
        print('请求失败')
if xuanze == '2':
    port = input('请输入端口 例如 20002：')
    time = input('请输入到期时间 例如 2025-1-12 23:59:59：')
    internet = int(input('请输入流量KB：'))
    if add_node(port,time,internet):
        print('请求成功')
    else:
        print('请求失败')
if xuanze == '3':
    port = input('请输入端口 例如 20002：')
    if remove_node(port):
        print('请求成功')
    else:
        print('请求失败')
if xuanze == '4':
    port = input('请输入端口 例如 20002：')
    if check_node(port):
        print('请求成功')
    else:
        print('请求失败')
if xuanze == '5':
    port = input('请输入端口 例如 20002：')
    internet = int(input('请输入流量KB：'))
    if add_node_measure(port,internet):
        print('请求成功')
    else:
        print('请求失败')
if xuanze == '6':
    port = input('请输入端口 例如 20002：')
    if update_node_uuid(port):
        print('请求成功')
    else:
        print('请求失败')
if xuanze == '7':
    port = input('请输入当前端口 例如 20002：')
    current_port = input('请输入更改后端口 例如 20003：')
    update_node_port(port,current_port)
    if update_node_uuid(port):
        print('请求成功')
    else:
        print('请求失败')