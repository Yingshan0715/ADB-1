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
GLOBAL_SIGN = ''


def set_namesstt_sign(astr):
    global GLOBAL_SIGN
    GLOBAL_SIGN = astr


def namesstt(adatetime):
    # 支持同一时间的不同账号 以 英文字母为标识
    adatetime = swtime(adatetime, False)
    return '%s%d%02d' % (GLOBAL_SIGN, adatetime.month, adatetime.day)


def fuzhu_of_depth(tAs, tIs, tHs, tpend, kwords, pph=True):
    a1, i1, h1 = tAs, tIs, tHs
    a2, i2, h2 = tpend, tpend, tpend

    namess = namesstt(tpend)

    dglc.cp()
    # 深度A行为变更为全部账号
    # 附加 uidesk and ykgg
    dglc.super_ss(kwords, a1, a2, jbc='bb-BitCoin')
    dglc._fufeiguanggao(1, [1, 999], a1, a2, 2, action=2, position_of_Real=1)
    dglc._fufeiguanggao(2, [1, 999], a1, a2, 2, action=2, position_of_Real=1)
    dglc._fufeiguanggao(3, [1, 999], a1, a2, 2, action=2, position_of_Real=1)
    dglc._fufeiguanggao(4, [1, 999], a1, a2, 2, action=2, position_of_Real=1)
    dglc._fufeiguanggao(5, [1, 999], a1, a2, 2, action=2, position_of_Real=1)
    dglc._fufeiguanggao(6, [1, 999], a1, a2, 2, action=2, position_of_Real=1)
    dglc._fufeiguanggao(7, [1, 999], a1, a2, 2, action=2, position_of_Real=1)
    #dglc.yybp([1, 999], a1, a2, 2, action=2)
    #dglc.ppld([1, 999], a1, a2, 2, action=2)
    #dglc.ppzq([1, 999], a1, a2, 2, action=2)
    #dglc.mxdp([1, 999], a1, a2, 2, action=2)
    #dglc.zszw([1, 999], a1, a2, 2, action=2)
    dglc.dp(12345, a1, a2, 2)
    dglc.tm(1, a1, a2, 2)
    dglc.tm(3, a1, a2, 2)
    dglc.sp('%s【辅】旗店深A行为' % namess)

    dglc.cp()
    dglc.wt(1, a1, a2, 1)
    # 附加 uidesk and ykgg 店铺A行为只包含曝光
    #dglc.ud([1, 999], a1, a2, 2, action=1)
    #dglc.ykgg([1, 999], a1, a2, 2, action=1)
    dglc.yybp([1, 999], a1, a2, 2, action=1)
    dglc.ppld([1, 999], a1, a2, 2, action=1)
    dglc.ppzq([1, 999], a1, a2, 2, action=1)
    dglc.mxdp([1, 999], a1, a2, 2, action=1)
    dglc.zszw([1, 999], a1, a2, 2, action=1)

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
    dglc.wt_gg(2, i2, i2, 2)
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

    dglc.tbtt(1, h1, h2, 2)

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


def depths_of_aipl(tAs, tIs, tpend, tPLs=False):
    namess = namesstt(tpend)

    #-------【AA】---------------★★★★★★★★★★#
    # dglc.cp()
    # dglc.qll(234, t180, tpend)
    # dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    # dglc.sp('%sv1】全渠道A' % namess)

    # dglc.cp()
    # glc.qll(234, t180, tpend)
    # dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    # dglc.zdy('%s【辅】旗舰店A行为' % namess, 1)
    # dglc.sp('%sv2】旗店之A' % namess)

    dglc.cp()
    dglc.zdy('%s【辅】旗舰店A行为' % namess)
    dglc.qll(234, t180, tpend, 3)
    dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    dglc.sp('%sv3】非店之A' % namess)

    ############ 旗舰店深浅A ##################
    dglc.cp()
    dglc.zdy('%s【辅】旗店深A行为' % namess)
    dglc.qll(234, t180, tpend, 1)
    dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    dglc.zdy('%s【辅】旗舰店A行为' % namess, 1)
    dglc.sp('%sv4】旗店深A' % namess)

    dglc.cp()
    dglc.zdy('%s【辅】旗店深A行为' % namess)
    dglc.qll(234, t180, tpend, 3)
    dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    dglc.zdy('%s【辅】旗舰店A行为' % namess, 1)
    dglc.sp('%sv5】旗店浅A' % namess)
    #-------【II】---------------★★★★★★★★★★#
    # dglc.cp()
    # dglc.qll(34, tIs, tpend)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    # dglc.sp('%sv6】全渠道I' % namess)

    # dglc.cp()
    # dglc.qll(34, tIs, tpend)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    # dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    # dglc.sp('%sv7】旗店之I' % namess)

    dglc.cp()
    dglc.zdy('%s【辅】旗舰店I行为' % namess)
    dglc.qll(34, tIs, tpend, 3)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.sp('%sv8】非店之I' % namess)

    # dglc.cp()
    # dglc.zdy('%s【辅】超级用户'%namess)
    # dglc.qll(34, tIs, tpend, 1)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    # dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    # dglc.sp('%sv9】超I-Total'%namess)

    dglc.cp()
    dglc.hy(2, tpend, tpend, 2)
    dglc.wt_gg(2, tpend, tpend, 3)

    dglc.qll(34, tIs, tpend, 1)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv9】粉丝I人群' % namess)

    dglc.cp()
    dglc.hy(2, tpend, tpend, 2)

    dglc.qll(34, tIs, tpend, 1)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv9】会员I人群' % namess)

    dglc.cp()
    dglc.dp(23, tIs, tpend)
    dglc.zdy('%s【辅】超级用户' % namess, 1)
    dglc.qll(34, tIs, tpend, 1)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv10】超I深I' % namess)

    dglc.cp()
    dglc.dp(23, tIs, tpend)
    dglc.zdy('%s【辅】超级用户' % namess, 3)
    dglc.qll(34, tIs, tpend, 1)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv11】超I浅I' % namess)

    # dglc.cp()
    # dglc.zdy('%s【辅】超级用户'%namess)
    # dglc.qll(34, tIs, tpend, 3)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    # dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    # dglc.sp('%sv12】非超I-Total'%namess)

    dglc.cp()
    dglc.dp(23, tIs, tpend)
    dglc.zdy('%s【辅】超级用户' % namess, 1)
    dglc.qll(34, tIs, tpend, 3)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv13】非超I深I' % namess)

    dglc.cp()
    dglc.dp(23, tIs, tpend)
    dglc.zdy('%s【辅】超级用户' % namess, 3)
    dglc.qll(34, tIs, tpend, 3)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    dglc.sp('%sv14】非超I浅I' % namess)

    #-------【PL】---------------★★★★★★★★★★#
    # dglc.cp()
    # dglc.qll(34, t180, tpend)
    # dglc.sp('%sv15】全部PL' % namess)

    # dglc.cp()
    # dglc.dp(5, tPLs, tpend)
    # dglc.qll(34, t180, tpend, 1)
    # dglc.sp('%sv16】旗舰店PL'%namess)

    if tPLs:
        pass
    else:
        tPLs = t365

    dglc.cp()
    dglc.zdy('%s【辅】活跃ZDY' % namess)
    dglc.dp(5, tPLs, tpend, 1)
    dglc.qll(34, t180, tpend, 1)
    dglc.sp('%sv17】旗店PL活跃' % namess)

    dglc.cp()
    dglc.zdy('%s【辅】活跃ZDY' % namess)
    dglc.dp(5, tPLs, tpend, 3)
    dglc.qll(34, t180, tpend, 1)
    dglc.sp('%sv18】旗店PL非活' % namess)

    # dglc.cp()
    # dglc.dp(5, tPLs, tpend)
    # dglc.qll(34, t180, tpend, 3)
    # dglc.sp('v19%s】非店PL'%namess)

    dglc.cp()
    dglc.zdy('%s【辅】活跃ZDY' % namess)
    dglc.dp(5, tPLs, tpend, 1)
    dglc.qll(34, t180, tpend, 3)
    dglc.sp('%sv20】非店PL活跃' % namess)

    dglc.cp()
    dglc.zdy('%s【辅】活跃ZDY' % namess)
    dglc.dp(5, tPLs, tpend, 3)
    dglc.qll(34, t180, tpend, 3)
    dglc.sp('%sv21】非店PL非活' % namess)


def diaoyong_jindian(t2bef, t2end):
    namess = namesstt(t2bef) + '-' + namesstt(t2end)

    if two_check_time(t2bef, t2end):
        dglc.cp()
        dglc.dp(12345, t2bef, t2end, 2)
        dglc.tm(1, t2bef, t2end, 2)
        dglc.tm(3, t2bef, t2end, 2)
        dglc.sp('%s【辅】进店ZDY' % namess)


def diaoyong_tracking(t2bef, t2end, tpend, with_people, Xmodel=3):

    dy_name = namesstt(tpend)  # tpend
    sc_name = namesstt(t2end)

    xname = 'xX' if Xmodel == 3 else '-'
    leixinname = ''

    def cp3():
        nonlocal leixinname
        dglc.cp()
        if with_people == 'gm':
            leixinname = '购买'
            dglc.dp(5, t2bef, t2end)
        elif with_people == 'jd':
            leixinname = '进店'
            dglc.zdy('%s%s%s【辅】进店ZDY' %
                     (namesstt(t2bef), '-', namesstt(t2end)))
        elif with_people == 'bg':
            leixinname = '曝光'
            dglc.zszw([1, 99], t2bef, t2end, action=1)
        elif with_people == 'sc':
            leixinname = '收藏'
            dglc.dp(2, t2bef, t2end)
        elif with_people == 'jg':
            leixinname = '加购'
            dglc.dp(3, t2bef, t2end)
        elif with_people == 'scjg':
            leixinname = '收加'
            dglc.dp(23, t2bef, t2end)
        elif with_people == 'ys':
            leixinname = '预售'
            dglc.dp(4, t2bef, t2end)
        elif with_people == 'ysgm':
            leixinname = '预售购买'
            dglc.dp(45, t2bef, t2end)
        else:
            leixinname = with_people[0]
            dglc.zdy(with_people[1])

    cp3()
    dglc.zdy('%sv3】非店之A' % dy_name, Xmodel)
    dglc.sp('%s-%s非店A%s%s' %
            (dy_name, sc_name, xname, leixinname))  # A

    cp3()
    dglc.zdy('%sv4】旗店深A' % dy_name, Xmodel)
    dglc.sp('%s-%s深度A%s%s' % (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv5】旗店浅A' % dy_name, Xmodel)
    dglc.sp('%s-%s浅度A%s%s' %
            (dy_name, sc_name, xname, leixinname))  # A

    cp3()
    dglc.zdy('%sv8】非店之I' % dy_name, Xmodel)
    dglc.sp('%s-%s非店I%s%s' %
            (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv9】粉丝I人群' % dy_name, Xmodel)
    dglc.sp('%s-%s粉丝I%s%s' %
            (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv10】会员I人群' % dy_name, Xmodel)
    dglc.sp('%s-%s会员I%s%s' %
            (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv11】超I浅I' % dy_name, Xmodel)
    dglc.zdy('%sv10】超I深I' % dy_name, 2)
    dglc.sp('%s-%s超级I%s%s' %
            (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv13】非超I深I' % dy_name, Xmodel)
    dglc.sp('%s-%s深度I%s%s' % (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv14】非超I浅I' % dy_name, Xmodel)
    dglc.sp('%s-%s浅度I%s%s' %
            (dy_name, sc_name, xname, leixinname))  # I

    cp3()
    dglc.zdy('%sv17】旗店PL活跃' % dy_name, Xmodel)
    dglc.sp('%s-%s旗店活跃PL%s%s' %
            (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv18】旗店PL非活' % dy_name, Xmodel)
    dglc.sp('%s-%s旗店非活PL%s%s' %
            (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv20】非店PL活跃' % dy_name, Xmodel)
    dglc.sp('%s-%s非店活跃PL%s%s' %
            (dy_name, sc_name, xname, leixinname))

    cp3()
    dglc.zdy('%sv21】非店PL非活' % dy_name, Xmodel)
    dglc.sp('%s-%s非店非活PL%s%s' %
            (dy_name, sc_name, xname, leixinname))  # PL
