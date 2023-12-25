# 写一个python代码，根据传入的经纬度，输出对应的地理瓦片行列号。具体算法为，根据输入的经纬度的值和最大层级数，找到对应的瓦片行列号，返回行列号的值。
# 1. 经纬度和最大层级数输入
# 2. 根据最大层级数，解析瓦片总数，并输出瓦片总数
# 3. 根据经纬度，解析对应的瓦片行列号，并输出行列号

import math
import sys

# 1. 经纬度和最大层级数输入

# 2. 根据最大层级数，解析瓦片总数，并输出瓦片总数
def tile_num(level):
    if level == 0:
        num = 2
    else:
        num = 2 * 4 ** level
    return num

# 3. 根据经纬度和最大层级树木，解析对应的瓦片行列号，并输出行列号
def tile_xy(lng, lat, level):

    # DOM行列号从左下角开始计算
    x = (math.floor((lng+180)/360*math.pow(2,(level+1))))
    # y = (math.floor((1-math.log(math.tan(lat*math.pi/180) + 1/math.cos(lat*math.pi/180))/math.pi)/2 *math.pow(2,(level))))
    # y = math.floor((lat+90)/180*math.pow(2,(level)))
    y = (math.floor((1+math.log(math.tan(lat*math.pi/180) + 1/math.cos(lat*math.pi/180))/math.pi)/2 *math.pow(2,level))); 

    return x, y, level

# 4.运行入口
if __name__ == '__main__':

    # 输入经纬度\最大层级数
    # lng = float(input("请输入经度:"))
    # lag = float(input("请输入纬度:"))
    # level = int(input("请输入最大层级数:"))
    
    lng = 113.936239
    lag = 22.533883
    # level = 2
    for i in range(0, 9):
        level = i
        a = tile_xy(lng, lag, level)
        print("瓦片总数为：", tile_num(level))
        print("瓦片行列和层级号为：", a)
    