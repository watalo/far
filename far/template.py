#!/usr/bin/env python
# -*- encoding: utf-8 -*-


'''
本文件记载了所有需要被用到的文字型的内容。
This document records all the text types that need to be used.

1.脚本主要内容
    - Class Title --> 标题文本
    - Class Paragraph --> 段落文本
        - 标准描述 --> 标准的八段文字
        - 特殊情况 --> 按照不同的数据时间完整性进行分类
            - 有当期数据：'1111','0111','0011','0001'
            - 无当期数据：'1110','0110','0010'
    - Class Table --> 表格文本
    
2.脚本关联关系
    (1)被main引用
        from template import *
    (2)引用resourcepath

'''

def load(template_text, template_var):
    """
    装载模板的文本和对应的参数集合
    """
    pass

def type_fstime():
    """
    识别财务报表的期限类型
    """
    pass
    


# class Title():
#     def __init__(self):
#         """
#         标题
#         """        
#         self.h1 = '一、财务简表'
#         self.h2 = '二、审计情况'
#         self.h3 = '三、财务分析'
#         self.h4 = '四、'
#         self.h5 = '五、yyyyy'
#         self.h6 = '六、zzzzz'
#         self.h7 = '七、xxxx'
#         self.h8 = '八、yyyy'


# class Section():
#     def __init__(self):
#         self.db = report_db
        
#     def ppr(self):
#         print(self.db)

# class Tables():
#     def __init__(self, *args):
#         self.row = args


# if __name__ == '__main__':
#     p = Section()
#     t = Title()
#     p.ppr()
    
#     print(settings.TMP_PATH)
    