#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@NAME		:dataio.py
@TIME		:2022/06/29 14:26:01
@AUTHOR     :watalo
@VERSION	:0.0.x

模块内容：
对原始财务报表进行读取、格式化
    - 读取: pd.read_excel --> df
    - 格式化:
        - 行: 
            - 科目：增加各种财务指标，需要进行财务科目进行计算
            - 汇总：增加仅需要汇总相加的指标，如刚性兑付、营运资金量等指标
        - 列: 增加每年比上年的增量、增幅、在总资产、总负债、总权益、总收入占比
'''

import os
import pandas as pd
from openpyxl import load_workbook
from resourcepath import *


def read_fs_data(input_path):
    '''
    读取xlsx文件数据，为避免xlsx文件中包含公式，需要进行处理。
    @input_path: 原始报表数据的路径，相对/绝对都可
    '''
    # 使用openpyxl.load_workbook的data_only参数进行强制转换
    ws = load_workbook(input_path,
                       data_only=True)
    ws.save(os.path.abspath(input_path))
    fs_df = pd.read_excel(io=input_path,
                       sheet_name='Sheet1',
                       index_col=0) # 强制将科目名称作为行标签
    # 报表通常格式-->行：科目名称，列：日期
    return fs_df.T # 不知道需不需摇转换，先这么滴

def format_df(fs_df):
    '''
    1.设置科目属性：
    实际只需要对每个科目给一个值就标签
    科目分类为：
        新增行，name="科目分类"
        新增行，name="流动性", [False, True, NaN]
        从而实现
        - 资产
            - 流动资产
            - 非流动资产
        - 负债
            - 流动负债
            - 非流动负债
        - 权益
        - 损益
        - 现金流
        - 财务指标
            - 营运指标
            - 流动性分析
            - 偿债能力 
        - 统计统计
            - sum
            - mean
    2.计算多层行标签：
        前3年、前2年、前1年、当期、前3年d、前2年d、前1年d、当期d
    3、
    '''
    pass


if __name__ == '__main__':

    input_path = './far/far/test_financial_statement.xlsx'

    fs_data = read_fs_data(input_path)
    print(fs_data.describe())