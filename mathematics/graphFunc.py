#!/usr/bin/env python
# coding: utf-8

# In[47]:


import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
plt.rcParams['figure.dpi'] = 120
LOWER, UPPER = -10, 10  # 初始化区间上下界
INTERVAL = 200


# In[35]:


def openFolder(fPath):
    """
    判断文件夹是否存在

    Parameters
    ----------
    fPath : str
        文件夹路径
    """
    if os.path.exists(fPath):
        pass
    else:
        os.makedirs(fPath)


# In[61]:


def graphFunc(func1, func2=None, lower=LOWER, upper=UPPER, interval=INTERVAL, fPath='./images'):
    """
    根据输入的函数，绘制函数图像

    Parameters
    ----------
    func1 : function
        函数方程，y=f(x)或者极坐标方程p(θ)
    func2 : function
        函数方程，考虑为参数方程的情况。
        这是func1对应x的参数方程
        func2对应y的参数方程
    lower : int or float
        区间下限
    upper : int or float
        区间上限
    interval : int
        将区间划分的分数
    fPath : str
        文件夹路径
    """
    step = (upper - lower) / INTERVAL
    t = np.arange(lower, upper, step)  # 区间内各点

    fig = plt.figure()
    openFolder(fPath)
    fPath += '/' + \
        datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S") + '.png'
    # 判断是否为参数方程
    if(func2 is None):
        plt.plot(t, func1(t))
    else:
        plt.plot(func1(t), func2(t))

    plt.xlabel('x or θ')
    plt.ylabel('y or ρ')
    # plt.legend(loc='best')
    plt.show()
    fig.savefig(fPath)


# In[63]:


if __name__ == '__main__':
    def func1(x):
        return (np.cos(x))**3

    def func2(x):
        return (np.sin(x))**3
    graphFunc(func1, func2)