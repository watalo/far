#!/usr/bin/env python
# -*- encoding: utf-8 -*-


'''far的核心内容之,在文档输出的时候可以直接调用相关的文字描述并能匹配固定的段落及变量
主要的内容包括：
    - 标题
    - 段落
        - 标准描述
        - 特殊分析
'''
from confpath import report_db

class Title():
    def __init__(self):
        """
        分析文件的标题
        """        
        self.H1 = '一、财务报表'
        self.H2 = '二、审计报告质量'
        self.H3 = '三、科目明细分析'
        self.H4 = '四、xxxxx'
        self.H5 = '五、yyyyy'
        self.H6 = '六、zzzzz'
        self.H7 = '七、xxxx'
        self.H8 = '八、yyyy'


class Paragraph():
    def __init__(self):
        self.db = report_db
        
    def ppr(self):
        print(self.db)

if __name__ == '__main__':
    p = Paragraph()
    t = Title()
    p.ppr()
    