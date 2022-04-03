import requests

url = 'https://reqbin.com/echo'
x = requests.get(url, timeout=3)
print("Status code of GET request: ", end='')
print(x.status_code, end="\n\n")

print("Headers:")
for header in x.headers.items():
    print(header)
print()


print("Content:")
# could use print(x.text) but we want to make the html content prettier.
data = x.text.replace(">", ">\n\t")
print(data, end='')


# if you want post request:

# x = requests.post(url)
# print("Status code of POST request: ", end='')
# print(x.status_code)
# feel free to browse x's props
