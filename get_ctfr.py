import requests
query=input('Enter Query:')
url = 'https://crt.sh/?q=%.'+query+'&output=json'

response = requests.get(url,verify=False)


host_list=[]
if response.status_code == 200:
    data = response.json()
    with open("urls.out", "a") as f:

        for i in range(len(data)):
            host_list.append(data[i]['common_name'])
            f.write(str(data[i]['common_name'])+'\n')
        
else:
    print('Request failed')
