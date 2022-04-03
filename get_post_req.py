import requests

url = 'https://reqbin.com/echo'
x = requests.get(url, timeout=3)
print("Status code of GET request: ", end='')
print(x.status_code)
print()


print("Headers:")
for header in x.headers.items():
    print(header)
print()


print("Html content:")
# print(x.text)
# make the html content prettier:
data = x.text.replace(">", ">\n\t")
print(data)


x = requests.post(url)
print("Status code of POST request: ", end='')
print(x.status_code)
# print(x.text)
