import requests

#resp=requests.get("https://gorest.co.in/public/v1/users")
#resp=requests.get("https://reqres.in/api/users?page=2")
'''print(resp)
print(type(resp))
print(dir(resp))'''
'''code=resp.status_code
assert code == 200, f"Code {code} doesn't match 200"

#print(resp.text)
#print(resp.content)
print(resp.json())
print(type(resp.headers))
print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)'''

url = "https://gorest.co.in/public/v1/users"
url_encoded_parameters = {"page":1}


def get_users(url, *args, **kwargs):
    """Function that gets users from site using get request
    and pick status code"""

    resp = requests.get(url, *args, **kwargs)
    #print(resp.headers)
    #print(resp.url)
    json_response = resp.json()
    #print(json_response['meta']['pagination']['pages'])
    #assert json_response['meta']['pagination']['pages'] == 80
    #print(json_response)
    #print(json_response['data'][19])
    return json_response,resp.status_code


if __name__ == '__main__':
    jsn1, code1 = get_users(url)
    jsn2, code2 = get_users(url, url_encoded_parameters)
    assert jsn1 == jsn2, "Results are not equal"