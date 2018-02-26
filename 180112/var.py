#_*_coding:utf-8 _*_
def get():
    protocol = "http"
    domain = "www.baidu.com"
    uri = "a/b/index.html"
    data = "name=kkk&psw=123456"
    url = "{protocol}://{domain}/{uri}?{data}"
    print url.format(protocol = protocol,
                     domain = domain,
                     uri = uri,
                     data = data
                     )
def str_join():
    case = "case01"
    desc = "测试用例01"
    data = "id=1"
    method = """def case_{case}(self):
        '{desc}'
        execute_case('{data}')
    """
    print method.format(case = case,
                        desc = desc,
                        data = data
                        )

# str = r"hello world"
# str1 = "a=1&b=2&c=3&b=4"
# list1 = str1.split('&')
# for i in xrange(len(list1)):
#     if list1[i].find("b=") == 0:
#         list1[i] = "b= "
# list2 = "&".join(list1)
# for i,j in enumerate(list1):
#     if j.startswith("b="):
#         list1[i] = "b= "
# list2 = "&".join(list1)
# print list1
# print list2
