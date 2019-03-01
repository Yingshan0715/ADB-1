from ..autoclass import AutoDatabank
from ..actionfunc import swtime, tnow, t180, t365
from random import randint

lc = AutoDatabank()
lc.yybp_order = 0
lc.ppld_order = 0


def quickrun():
    '''快速运行所有代表性的人群一次，不产生人群'''
    lc.cp()
    lc.qll(1234, t180, tnow, randint(1, 3))
    lc.ss('LCCCCCcccccCL'*20, t180, tnow, randint(1, 3))
    lc.zszw([1, 99], t365, tnow, randint(1, 3))
    lc.yhh(1, t180, tnow, randint(1, 3))
    lc.jhs(1, t180, tnow, randint(1, 3))
    lc.dp(23, t180, tnow, randint(1, 3))
    lc.dp(5, t365, tnow, randint(1, 3))
    lc.hy(2, tnow, tnow, randint(1, 3))
    lc.tm(1, t180, tnow, randint(1, 3))


def run_Total(withsp=False):
    '''运行所有逻辑的人群方法，action参数为随机参数
    start_date, end_date 为当前时间可选极限时间段，也是checktime函数的时间范围
    jbc参数为随机123,介入SP方法 不产生人群'''
    lc.cp()
    lc.qll(1234, t180, tnow, randint(1, 3))
    lc.qll(34, t180, tnow, randint(1, 3))
    if withsp:
        lc.sp('qll测试')

    lc.cp()
    sousuoci = ''.join(['lclclclclclclclc' + str(i) for i in range(20)])
    lc.ss('lc' + str(randint(100, 1000)), t180, tnow, randint(1, 3))
    lc.ss('lc' + str(randint(100, 1000)), t180, tnow, randint(1, 3))
    lc.ss(sousuoci, t180, tnow, 2)
    if withsp:
        lc.sp('ss测试')

    lc.cp()
    lc.ud([randint(1, 4), randint(5, 15)], t365,
          tnow, randint(1, 3), action=randint(1, 2))
    lc.ykgg([randint(1, 4), randint(5, 15)], t365,
            tnow, randint(1, 3), action=randint(1, 2))
    lc.yybp([randint(1, 4), randint(5, 15)], t365,
            tnow, randint(1, 3), action=randint(1, 2))
    lc.ppld([randint(1, 4), randint(5, 15)], t365,
            tnow, randint(1, 3), action=randint(1, 2))
    lc.ppzq([randint(1, 4), randint(5, 15)], t365,
            tnow, randint(1, 3), action=randint(1, 2))
    lc.mxdp([randint(1, 4), randint(5, 15)], t365,
            tnow, randint(1, 3), action=randint(1, 2))
    lc.zszw([randint(1, 4), randint(5, 15)], t365,
            tnow, randint(1, 3), action=randint(1, 2))
    lc.pphysgg([randint(1, 4), randint(5, 15)], t365,
               tnow, randint(1, 3), action=randint(1, 2))
    if withsp:
        lc.sp('ffgg测试')

    lc.cp()
    lc.pph(randint(1, 3), randint(1, 2), t180, tnow, randint(1, 3))
    lc.pph(randint(1, 3), randint(1, 2), t180, tnow, randint(1, 3))
    lc.pph(randint(1, 3), randint(1, 2), t180, tnow, randint(1, 3))
    if withsp:
        lc.sp('pph测试')

    lc.cp()
    lc.tbtt(randint(1, 7), t180, tnow, randint(1, 3))
    lc.yhh(randint(1, 3), t180, tnow, randint(1, 3))
    lc.bmqd(randint(1, 2), t180, tnow, randint(1, 3))
    lc.cnxh(1, t180, tnow, randint(1, 3))
    lc.shyjs(randint(1, 2), t180, tnow, randint(1, 3))
    lc.zb(1, t180, tnow, randint(1, 3))
    lc.wt(randint(1, 7), t180, tnow, randint(1, 3))
    if withsp:
        lc.sp('nrqd测试')

    lc.cp()
    lc.cjppr(randint(1, 4), t180, tnow, randint(1, 3))
    lc.hdb(1, randint(1, 2), t180, tnow, randint(1, 3))
    lc.thllb(randint(1, 3), randint(1, 2), t180, tnow, randint(1, 3))
    lc.jhs(randint(1, 2), t180, tnow, randint(1, 3))
    lc.syzx(randint(1, 2), t180, tnow, randint(1, 3))
    lc.tqg(randint(1, 2), t180, tnow, randint(1, 3))
    lc.hjr(randint(1, 2), t180, tnow, randint(1, 3))
    if withsp:
        lc.sp('tmyxpt测试')

    #lc.cp()
    #lc.tm(1, t180, tnow, randint(1, 3))
    #lc.tm(3, t180, tnow, randint(1, 3))
    #if withsp:
    #    lc.sp('tm测试')

    lc.cp()
    lc.dp(1, t180, tnow, randint(1, 3))
    lc.dp(12345, t180, tnow, randint(1, 3))
    lc.dp(5, t365, tnow, randint(1, 3))
    if withsp:
        lc.sp('dp测试')

    lc.cp()
    lc.qqdgm(1, t180, tnow, randint(1, 3))
    lc.qqdgm(12345, t180, tnow, randint(1, 3))
    lc.qqdgm(5, t365, tnow, randint(1, 3))
    if withsp:
        lc.sp('qqdgm圈人测试')

    lc.cp()
    lc.hy(randint(1, 2), t180, tnow, randint(1, 3))
    lc.hy(randint(1, 2), t180, tnow, randint(1, 3))
    lc.hy(randint(1, 2), t180, tnow, randint(1, 3))
    if withsp:
        lc.sp('hy测试')