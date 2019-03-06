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
dglc.brand_name = '科罗娜'


def set_dglc(izhang_hao, tmall_global, p_type, yybp, ppld, ppzq, mxdp, zszw, brand_name):
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

tnow = swtime('2019-2-28',False)

namess = '%02d%02d' % (tnow.month, tnow.day)
t30 = somedays(swtime(tnow + timedelta(1)), 30)
t60 = somedays(swtime(tnow + timedelta(1)), 60)
t90 = somedays(swtime(tnow + timedelta(1)), 90)


def set_tnow(some_date):
    global tnow, namess, t30, t60, t90
    tnow = swtime(some_date, False)
    namess = '%02d%02d' % (tnow.month, tnow.day)
    t30 = somedays(swtime(tnow + timedelta(1)), 30)
    t60 = somedays(swtime(tnow + timedelta(1)), 60)
    t90 = somedays(swtime(tnow + timedelta(1)), 90)


def xinke_run(ty):

    def cp2():
        dglc.cp()
        if ty == 1:
            dglc.pjpc(1, 3)  # 啤酒频次
        elif ty == 2:
            dglc.xfxw(4, 56789, 3)  # 消费行为 天猫
            dglc.pjpc(23456, 1)
        elif ty == 3:
            dglc.xfxw(4, 56789, 3)
            dglc.pjpc(23456, 3)

    def sp2(x):
        if ty == 1:
            dglc.sp(x + '-0')
        elif ty == 2:
            dglc.sp(x + '-3')
        elif ty == 3:
            dglc.sp(x + '-X3')

    cp2()  # CPPPPPPPPPP
    dglc.dp(5, t365, tnow, 1)
    dglc.pph(2, 2, tnow, tnow, 3)
    dglc.hy(2, tnow, tnow, 2)
    dglc.klnll(5, [2, 999], t90, tnow, 2)
    dglc.dp(23, t90, tnow, 2)
    dglc.tm(3, t90, tnow, 2)
    dglc.ss('科罗娜', t90, tnow, 2)
    sp2('%s旗舰店重I90天' % namess)

    cp2()  # CPPPPPPPPPP
    dglc.dp(5, t365, tnow, 1)
    dglc.pph(2, 2, tnow, tnow, 3)
    dglc.hy(2, tnow, tnow, 3)
    dglc.tm(3, t90, tnow, 3)
    dglc.ss('科罗娜', t90, tnow, 3)

    dglc.klnll(5, [2, 999], t90, tnow, 3)
    dglc.dp(23, t90, tnow, 3)

    dglc.klnll(4, [2, 999], t90, tnow, 3)
    dglc.dptmcs(23, t90, tnow, 2)
    sp2('%s猫超重I90天' % namess)

    cp2()  # CPPPPPPPPPP
    dglc.dp(5, t365, tnow, 1)
    dglc.pph(2, 2, tnow, tnow, 3)
    dglc.hy(2, tnow, tnow, 3)
    dglc.tm(3, t90, tnow, 3)
    dglc.ss('科罗娜', t90, tnow, 3)

    dglc.klnll(4, [2, 999], t90, tnow, 3)
    dglc.dptmcs(23, t90, tnow, 3)

    dglc.klnll(5, [2, 999], t90, tnow, 3)
    dglc.dp(23, t90, tnow, 3)

    dglc.klnll(1, [2, 999], t90, tnow, 3)
    dglc.dpall(23, t90, tnow, 2)
    sp2('%s其他重I90天' % namess)

    cp2()  # CPPPPPPPPPP
    dglc.dp(5, t365, tnow, 1)
    dglc.pph(2, 2, tnow, tnow, 3)
    dglc.hy(2, tnow, tnow, 3)
    dglc.ss('科罗娜', t90, tnow, 3)
    dglc.klnll(1, [2, 999], t90, tnow, 3)
    dglc.dpall(23, t90, tnow, 2)
    dglc.tm(3, t90, tnow, 3)

    dglc.qll(2, t90, tnow, 3)

    sp2('%s轻度兴趣90天' % namess)

    cp2()  # CPPPPPPPPPP
    dglc.dp(5, t365, tnow, 1)
    dglc.qll(1, t180, tnow, 3)
    dglc.qll(2, t90, tnow, 3)
    dglc.qll(2, t180, tnow, 3)
    sp2('%s历史沉淀I人群' % namess)

    cp2()  # CPPPPPPPPPP
    dglc.dp(5, t365, tnow, 1)
    dglc.qll(2, t90, tnow, 3)
    dglc.qll(1, t90, tnow, 3)
    sp2('%s认知人群90天' % namess)

    cp2()  # CPPPPPPPPPP
    dglc.dp(5, t365, tnow, 1)
    dglc.qll(2, t180, tnow, 3)
    dglc.qll(1, t90, tnow, 3)
    dglc.qll(1, t180, tnow, 3)
    sp2('%s历史沉淀A人群' % namess)


def laoke_run_maochao():

    for x in ['0-30', '30-60', '60-90', '90-365']:
        tse = x.split('-')[0]
        if tse == '0':
            ts, te = None, t30
        elif tse == '30':
            ts, te = t30, t60
        elif tse == '60':
            ts, te = t60, t90
        elif tse == '90':
            ts, te = t90, t365

        for y in ['0-50', '50-200', '200-9999']:
            vmin, vmax = y.split('-')

            dglc.cp()
            dglc.qll(2, tnow, tnow)
            dglc.dp(5, t365, tnow, 2)
            dglc.klngm(4, [vmin, vmax], t365, tnow, 3)
            if ts:
                dglc.dpall(5, ts, tnow, 1)
                dglc.dpall(5, te, tnow, 3)
            else:
                dglc.dpall(5, te, tnow, 1)
            dglc.sp('%s-%s-%s-%s' %
                    (namess, x.split('-')[1], y.split('-')[1], '猫超'))  # change behind


def laoke_run_qijiandian():

    for x in ['0-30', '30-60', '60-90', '90-365']:
        tse = x.split('-')[0]
        if tse == '0':
            ts, te = None, t30
        elif tse == '30':
            ts, te = t30, t60
        elif tse == '60':
            ts, te = t60, t90
        elif tse == '90':
            ts, te = t90, t365

        for y in ['0-200', '200-350', '350-9999']:
            vmin, vmax = y.split('-')

            dglc.cp()
            dglc.qll(2, tnow, tnow)
            dglc.klngm(5, [vmin, vmax], t365, tnow, 2)
            if ts:
                dglc.dpall(5, ts, tnow, 1)
                dglc.dpall(5, te, tnow, 3)
            else:
                dglc.dpall(5, te, tnow, 1)
            dglc.sp('%s-%s-%s-%s' %
                    (namess, x.split('-')[1], y.split('-')[1], '旗舰'))

xinkelist = ['旗舰店重I90天', '猫超重I90天', '其他重I90天',
             '轻度兴趣90天', '历史沉淀I人群', '认知人群90天', '历史沉淀A人群']
xinkelabel = ['-0', '-3', '-X3']


maochaolist_x = ['0-30', '30-60', '60-90', '90-365']
maochaolist_y = ['0-50', '50-200', '200-9999']

qijiandianlist_x = maochaolist_x
qijiandianlist_y = ['0-200', '200-350', '350-9999']


def date_namess(adate):
    adate = swtime(adate, False)
    return '%02d%02d' % (adate.month, adate.day)


def xinke_xiangshang(t_small, t_large):
    assert swtime(t_small, False) < swtime(t_large, False)
    list1 = [date_namess(t_small) + x +
             y for x in xinkelist for y in xinkelabel]

    list2 = [date_namess(t_large) + x +
             y for x in xinkelist for y in xinkelabel]

    for x_xy, x in enumerate(list1):
        if x_xy > 2:
            dglc.cp()
            dglc.dp(5, '2018-11-11', '2018-11-11')  # 辅助包人群
            dglc.zdy(x, 2)  # 并集辅助包
            for y_xy, y in enumerate(list2):
                if y_xy <= x_xy // 3 * 3 - 1:
                    jbc = 1 if y_xy == 0 else 2
                    dglc.zdy(y, jbc)
            dglc.sp(x.split('-')[0][:-1] + '-' + x.split('-')[1] + '-【上')

        else:
            pass


def laoke_maochao_xiangshang(t_small, t_large):
    assert swtime(t_small, False) < swtime(t_large, False)
    list1 = ['%s-%s-%s-%s' %
             (date_namess(t_small), x.split('-')[1], y.split('-')[1], '猫超') for x in maochaolist_x for y in maochaolist_y]

    list2 = ['%s-%s-%s-%s' %
             (date_namess(t_large), x.split('-')[1], y.split('-')[1], '猫超') for x in maochaolist_x for y in maochaolist_y]

    for x_xy, x in enumerate(list1):
        if x_xy > 2:
            dglc.cp()
            dglc.qll(2, t_small, t_small, 1)  # 辅助包人群
            dglc.qll(2, t_small, t_small, 2)  # 并集辅助包
            dglc.zdy(x, 3)
            dglc.qll(2, t_large, t_large, 1)
            for y_xy, y in enumerate(list2):
                if y_xy <= x_xy // 3 * 3 - 1:
                    jbc = 3 if y_xy == 0 else 2
                    dglc.zdy(y, jbc)
            dglc.sp('%s-%s-%s-%s-%s' % (x.split('-')[0], x.split('-')[1],
                                        x.split('-')[2], x.split('-')[3][:-1], '【上'))

        else:
            pass


def laoke_qijiandian_xiangshang(t_small, t_large):
    assert swtime(t_small, False) < swtime(t_large, False)
    list1 = ['%s-%s-%s-%s' %
             (date_namess(t_small), x.split('-')[1], y.split('-')[1], '旗舰') for x in qijiandianlist_x for y in qijiandianlist_y]

    list2 = ['%s-%s-%s-%s' %
             (date_namess(t_large), x.split('-')[1], y.split('-')[1], '旗舰') for x in qijiandianlist_x for y in qijiandianlist_y]

    for x_xy, x in enumerate(list1):
        if x_xy > 2:
            dglc.cp()
            dglc.qll(2, t_small, t_small, 1)  # 辅助包人群
            dglc.qll(2, t_small, t_small, 2)  # 并集辅助包
            dglc.zdy(x, 3)
            dglc.qll(2, t_large, t_large, 1)
            for y_xy, y in enumerate(list2):
                if y_xy <= x_xy // 3 * 3 - 1:
                    jbc = 3 if y_xy == 0 else 2
                    dglc.zdy(y, jbc)
            dglc.sp('%s-%s-%s-%s-%s' % (x.split('-')[0], x.split('-')[1],
                                        x.split('-')[2], x.split('-')[3][:-1], '【上'))
        else:
            pass
