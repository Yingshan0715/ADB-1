from ..autoclass import AutoDatabank
from ..actionfunc import timedelta, parse, somedays
from ..actionfunc import swtime, checktime, two_check_time
from ..actionfunc import t365, t180, tnow
from .. import autoclass
import json

modulepath = autoclass.__file__[:-12] + 'setini/' + 'eightxx'

dglc = AutoDatabank(zhanghao=2, tmall_global=False, purchase_Behaviour='dp')
dglc.yybp_order = 0
dglc.ppld_order = 0


def reloaddglc():
    global dglc
    with open(modulepath, 'r') as f:
        izh, tg, pb, o1, o2, o3, o4, o5 = json.load(f)['valuex']
    dglc = autoclass.AutoDatabank(izh, tg, pb)
    dglc.yybp_order = o1
    dglc.ppld_order = o2
    dglc.ppzq_order = o3
    dglc.mxdp_order = o4
    dglc.zszw_order = o5
    print('重载成功...')
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#


def diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, zhuanhuarenqun, Xmodel=3):
    reloaddglc()
    xname = 'xX' if Xmodel == 3 else ''
    leixinname = ''

    def cp3():
        nonlocal leixinname
        dglc.cp()
        if zhuanhuarenqun == 'jindian':
            leixinname = '进店'
            dglc.zdy('%s【辅】进店ZDY' % shengchengname)
        elif zhuanhuarenqun == 'shoucang':
            leixinname = '收藏'
            dglc.dp(2, t2bef, t2end)
        elif zhuanhuarenqun == 'jiagou':
            leixinname = '加购'
            dglc.dp(3, t2bef, t2end)
        elif zhuanhuarenqun == 'yushou':
            leixinname = '预售'
            dglc.dp(4, t2bef, t2end)
        elif zhuanhuarenqun == 'baoguang':
            leixinname = '曝光'
            dglc.zszw([1, 99], t2bef, t2end, action=1)

    cp3()
    dglc.zdy('%sv3】非店之A' % diaoyongname, Xmodel)
    dglc.sp('%s-%s非店A%s%s' % (diaoyongname, shengchengname, xname, leixinname))

    cp3()
    dglc.zdy('%sv4】旗店深A' % diaoyongname, Xmodel)
    dglc.sp('%s-%s深度A%s%s' % (diaoyongname, shengchengname, xname, leixinname))

    cp3()
    dglc.zdy('%sv5】旗店浅A' % diaoyongname, Xmodel)
    dglc.sp('%s-%s浅度A%s%s' %
            (diaoyongname, shengchengname, xname, leixinname))  # A

    cp3()
    dglc.zdy('%sv11】超I浅I' % diaoyongname, Xmodel)
    dglc.zdy('%sv10】超I深I' % diaoyongname, 2)
    dglc.sp('%s-%s超级I%s%s' %
            (diaoyongname, shengchengname, xname, leixinname))

    cp3()
    dglc.zdy('%sv12】非超I深I' % diaoyongname, Xmodel)
    dglc.sp('%s-%s深度I%s%s' % (diaoyongname, shengchengname, xname, leixinname))

    cp3()
    dglc.zdy('%sv13】非超I浅I' % diaoyongname, Xmodel)
    dglc.sp('%s-%s浅度I%s%s' % (diaoyongname, shengchengname, xname, leixinname))

    cp3()
    dglc.zdy('%sv8】非店之I' % diaoyongname, Xmodel)
    dglc.sp('%s-%s非店I%s%s' %
            (diaoyongname, shengchengname, xname, leixinname))  # I

    cp3()
    dglc.zdy('%sv17】旗店PL活跃' % diaoyongname, Xmodel)
    dglc.sp('%s-%s旗店活跃PL%s%s' %
            (diaoyongname, shengchengname, xname, leixinname))

    cp3()
    dglc.zdy('%sv18】旗店PL非活' % diaoyongname, Xmodel)
    dglc.sp('%s-%s旗店非活PL%s%s' %
            (diaoyongname, shengchengname, xname, leixinname))

    cp3()
    dglc.zdy('%sv20】非店PL活跃' % diaoyongname, Xmodel)
    dglc.sp('%s-%s非店活跃PL%s%s' %
            (diaoyongname, shengchengname, xname, leixinname))

    cp3()
    dglc.zdy('%sv21】非店PL非活' % diaoyongname, Xmodel)
    dglc.sp('%s-%s非店非活PL%s%s' %
            (diaoyongname, shengchengname, xname, leixinname))  # PL
