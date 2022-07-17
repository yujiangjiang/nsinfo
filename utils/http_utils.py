import json

import requests

from dto.common_dto import RestResult


def get(url, params={}, headers={}):
    if 'Content-Type' not in headers.keys() or headers['Content-Type'] is None or headers['Content-Type'] == '':
        headers['Content-Type'] = 'application/json'

    response = requests.get(url, params=params, headers=headers)
    text = response.text
    res = json.loads(text)
    if res['code'] == 200:
        return RestResult.success(res['data'])
    raise Exception(response.text)


def post(url, data={}, headers={}):

    if 'Content-Type' not in headers.keys() or headers['Content-Type'] is None or headers['Content-Type'] == '':
        headers['Content-Type'] = 'application/json'

    jsonData = json.dumps(data)
    response = requests.post(url, data=jsonData, headers=headers)
    res = json.loads(response.text)
    if res['code'] == 200:
        return RestResult.success(res['data'])
    raise Exception(response.text)


if __name__ == '__main__':
    data = {
        "username": "anna",
        "password": "314130"
    }
    # result = post("http://localhost:8081/api/v1/user/login", data, {'Content-Type': ''})
    # print(result.data)
    params = {
        'pageNum': 1,
        'pageSize': 10
    }
    res = get("http://localhost:8081/api/v1/user/list", params=params, headers={'token': '5f727decece7a8f4e962b950e42f29bf'})
    print(res.data)
