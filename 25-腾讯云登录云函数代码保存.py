# -*- coding: utf8 -*-
import json


def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent = 2))
    print("Received context: " + str(context))

    json_params = json.loads(event.get('body'))

    user_name = json_params.get('username')
    print("当前的用户名为：", user_name)
    password = json_params.get('password')
    print("当前的密码为：", password)

    # 模拟查询数据库进行用户名和密码的判断
    if user_name == "admin" and password == "123456":
        login_ret = {"errno": 0, "errmsg": "登陆成功"}
    else:
        login_ret = {"errno": 1, "errmsg": "登陆失败！您输入的用户名密码为：%s : %s\n正确的用户名密码为admin : 123456" % (user_name, password)}

    # 封装为特定的数据给腾讯的统一出口
    ret = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        "body": json.dumps(login_ret)
    }

    return ret