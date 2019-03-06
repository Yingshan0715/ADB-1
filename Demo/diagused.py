from ..autoclass import AutoDatabank
from ..actionfunc import timedelta, parse, somedays, namesstt
from ..actionfunc import swtime, checktime, two_check_time
from ..actionfunc import t365, t180, tnow
from .. import adbpath
import json

modulepath = adbpath.__file__[:-10] + 'setini/' + 'eightxx'

dglc = AutoDatabank(zhanghao=2, tmall_global=False, purchase_Behaviour='dp')
dglc.yybp_order = 0
dglc.ppld_order = 0


def reloaddglc():
    global dglc
    with open(modulepath, 'r') as f:
        izh, tg, pb, o1, o2, o3, o4, o5, bn = json.load(f)['valuex']
    dglc = AutoDatabank(izh, tg, pb)
    dglc.yybp_order = o1
    dglc.ppld_order = o2
    dglc.ppzq_order = o3
    dglc.mxdp_order = o4
    dglc.zszw_order = o5
    dglc.brand_name = bn
    print('重载成功...')
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#


def diaoyong_jindian(t2bef, t2end):
    reloaddglc()
    namess = namesstt(t2bef) + '-' + namesstt(t2end)
    
    if two_check_time(t2bef, t2end):
        dglc.cp()
        dglc.dp(12345, t2bef, t2end, 2)
        dglc.tm(1, t2bef, t2end, 2)
        dglc.tm(3, t2bef, t2end, 2)
        dglc.sp('%s【辅】进店ZDY' % namess)


def diaoyong_tracking(t2bef, t2end, with_people, Xmodel=3):
    reloaddglc()
    tpend = swtime(t2bef, False) - timedelta(1)
    dy_name = namesstt(tpend)
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
            dglc.dp(4, 1020, t2end)
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
