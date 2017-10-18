#!/usr/local/bin python
# -*- coding:utf-8 -*-
#とりあえず、xcs-master2のやつ丸つけ
"""
kはわかったけど、 その後の２つはよくわからない。
下のやつはアルゴリズムにある値だったので、使うことはわかる。
"""

class XCSConfig():
    k = 2
    max_iterations = 3000
    max_experiments = 10


    N = 600
    beta = 0.2
    alpha = 0.1

    epsilon_0 = 10

    nyu = 5
    gamma = 0.71

    theta_ga = 25
    chi = 0.8
    myu = 0.04

    theta_del = 20
    delta = 0.1
    theta_sub = 20

    p_sharp = 0.33
    p_explr = 0.5

    theta_mna = 2

    doGASubsumption = True
    doActionSetSubsumtion = True

XCSConfig = XCSConfig()
conf = XCSConfig
