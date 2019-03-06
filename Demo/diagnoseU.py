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
                   t2bef,
                   kwords, pph=True):

    a1 = tAs
    a2 = swtime(t2bef, False) - timedelta(1)
    i1 = tIs
    i2 = swtime(t2bef, False) - timedelta(1)
    h1 = tHs
    h2 = swtime(t2bef, False) - timedelta(1)

    namess = namesstt(a2)

    dglc.cp()
    dglc.super_ss(kwords, a1, a2, jbc='bb-BitCoin')
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


def depths_of_aipl(tAs, tIs, t2bef):
    tpend = swtime(t2bef, 0) - timedelta(1)
    namess = namesstt(tpend)

    #-------【AA】---------------★★★★★★★★★★#
    dglc.cp()
    dglc.qll(234, t180, tpend)
    dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    dglc.sp('%sv1】全渠道A' % namess)

    # dglc.cp()
    #dglc.qll(234, t180, tpend)
    # dglc.qll(1, tAs, tpend, 3)  # 连接A差IPL
    #dglc.zdy('%s【辅】旗舰店A行为' % namess, 1)
    #dglc.sp('%sv2】旗店之A' % namess)

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
    dglc.cp()
    dglc.qll(34, tIs, tpend)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.sp('%sv6】全渠道I' % namess)

    # dglc.cp()
    #dglc.qll(34, tIs, tpend)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    #dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    #dglc.sp('%sv7】旗店之I' % namess)

    dglc.cp()
    dglc.zdy('%s【辅】旗舰店I行为' % namess)
    dglc.qll(34, tIs, tpend, 3)
    dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    dglc.sp('%sv8】非店之I' % namess)

    # dglc.cp()
    # dglc.zdy('%s【辅】超级用户'%namess)
    #dglc.qll(34, tIs, tpend, 1)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    #dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
    # dglc.sp('%sv9】超I-Total'%namess)

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
    #dglc.qll(34, tIs, tpend, 3)
    # dglc.qll(2, tIs, tpend, 3)  # 连接I差PL
    #dglc.zdy('%s【辅】旗舰店I行为' % namess, 1)
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
    dglc.cp()
    dglc.qll(34, t180, tpend)
    dglc.sp('%sv15】全部PL' % namess)

    # dglc.cp()
    #dglc.dp(5, t365, tpend)
    #dglc.qll(34, t180, tpend, 1)
    # dglc.sp('%sv16】旗舰店PL'%namess)

    dglc.cp()
    dglc.zdy('%s【辅】活跃ZDY' % namess)
    dglc.dp(5, t365, tpend, 1)
    dglc.qll(34, t180, tpend, 1)
    dglc.sp('%sv17】旗店PL活跃' % namess)

    dglc.cp()
    dglc.zdy('%s【辅】活跃ZDY' % namess)
    dglc.dp(5, t365, tpend, 3)
    dglc.qll(34, t180, tpend, 1)
    dglc.sp('%sv18】旗店PL非活' % namess)

    # dglc.cp()
    #dglc.dp(5, t365, tpend)
    #dglc.qll(34, t180, tpend, 3)
    # dglc.sp('v19%s】非店PL'%namess)

    dglc.cp()
    dglc.zdy('%s【辅】活跃ZDY' % namess)
    dglc.dp(5, t365, tpend, 1)
    dglc.qll(34, t180, tpend, 3)
    dglc.sp('%sv20】非店PL活跃' % namess)

    dglc.cp()
    dglc.zdy('%s【辅】活跃ZDY' % namess)
    dglc.dp(5, t365, tpend, 3)
    dglc.qll(34, t180, tpend, 3)
    dglc.sp('%sv21】非店PL非活' % namess)

#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★#


def new_and_old(customertype, ts, te):
    '''
    场景：每日新老客分布  xModel
    customertype 可选 'new' ,'old'
    该函数可以指定 t2bef,t2end，用以实现任意时间段内的每日新老客
    new_and_old(customertype='new', t2bef, t2end)
    new_and_old(customertype='old', t2bef, t2end)
    '''
    assert customertype in ['new', 'old']
    t2bef, t2end = ts, te
    onedaybef = swtime(t2bef, False) - timedelta(1)

    jbc = 3 if customertype == 'new' else 1
    nameno = '新客' if customertype == 'new' else '老客'

    dglc.cp()
    dglc.dp(5, t365, onedaybef)  # 争议 qll 或者 dp
    # dglc.qll(34,onedaybef,onedaybef)
    dglc.dp(5, t2bef, t2end, jbc)
    dglc.sp('期间%s】' % nameno + 'Total')

    while swtime(ts, False) != (swtime(te, False) + timedelta(1)):
        dglc.cp()
        dglc.dp(5, t365, onedaybef)  # 争议 qll 或者 dp
        # dglc.qll(34,onedaybef,onedaybef)
        dglc.dp(5, ts, ts, jbc)
        dglc.dp(5, t2bef, t2end, 3)
        dglc.sp('期间%s】x' % nameno + swtime(ts)[-5:])
        ts = swtime(ts, False) + timedelta(1)


def zszw_new_and_old_convert(customertype, ts, te, t2bef, t2end, num=6, namess=''):
    '''场景：钻石展位转化 新老客 xModel
    customertype 可选 'new' ,'old', 'all'
    zszw_new_and_old_convert('all', ts, te, num=10)'''
    assert customertype in ['all', 'new', 'old']
    onedaybef = swtime(swtime(ts, False) - timedelta(1))

    if customertype == 'all':
        name = '全部'
        jbc = 1
    elif customertype == 'new':
        name = '新客'
        jbc = 3
    elif customertype == 'old':
        name = '老客'
        jbc = 1

    # 曝光人群计算
    dglc.cp()
    if customertype != 'all':
        dglc.dp(5, t365, onedaybef, 1)    # 新老客定义的争议 是 qll 还是 dp
        #dglc.qll(34, t365, onedaybef)
    dglc.zszw([1, 999], ts, te, jbc)
    dglc.sp(name + 'Total曝光' + namess)

    for i in range(1, num + 1):
        dglc.cp()
        if customertype != 'all':
            dglc.dp(5, t365, onedaybef, 1)    # 新老客定义的争议 是 qll 还是 dp
            #dglc.qll(34, t365, onedaybef)
        dglc.zszw([i, i], ts, te, jbc)
        dglc.zszw([1, 999], ts, te, 3)
        dglc.sp(name + '曝光x' + str(i) + namess)

    # 曝光人群计算其中转化人群
    dglc.cp()
    dglc.dp(5, t2bef, t2end)
    if customertype != 'all':
        dglc.dp(5, t365, onedaybef, 1)    # 新老客定义的争议 是 qll 还是 dp
        #dglc.qll(34, t365, onedaybef)
    dglc.zszw([1, 999], ts, te, jbc)
    dglc.sp(name + 'Total曝光【购' + namess)

    for i in range(1, num + 1):
        dglc.cp()
        dglc.dp(5, t2bef, t2end)
        if customertype != 'all':
            dglc.dp(5, t365, onedaybef, 1)    # 新老客定义的争议 是 qll 还是 dp
            #dglc.qll(34, t365, onedaybef)
        dglc.zszw([i, i], ts, te, jbc)
        dglc.zszw([1, 999], ts, te, 3)
        dglc.sp(name + '曝光x' + str(i) + '【购' + namess)
