import json
import requests


# 发送get请求

# par = {'keywords':'yoyoketang'}
# r = requests.get('http://zzk.cnblogs.com/s/blogpost',params=par)
# print(r.status_code) # 调用response类里边的status_code方法，查看返回的状态码
# print(r.text)
'''
response类:
r.status_code  返回响应状态码
r.content      字节方式的响应体，会自动解码gzip和deflate压缩
r.headers      以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
r.json()       Requests中内置的JSON解码器
r.url          获取url
r.encoding     编码格式
r.cookies      获取cookie
r.raw          返回原始响应体
r.text         字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.raise_for_status()   失败请求(非200响应)抛出异常
'''


# 发送post请求

# payload = {'yoyo':'hello world',
#            'pythonQQ群':'226296743'}

# 转化成json格式
# data_json = json.dumps(payload)
# r = requests.post('http://httpbin.org/post',data=data_json)
# print(r.text)


# cookie完整的组成结构：
'''
cookie ={u'domain': u'.cnblogs.com',
        u'name': u'.CNBlogsCookie',
        u'value': u'xxxx',
        u'expiry': 1491887887,
        u'path': u'/',
        u'httpOnly': True,
        u'secure': False}

name：cookie的名称
value：cookie对应的值，动态生成的
domain：服务器域名
expiry：Cookie有效终止日期
path：Path属性定义了Web服务器上哪些路径下的页面可获取服务器设置的Cookie
httpOnly：防脚本攻击
secure:在Cookie中标记该变量，表明只有当浏览器和Web Server之间的通信协议为加密认证协议时，
浏览器才向服务器提交相应的Cookie。当前这种协议只有一种，即为HTTPS。

'''





# JSON数据处理

# 以下对应关系表是从json模块的源码里面爬出来的.python的数据类，经过encode成json的数据类型，对应的表如下
'''
|  | Python              | JSON          |
|  +===================+===============+
|  | dict                | object        |
|  +-------------- -----+---------------+
|  | list, tuple         | array         |
|  +-------------------+---------------+
|  | str, unicode        | string        |
|  +-------------------+---------------+
|  | int, long, float    | number        |
|  +-------------------+---------------+
|  | True                | true          |
|  +-------------------+---------------+
|  | False               | false         |
|  +-------------------+---------------+
|  | None                | null          |
|  +-------------------+--------------
'''

# 同样json数据转化成python可识别的数据，对应的表关系如下
'''
|  | JSON               | Python            |
|  +===============+===================+
|  | object             | dict              |
|  +---------------+-------------------+
|  | array              | list              |
|  +---------------+-------------------+
|  | string             | unicode           |
|  +---------------+-------------------+
|  | number (int)       | int, long         |
|  +---------------+-------------------+
|  | number (real)      | float             |
|  +---------------+-------------------+
|  | true               | True              |
|  +---------------+-------------------+
|  | false              | False             |
|  +---------------+-------------------+
|  | null               | None              |
|  +---------------+------------------
'''


# 案例：
# 比如打开快递网：http://www.kuaidi.com/，搜索某个单号，判断它的状态是不是已签收

# url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-754124003642212-zhongtong-UUCAO1608705865090.html"
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
#            }  # get方法其它加个ser-Agent就可以了
#
# s = requests.session()
# r = s.post(url, headers=headers,verify=False)
# result = r.json()
# data = result["data"]   # 获取data里面内容
# print(data)
# print(data[0])          # 获取data里的第一个
# get_result = data[0]['context']  # 获取已签收状态
# print(get_result)
#
# if u"签收" in get_result:
#     print("快递单已签收成功")
# else:
#     print("未签收")





# 重定向（Location）

# 案例：

# headers = {
#      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
#           }
# s = requests.session()
# # 打开我的随笔
# r = s.get('https://i.cnblogs.com/EditPosts.aspx?opt=1',
#           headers=headers,
#           allow_redirects=True,
#           verify=False)
# # 打印状态码，自动处理重定向请求
# print(r.status_code)
# new_url = r.headers["Location"]
# print(new_url)





# 参数关联

# 案例：

# url = "https://passport.cnblogs.com/user/signin"
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
#            "Accept": "application/json, text/javascript, */*; q=0.01",
#            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#            "Accept-Encoding": "gzip, deflate, br",
#            "Content-Type": "application/json; charset=utf-8",
#            "X-Requested-With": "XMLHttpRequest",
#            "Content-Length": "385",
#            "Cookie": "xxx已省略",
#            "Connection": "keep-alive"
#            }
#
# payload = {
#     "input1": "xxx",
#     "input2": "xxx",
#     "remember": True}
#
# # 第一步：session登录
# s = requests.session()
# r = s.post(url, json=payload, headers=headers, verify=False)
# print(r.json())
#
# # 第二步：保存草稿
# url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# body = {"__VIEWSTATE": "",
#         "__VIEWSTATEGENERATOR": "FE27D343",
#         "Editor$Edit$txbTitle": "这是我的标题：上海-6悠悠",
#         "Editor$Edit$EditorBody": "<p>这里是中文内容：http://www.cnblogs.com/yoyoketang/</p>",
#         "Editor$Edit$Advanced$ckbPublished": "on",
#         "Editor$Edit$Advanced$chkDisplayHomePage": "on",
#         "Editor$Edit$Advanced$chkComments": "on",
#         "Editor$Edit$Advanced$chkMainSyndication": "on",
#         "Editor$Edit$lkbDraft": "存为草稿",
#         }
#
# r2 = s.post(url2, data=body, verify=False)
# # 获取当前url地址
# print(r2.url)
#
# # 第三步：正则提取需要的参数值
# import re
# postid = re.findall(r"postid=(.+?)&", r2.url)
# print(postid)  # 这里是list
# # 提取为字符串
# print(postid[0])
#
# # 第四步：删除草稿箱
# url3 = "https://i.cnblogs.com/post/delete"
# json3 = {"postId": postid[0]}
# r3 = s.post(url3, json=json3, verify=False)
# print(r3.json())





# 参数化

# 案例：

def login(s, url, payload):
    '''登录'''
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
               "Accept": "application/json, text/javascript, */*; q=0.01",
               "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
               "Accept-Encoding": "gzip, deflate, br",
               "Content-Type": "application/json; charset=utf-8",
               "X-Requested-With": "XMLHttpRequest",
               "Content-Length": "385",
               "Cookie": "xxx已省略",
               "Connection": "keep-alive"
               }
    r = s.post(url, json=payload, headers=headers, verify=False)
    result = r.json()
    print(result)
    return result['success']    # 返回True或False

def save_box(s, url2, title, body_data):
    '''# 获取报存之后url地址'''
    body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "FE27D343",
        "Editor$Edit$txbTitle": title,
        "Editor$Edit$EditorBody": "<p>"+body_data+"</p>",
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage": "on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$lkbDraft": "存为草稿",
        }
    r2 = s.post(url2, data=body, verify=False)
    print(r2.url)
    return r2.url

def get_postid(u):
    '''正则提取postid'''
    import re
    postid = re.findall(r"postid=(.+?)&", u)
    print(postid)  # 这里是list
    if len(postid) < 1:
        return ''
    else:
        return postid[0]

def delete_box(s,url3, postid):
    '''删除草稿箱'''
    json3 = {"postId": postid}
    r3 = s.post(url3, json=json3, verify=False)
    print(r3.json())


# 调用上边定义的函数
if __name__ == "__main__":
    url = "https://passport.cnblogs.com/user/signin"
    payload = {
                "input1": "账号",
                "input2": "密码",
                "remember": True
               }
    s = requests.session()
    # 第1步登录
    login(s, url, payload,)
    url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    # 第2步保存
    u = save_box(s, url2, "标题", "正文内容")
    # 第3步提取postid
    postid = get_postid(u)
    url3 = "https://i.cnblogs.com/post/delete"
    # 第4步删除
    delete_box(s, url3, postid)













