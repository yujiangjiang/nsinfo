from utils.excel_utils import export
from utils.http_utils import get


def exportUser():
    params = {
        'pageNum': 1,
        'pageSize': 10
    }
    res = get("http://localhost:8081/api/v1/user/list", params=params, headers={'token': '5f727decece7a8f4e962b950e42f29bf'})


    title = [
        {'name': 'id', 'title': '用户id'},
        {'name': 'username', 'title': '用户名'},
        {'name': 'password', 'title': '密码'},
        {'name': 'status', 'title': '状态'},
        {'name': 'createTime', 'title': '创建时间'}
    ]

    export(title, res.data['list'], 'D:\\python_space\\nsinfo\\user.xls')






if __name__ == '__main__':
    exportUser()

