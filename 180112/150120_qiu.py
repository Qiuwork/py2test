#_*_ coding:utf-8 _*_
# Author: Qiu
#大脚超市赊账人员名单如下：
#['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿']
#大脚想移除掉里面的姓氏重复的人（不考虑复姓），但是对于每种姓氏大脚想保留最后出现的那个人。希望你来帮助她
import json

def dajiao():
    credit_list = ['刘能', '王老七', '谢广坤', '赵玉田', '杨晓燕', '刘大脑袋', '王长贵', '谢飞机', '赵四', '王大拿']
    new_list = sorted(credit_list, key=lambda x: x[0:3], reverse=True)  ##按元素的第一个中文字符排序。
    n_list = []
    d_list = []
    for i in new_list:
        if i[0:3] not in n_list:
            n_list.append(i[0:3])
        else:
            d_list.append(i)
    for d in d_list:
        new_list.remove(d)
    print json.dumps(new_list, ensure_ascii=False)
    print '-------------------------'
    return new_list
dajiao()

#编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
# data = {
#             '小明':{'语文':60, '数学':68, '英语':45},
#             '小璐':{'语文':10, '数学':28, '英语':5},
#             '小辉':{'语文':44, '数学':86, '英语':73},
#             '小亮':{'语文':99, '数学':95, '英语':95},
#             '田老师':{'语文':98, '数学':65, '英语':100},
#             '刘老师':{'语文':77, '数学':97, '英语':65},
#        	}
# a.找到平均分不足60分的人，
# b.找出各科的最高分,平均分
# c.找出各科的学霸

def data_analysis():
    data = {
        '小明':{'语文':60, '数学':68, '英语':45},
        '小璐':{'语文':10, '数学':28, '英语':5},
        '小辉':{'语文':44, '数学':86, '英语':73},
        '小亮':{'语文':99, '数学':95, '英语':95},
        '田老师':{'语文':98, '数学':65, '英语':100},
        '刘老师':{'语文':77, '数学':97, '英语':65},
    }
    yu_list = []
    shu_list = []
    ying_list = []
    bad_list = []
    for name,report in data.items():
        if sum(report.values()) / len(report) < 60:
            bad_list.append(name)
        for course,score in report.items():
            if course == '语文':
                yu_list.append(score)
            if course == '数学':
                shu_list.append(score)
            if course == '英语':
                ying_list.append(score)
    yu = max(yu_list)
    shu = max(shu_list)
    ying = max(ying_list)
    yu_avg = float(sum(yu_list)) / len(data)
    shu_avg = float(sum(shu_list)) / len(data)
    ying_avg = float(sum(ying_list)) / len(data)
    print "平均分不足60分的名单：%s" % json.dumps(bad_list,ensure_ascii=False)
    print "语文的最高分为%d，平均分为%0.2f；数学的最高分为%d，平均分为%0.2f；英语的最高分为%d，平均分为%0.2f."\
          % (yu,yu_avg,shu,shu_avg,ying,ying_avg)
    for name,report in data.items():
        if report.values()[report.keys().index('语文')] == yu:
            print "语文的学霸是%s" % name
        if report.values()[report.keys().index('数学')] == shu:
            print "数学的学霸是%s" % name
        if report.values()[report.keys().index('英语')] == ying:
            print "英语的学霸是%s" % name
    print '-------------------------'
    return bad_list
data_analysis()

#统计一篇英文文章每个单词的出现频率，并返回出现频率最高的前5个单词及其出现次数(字典形式)
#A small sample of texts from Project Gutenberg appears in the NLTK corpus collection.
#  However, you may be interested in analyzing other texts from Project Gutenberg.
# You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/,
# and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English,
# it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian

#如果需要包含并列第五的单词，直接执行top5();如果只需要获取前五的单词，将107-109行注释掉。
def top5():
    notes = "A small sample of texts from Project Gutenberg appears in the NLTK corpus collection.\
     However, you may be interested in analyzing other texts from Project Gutenberg. \
     You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, \
     and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, \
     it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian"
    sp_list = notes.split()
    for i in range(len(sp_list)):
        if sp_list[i].endswith('.') or sp_list[i].endswith(','):
            sp_list[i] = sp_list[i][:-1]
    note_dict = {}
    for note in sp_list:
        if note_dict.get(note):
            continue
        else:
            note_dict[note] = sp_list.count(note)
    new_list = sorted(note_dict.items(),key=lambda x:x[1],reverse=True)
    num = 5
    for i in range(5,len(new_list)-1):  #包含并列第五的单词，如只需前五，注释掉这个for循环代码段。
        if new_list[4][1] == new_list[i][1]:
           num = i + 1
    top5_dict = dict(new_list[:num])
    print top5_dict
    print '-------------------------'
    return top5_dict
top5()

