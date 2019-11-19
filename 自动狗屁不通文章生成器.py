#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re
import random
import readJSON

data = readJSON.讀JSON文件("data.json")
名人名言 = data["famous"]  # a 代表前面墊話，b代表後面墊話
前面墊話 = data["before"]  # 在名人名言前面弄點廢話
後面墊話 = data['after']  # 在名人名言後面弄點廢話
廢話 = data['bosh']  # 代表文章主要廢話來源

xx = "學生會退會"

重複度 = 2


def 洗牌遍歷(列表):
    global 重複度
    池 = list(列表) * 重複度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素


下一句廢話 = 洗牌遍歷(廢話)
下一句名人名言 = 洗牌遍歷(名人名言)


def 來點名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace("a", random.choice(前面墊話))
    xx = xx.replace("b", random.choice(後面墊話))
    return xx


def 另起一段():
    xx = "。 "
    xx += "\r\n"
    xx += "    "
    return xx


if __name__ == "__main__":
    xx = input("請輸入文章主題:")
    for x in xx:
        tmp = str()
        while (len(tmp) < 6000):
            分支 = random.randint(0, 100)
            if 分支 < 5:
                tmp += 另起一段()
            elif 分支 < 20:
                tmp += 來點名人名言()
            else:
                tmp += next(下一句廢話)
        tmp = tmp.replace("x", xx)
        print(tmp)
