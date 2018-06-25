# -*- coding:utf-8 -*-
import os

import xlrd

from my_wxpython.base import *

__author__ = 'you'
__create_time__: '2017/8/25 22:18'


def open_work_dir(evt, view):
    config_dir = r"G:\个人账户\账户单"
    config_config = view.year.GetValue()
    config_file = os.path.join(config_dir, config_config)

    os.system("start {}".format(config_file))


def query(evt, view):
    view.result.Clear()
    config_dir = r"G:\个人账户\账户单"
    config_config = view.year.GetValue()
    config_file = os.path.join(config_dir, config_config)
    month_name = view.month.GetValue()

    try:
        data = xlrd.open_workbook(config_file).sheet_by_name(month_name)
        value_1 = data.col_values(0)  # 时间
        value_2 = data.col_values(4)  # 支出原因
        value_3 = data.col_values(3)  # 支出
        value_4 = data.col_values(1)  # 收入
        pay_reason = list()  # 支出原因
        pay_money = list()  # 当天付款金额
        all_data = dict()  # 保存所有数据

        for index, reason in enumerate(value_2):
            if value_1[index] in ["个人账户支出收入情况", "时间"]:
                continue
            if value_1[index]:
                pay_reason = list()
                pay_money = list()
                all_data[value_1[index]] = (pay_reason, pay_money)
                if reason:
                    pay_reason.append(reason)
                if value_3[index]:
                    pay_money.append(value_3[index])
            else:
                if reason:
                    pay_reason.append(reason)
                if value_3[index]:
                    pay_money.append(value_3[index])

        for date, reason in all_data.items():
            print("{}".format(date))
            print("{} : {}".format("支出原因", '，'.join(reason[0])))
            print("{0} : {1:.2f}".format("当天支付金额总数", money_total(reason[1])))
            print()

        print("{0} : {1:.2f}".format("本月份总收入", value_4[2]))
        print("{0} : {1:.2f}".format("本月份总支出", money_all_total(value_3)))
        print("{0} : {1:.2f}".format("本月份剩余余额", value_4[2] - money_all_total(value_3)))

    except xlrd.biffh.XLRDError:
        print("你输入的月份不存在")


def money_total(num_list):
    money_sum = 0
    for i in num_list:
        money_sum += i
    return money_sum


def money_all_total(value):
    money_sum = 0
    for i in value:
        if i in ["支出"]:
            continue
        if i:
            money_sum += i
    return money_sum
