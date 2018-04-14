# -*- coding: utf-8 -*-
"""
注意，经过测试，pandas版本0.21.0会报错。0.20.0以及以下正常使用，
这个错误的原因是pandas团队在新的版本（0.21.0）中对idxmax函数的设计没有考虑周全。
所以，建议使用pandas的版本为0.20.0。
"""


import numpy as np
import pandas as pd

#zwQuant
import zwSys as zw
import zwTools as zwt
import zwQTBox as zwx
import zwQTDraw as zwdr
import zwBacktest as zwbt
import zwStrategy as zwsta
import zw_talib as zwta

#=======================    

    
def bt_endRets(qx):
    #---ok ，测试完毕
    # 保存测试数据，qxlib，每日收益等数据；xtrdLib，交易清单数据
    #qx.qxLib=qx.qxLib.round(4)
    qx.qxLib.to_csv(qx.fn_qxLib,index=False,encoding='utf-8')
    qx.xtrdLib.to_csv(qx.fn_xtrdLib,index=False,encoding='utf-8')
    qx.prQLib()
    #
    #-------计算交易回报数据
    zwx.zwRetTradeCalc(qx)
    zwx.zwRetPr(qx)

    # 使用自定义输出结果，步奏一：需要屏蔽如下内容
    '''
    #-------绘制相关图表，可采用不同的模板
    # 初始化绘图模板：dr_quant3x
    zwdr.dr_quant3x_init(qx,12,8);
    #  设置相关参数
    xcod=zw.stkLibCode[0];ksgn=qx.priceBuy;
    #xcod='glng';ksgn=qx.priceBuy;
    #kmid8=[['aeti',ksgn],['egan',ksgn],['glng',ksgn,'ma_5','ma_30'],['simo',ksgn,'ma_5','ma_30']]   
    mstr1,mstr2,mstr3='macd','msign','mdiff'
    kmid8=[[xcod,ksgn,mstr1,mstr2,mstr3]]

    # 绘图
    zwdr.dr_quant3x(qx,xcod,'val',kmid8,'')
    # 可设置，中间图形窗口的标识
    #qx.pltMid.legend([]);
    #
    '''

    print('')
    print('每日交易推荐')
    print('::xtrdLib',qx.fn_xtrdLib)
    print(qx.xtrdLib.tail())
    #print(qx.xtrdLib)


    # 使用自定义输出结果，步奏二：在本函数末尾添加。
    if qx.plotly_mode_flag == True:
        zwdr.my_plotly_show(qx)
    else:
        zwdr.my_qunt_plot(qx)



#==================main
#--------init，设置参数
rss='dat\\'  #rss='\\zwdat\\cn\\day\\'
xlst=['600401']   #600401,*ST海润
qx=zwbt.bt_init(xlst,rss,'macd20',10000)

#---设置策略参数
qx.staVars=[12,26,'2015-01-01','']    
qx.debugMod=1
qx.plotly_mode_flag = True
qx.staFun=zwsta.macd20 #---绑定策略函数&运行回溯主函数

#---根据当前策略，对数据进行预处理
zwsta.macd10_dataPre(qx,'macd20','close')
#----运行回溯主程序

zwbt.zwBackTest(qx)
#----输出回溯结果
bt_endRets(qx) #
    
