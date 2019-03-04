from ..autoclass import AutoDatabank
from ..actionfunc import timedelta, parse, somedays
from ..actionfunc import swtime, checktime, two_check_time
from ..actionfunc import t365, t180, tnow
from .. import adbpath
import json

modulepath = adbpath.__file__[:-10] + 'setini/' + 'eightxx'

dglc = AutoDatabank(zhanghao=2, tmall_global=False, purchase_Behaviour='dp')
dglc.yybp_order = 0
dglc.ppld_order = 0
# set dglcR
with open(modulepath, 'w') as f:
    json.dump({'valuex': (2, False, 'dp', 0, 0, 2, 2, 2, '未命名')}, f)


def set_dglc(izhang_hao, tmall_global, p_type, yybp, ppld, ppzq, mxdp, zszw, brand_name):
    '''tmall_global：如果有出现 tmall_global，必填True 默认False
       p_typle：选择 店铺的行为，‘gj’为国际店行为，‘dp’为官方直营旗舰店行为'''
    global dglc
    dglc = AutoDatabank(zhanghao=izhang_hao,
                         tmall_global=tmall_global, purchase_Behaviour=p_type)
    dglc.yybp_order = yybp
    dglc.ppld_order = ppld
    dglc.ppzq_order = ppzq
    dglc.mxdp_order = mxdp
    dglc.zszw_order = zszw
    dglc.brand_name = brand_name

    with open(modulepath, 'w') as f:
        json.dump({'valuex': (izhang_hao, tmall_global,
                              p_type, yybp, ppld, ppzq, mxdp, zszw, brand_name)}, f)

#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#


def fuzhu_of_depth(tAs, tIs, tHs,
                   t2bef, t2end,
                   kwords, pph=True,
                   namess='def'):
    assert pph in [True, False]

    a1 = tAs
    a2 = swtime(t2bef, False) - timedelta(1)
    i1 = tIs
    i2 = swtime(t2bef, False) - timedelta(1)
    h1 = tHs
    h2 = swtime(t2bef, False) - timedelta(1)

    dglc.cp()
    dglc.yybp([1, 999], a1, a2, 2, action=2)
    dglc.ppld([1, 999], a1, a2, 2, action=2)
    dglc.ppzq([1, 999], a1, a2, 2, action=2)
    dglc.mxdp([1, 999], a1, a2, 2, action=2)
    dglc.zszw([1, 999], a1, a2, 2, action=2)
    dglc.dp(12345, a1, a2, 2)
    dglc.tm(1, a1, a2, 2)
    dglc.tm(3, a1, a2, 2)
    dglc.sp('%s【辅】旗店深A行为' % namess)

    dglc.cp()
    dglc.wt(1, a1, a2, 1)
    dglc.yybp([1, 999], a1, a2, 2, action=1)
    dglc.yybp([1, 999], a1, a2, 2, action=2)
    dglc.ppld([1, 999], a1, a2, 2, action=1)
    dglc.ppld([1, 999], a1, a2, 2, action=2)
    dglc.ppzq([1, 999], a1, a2, 2, action=1)
    dglc.ppzq([1, 999], a1, a2, 2, action=2)
    dglc.mxdp([1, 999], a1, a2, 2, action=1)
    dglc.mxdp([1, 999], a1, a2, 2, action=2)
    dglc.zszw([1, 999], a1, a2, 2, action=1)
    dglc.zszw([1, 999], a1, a2, 2, action=2)
    dglc.dp(12345, a1, a2, 2)
    dglc.tm(1, a1, a2, 2)
    dglc.tm(3, a1, a2, 2)
    dglc.sp('%s【辅】旗舰店A行为' % namess)

    dglc.cp()
    dglc.dp(12345, i1, i2, 1)
    dglc.tm(3, i1, i2, 2)
    dglc.tm(1, i1, i2, 2)
    dglc.sp('%s【辅】旗舰店I行为' % namess)

    dglc.cp()
    dglc.tm(3, i1, i2, 2)
    dglc.hy(2, i2, i2, 2)
    if pph:
        dglc.pph(2, 2, i2, i2, 2)
        dglc.pph(1, 2, i2, i2, 2)
    dglc.sp('%s【辅】超级用户' % namess)

    dglc.cp()
    dglc.dp(12345, h1, h2, 2)
    dglc.tm(3, h1, h2, 2)
    dglc.pph(1, 1, h1, h2, 2)
    dglc.pph(2, 1, h1, h2, 2)

    dglc.tbtt(2, h1, h2, 2)
    dglc.tbtt(3, h1, h2, 2)
    dglc.tbtt(4, h1, h2, 2)
    dglc.tbtt(5, h1, h2, 2)
    dglc.yhh(2, h1, h2, 2)
    dglc.yhh(3, h1, h2, 2)
    dglc.bmqd(2, h1, h2, 2)
    dglc.cnxh(1, h1, h2, 2)
    dglc.shyjs(2, h1, h2, 2)
    dglc.wt(4, h1, h2, 2)
    dglc.wt(5, h1, h2, 2)
    dglc.wt(6, h1, h2, 2)
    dglc.wt(7, h1, h2, 2)
    dglc.sp('%s【辅】活跃ZDY' % namess)

#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#


def _depths_of_aipl(tAs, tIs, t2bef, t2end,
                    with_people, namess, Xmodel):
    tpend = swtime(t2bef, 0) - timedelta(1)
    xmodelname = '未' if Xmodel == 3 else ''

    if with_people == 'gm':
        name = '【%s购' % xmodelname
    elif with_people == 'jd':
        name = '【%s进' % xmodelname
    elif with_people == 'bg':
        name = '【%s曝' % xmodelname
    elif with_people == 'sc':
        name = '【%s收' % xmodelname
    elif with_people == 'jg':
        name = '【%s加' % xmodelname
    elif with_people == 'scjg':
        name = '【%s收加' % xmodelname
    elif with_people == 'ys':
        name = '【%s预' % xmodelname
    elif with_people == 'no':
        name = ''
    elif with_people == 'jdbg':
        name = '【%s进曝光' % xmodelname
    else:
        raise SystemError

    def cp2():
        dglc.cp()
        if with_people == 'gm':
            dglc.dp(5, t2bef, t2end)
        elif with_people == 'jd':
            dglc.zdy('%s【辅】进店ZDY' % namess)
        elif with_people == 'bg':
            dglc.zszw([1, 999], t2bef, t2end)
        elif with_people == 'sc':
            dglc.dp(2, t2bef, t2end)
        elif with_people == 'jg':
            dglc.dp(3, t2bef, t2end)
        elif with_people == 'scjg':
            dglc.dp(23, t2bef, t2end)
        elif with_people == 'ys':
            dglc.dp(4, t2bef, t2end)
        elif with_people == 'jdbg':
            dglc.zszw([1, 999], t2bef, t2end)
            dglc.zdy('%s【辅】进店ZDY' % namess)

    #-------【AA】---------------★★★★★★★★★★#
    # cp2()
    #dglc.qll(234, t180, tpend, Xmodel)
    # dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    #dglc.sp('%sv1】全渠道A' % namess + name)

    # cp2()
    #dglc.qll(234, t180, tpend, Xmodel)
    # dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    #dglc.zdy('%s【辅】旗舰店A行为' % namess, 1)
    #dglc.sp('%sv2】旗店之A' % namess + name)

    cp2()
    dglc.zdy('%s【辅】旗舰店A行为' % namess, Xmodel)
    dglc.qll(234, t180, tpend, 3)
    dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    dglc.sp('%sv3】非店之A' % namess + name)

    ############ 旗舰店深浅A ##################
    cp2()
    dglc.zdy('%s【辅】旗店深A行为' % namess, Xmodel)
    dglc.qll(234, t180, tpend, 1)
    dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    dglc.zdy('%s【辅】旗舰店A行为' % namess, 1)
    dglc.sp('%sv4】旗店深A' % namess + name)

    cp2()
    dglc.zdy('%s【辅】旗店深A行为' % namess, Xmodel)
    dglc.qll(234, t180, tpend, 3)
    dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    dglc.zdy('%s【辅】旗舰店A行为' % namess, 1)
    dglc.sp('%sv5】旗店浅A' % namess + name)
    #-------【II】---------------★★★★★★★★★★#
    # cp2()
    #dglc.qll(34, tIs, tpend, Xmodel)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    #dglc.sp('%sv6】全渠道I' % namess + name)

    # cp2()
    #dglc.qll(34, tIs, tpend, Xmodel)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    #dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    #dglc.sp('%sv7】旗店之I' % namess + name)

    cp2()
    dglc.zdy('%s【辅】旗舰店I行为' % namess, Xmodel)
    dglc.qll(34, tIs, tpend, 3)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.sp('%sv8】非店之I' % namess + name)

    # cp2()
    #dglc.zdy('%s【辅】超级用户'%namess, Xmodel)
    #dglc.qll(34, tIs, tpend, 1)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    #dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    #dglc.sp('%sv9】超I-Total'%namess + name)

    cp2()
    dglc.dp(23, tIs, tpend, Xmodel)
    dglc.zdy('%s【辅】超级用户' % namess, 1)
    dglc.qll(34, tIs, tpend, 1)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv10】超I深I' % namess + name)

    cp2()
    dglc.dp(23, tIs, tpend, Xmodel)
    dglc.zdy('%s【辅】超级用户' % namess, 3)
    dglc.qll(34, tIs, tpend, 1)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv11】超I浅I' % namess + name)

    # cp2()
    #dglc.zdy('%s【辅】超级用户'%namess, Xmodel)
    #dglc.qll(34, tIs, tpend, 3)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    #dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    #dglc.sp('%sv12】非超I-Total'%namess + name)

    cp2()
    dglc.dp(23, tIs, tpend, Xmodel)
    dglc.zdy('%s【辅】超级用户' % namess, 1)
    dglc.qll(34, tIs, tpend, 3)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv13】非超I深I' % namess + name)

    cp2()
    dglc.dp(23, tIs, tpend, Xmodel)
    dglc.zdy('%s【辅】超级用户' % namess, 3)
    dglc.qll(34, tIs, tpend, 3)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv14】非超I浅I' % namess + name)

    #-------【PL】---------------★★★★★★★★★★#
    # cp2()
    #dglc.qll(34, t180, tpend, Xmodel)
    #dglc.sp('%sv15】全部PL' % namess + name)

    # cp2()
    #dglc.dp(5, t365, tpend, Xmodel)
    #dglc.qll(34, t180, tpend, 1)
    #dglc.sp('%sv16】旗舰店PL'%namess + name)

    t365 = '2018-3-10'

    cp2()
    dglc.zdy('%s【辅】活跃ZDY' % namess, Xmodel)
    dglc.dp(5, t365, tpend, 1)
    dglc.qll(34, t180, tpend, 1)
    dglc.sp('%sv17】旗店PL活跃' % namess + name)

    cp2()
    dglc.zdy('%s【辅】活跃ZDY' % namess, Xmodel)
    dglc.dp(5, t365, tpend, 3)
    dglc.qll(34, t180, tpend, 1)
    dglc.sp('%sv18】旗店PL非活' % namess + name)

    # cp2()
    #dglc.dp(5, t365, tpend, Xmodel)
    #dglc.qll(34, t180, tpend, 3)
    #dglc.sp('v19%s】非店PL'%namess + name)

    cp2()
    dglc.zdy('%s【辅】活跃ZDY' % namess, Xmodel)
    dglc.dp(5, t365, tpend, 1)
    dglc.qll(34, t180, tpend, 3)
    dglc.sp('%sv20】非店PL活跃' % namess + name)

    cp2()
    dglc.zdy('%s【辅】活跃ZDY' % namess, Xmodel)
    dglc.dp(5, t365, tpend, 3)
    dglc.qll(34, t180, tpend, 3)
    dglc.sp('%sv21】非店PL非活' % namess + name)

#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#


def depths_of_aiplxModel(tAs, tIs, t2bef, t2end,
                         with_convert_of_people='No', namess='def'):
    _depths_of_aipl(tAs, tIs, t2bef, t2end,
                    with_convert_of_people, namess, Xmodel=3)


def depths_of_aipl(tAs, tIs, t2bef, t2end,
                   with_convert_of_people='No', namess='def'):
    _depths_of_aipl(tAs, tIs, t2bef, t2end,
                    with_convert_of_people, namess, Xmodel=1)
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
