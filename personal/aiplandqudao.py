from ..autoclass import AutoDatabank
from ..actionfunc import timedelta, parse, somedays, swtime, t180
from .. import adbpath
import json

modulepath = adbpath.__file__[:-10] + 'setini/' + 'eightxx'
dglc = AutoDatabank(zhanghao=2, tmall_global=False, purchase_Behaviour='dp')


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


tAs = swtime('2018-12-10', False)
tIs = swtime('2018-9-10', False)
tPLs = t180


def xinzeng_aipl(ts, te, namess):
    tpend = swtime(ts, False) - timedelta(1)
    dglc.cp()
    dglc.qll(1234, tAs, tpend)
    dglc.qll(234, ts, te, 3)
    dglc.qll(1, ts, te, 3)
    dglc.sp('%s新增A人群' % namess)

    dglc.cp()
    dglc.qll(1234, tIs, tpend)
    dglc.qll(34, ts, te, 3)
    dglc.qll(2, ts, te, 3)
    dglc.sp('%s新增I人群' % namess)

    dglc.cp()
    dglc.qll(1234, t180, tpend, 3)
    dglc.qll(34, ts, te, 3)
    dglc.sp('%s新增PL人群' % namess)


def yuanyou_aipl(ts, te, namess):
    tpend = swtime(ts, False) - timedelta(1)
    dglc.cp()
    dglc.qll(1234, tAs, tpend)
    dglc.qll(234, ts, te, 1)
    dglc.qll(1, ts, te, 3)
    dglc.sp('%s原有A人群' % namess)

    dglc.cp()
    dglc.qll(1234, tIs, tpend)
    dglc.qll(34, ts, te, 1)
    dglc.qll(2, ts, te, 3)
    dglc.sp('%s原有I人群' % namess)

    dglc.cp()
    dglc.qll(1234, t180, tpend, 3)
    dglc.qll(34, ts, te, 1)
    dglc.sp('%s原有PL人群' % namess)


def qudaofenbu_aipl(ts, te, aipl_name, nametyple, namess):
    aipl_name2 = aipl_name[:-2]

    dglc.cp()
    dglc.ud([1, 99], ts, te, 3, action=1)
    dglc.ud([1, 99], ts, te, 3, action=2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-UD' % (namess, aipl_name2))

    dglc.cp()
    dglc.ykgg([1, 99], ts, te, 3, action=1)
    dglc.ykgg([1, 99], ts, te, 3, action=2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-优酷广告' % (namess, aipl_name2))

    dglc.cp()
    dglc.jhs(2, ts, te, 3)
    dglc.jhs(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-聚划算' % (namess, aipl_name2))

    dglc.cp()
    dglc.tqg(2, ts, te, 3)
    dglc.tqg(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-淘抢购' % (namess, aipl_name2))

    dglc.cp()
    dglc.syzx(2, ts, te, 3)
    dglc.syzx(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-试用中心' % (namess, aipl_name2))

    dglc.cp()
    dglc.tmux(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-天猫U先' % (namess, aipl_name2))

    dglc.cp()
    dglc.cjppr(1, ts, te, 3)
    dglc.cjppr(2, ts, te, 3)
    dglc.cjppr(3, ts, te, 3)
    dglc.cjppr(4, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-超级品牌日' % (namess, aipl_name2))

    dglc.cp()
    dglc.hjr(1, ts, te, 3)
    dglc.hjr(2, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-欢聚日' % (namess, aipl_name2))

    dglc.cp()
    dglc.hdb(2, 1, ts, te, 3)
    dglc.hdb(1, 1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-互动吧' % (namess, aipl_name2))

    dglc.cp()
    dglc.thllb(3, 2, ts, te, 3)
    dglc.thllb(3, 1, ts, te, 3)
    dglc.thllb(2, 2, ts, te, 3)
    dglc.thllb(2, 1, ts, te, 3)
    dglc.thllb(1, 1, ts, te, 3)
    dglc.thllb(1, 2, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-天合流量宝' % (namess, aipl_name2))

    dglc.cp()
    dglc.pph(1, 1, ts, te, 3)
    dglc.pph(2, 1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-品牌号' % (namess, aipl_name2))

    dglc.cp()
    dglc.tbtt(1, ts, te, 3)
    dglc.tbtt(2, ts, te, 3)
    dglc.tbtt(3, ts, te, 3)
    dglc.tbtt(4, ts, te, 3)
    dglc.tbtt(5, ts, te, 3)
    dglc.tbtt(6, ts, te, 3)
    dglc.tbtt(7, ts, te, 3)
    dglc.tbtt_v(1, ts, te, 3)
    dglc.tbtt_v(2, ts, te, 3)
    dglc.tbtt_v(3, ts, te, 3)
    dglc.tbtt_v(4, ts, te, 3)
    dglc.tbtt_v(5, ts, te, 3)
    dglc.tbtt_v(6, ts, te, 3)
    dglc.tbtt_v(7, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-淘宝头条' % (namess, aipl_name2))

    dglc.cp()
    dglc.yhh(1, ts, te, 3)
    dglc.yhh(2, ts, te, 3)
    dglc.yhh(3, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-有好货' % (namess, aipl_name2))

    dglc.cp()
    dglc.bmqd(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-必买清单' % (namess, aipl_name2))

    dglc.cp()
    dglc.cnxh(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-猜你喜欢' % (namess, aipl_name2))

    dglc.cp()
    dglc.zb(1, ts, te, 3)
    dglc.zb(2, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-直播' % (namess, aipl_name2))

    dglc.cp()
    dglc.wt_gg(2, ts, te, 3)
    dglc.wt(1, ts, te, 3)
    dglc.wt(2, ts, te, 3)
    dglc.wt(3, ts, te, 3)
    dglc.wt(4, ts, te, 3)
    dglc.wt(5, ts, te, 3)
    dglc.wt(6, ts, te, 3)
    dglc.wt(7, ts, te, 3)
    dglc.wt_v(1, ts, te, 3)
    dglc.wt_v(2, ts, te, 3)
    dglc.wt_v(3, ts, te, 3)
    dglc.wt_v(4, ts, te, 3)
    dglc.wt_v(5, ts, te, 3)
    dglc.wt_v(6, ts, te, 3)
    dglc.wt_v(7, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-微淘' % (namess, aipl_name2))

    dglc.cp()
    dglc.mrhd(1, ts, te, 3)
    dglc.mrhd(2, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-每日好店' % (namess, aipl_name2))

    dglc.cp()
    dglc.yybp([1, 99], ts, te, 3, action=1)
    dglc.yybp([1, 99], ts, te, 3, action=2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-一夜霸屏' % (namess, aipl_name2))

    dglc.cp()
    dglc.ppld([1, 99], ts, te, 3, action=1)
    dglc.ppld([1, 99], ts, te, 3, action=2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-品牌雷达' % (namess, aipl_name2))

    dglc.cp()
    dglc.ppzq([1, 99], ts, te, 3, action=1)
    dglc.ppzq([1, 99], ts, te, 3, action=2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-品牌专区' % (namess, aipl_name2))

    dglc.cp()
    dglc.mxdp([1, 99], ts, te, 3, action=1)
    dglc.mxdp([1, 99], ts, te, 3, action=2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-明星店铺' % (namess, aipl_name2))

    dglc.cp()
    dglc.zszw([1, 99], ts, te, 3, action=1)
    dglc.zszw([1, 99], ts, te, 3, action=2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-钻石展位' % (namess, aipl_name2))

    dglc.cp()
    dglc.pptx([1, 99], ts, te, 3, action=1)
    dglc.pptx([1, 99], ts, te, 3, action=2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-品牌特秀' % (namess, aipl_name2))

    dglc.cp()
    dglc.yyy([1, 99], ts, te, 3, action=1)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-摇一摇' % (namess, aipl_name2))

    dglc.cp()
    dglc.cnyz(3, ts, te, 3)
    dglc.cnyz(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-菜鸟驿站' % (namess, aipl_name2))

    dglc.cp()
    dglc.xianxiaUxian(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-线下U先' % (namess, aipl_name2))

    dglc.cp()
    dglc.zhsq(2, ts, te, 3)
    dglc.zhsq(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-智慧商圈' % (namess, aipl_name2))

    dglc.cp()
    if nametyple == 34:
        dglc.dptmgj(45, ts, te, 3)
    else:
        dglc.dptmgj(123, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-天猫国际' % (namess, aipl_name2))

    dglc.cp()
    if nametyple == 34:
        dglc.dptmgjzy(45, ts, te, 3)
    else:
        dglc.dptmgjzy(123, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-国际直营' % (namess, aipl_name2))

    dglc.cp()
    if nametyple == 34:
        dglc.dptmcs(45, ts, te, 3)
    else:
        dglc.dptmcs(123, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-天猫超市' % (namess, aipl_name2))

    dglc.cp()
    if nametyple == 34:
        dglc.dp(45, ts, te, 3)
    else:
        dglc.dp(123, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-天猫旗舰店' % (namess, aipl_name2))

    dglc.cp()
    if nametyple == 34:
        dglc.dpall(45, ts, te, 3)
    else:
        dglc.dpall(123, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-天猫全部' % (namess, aipl_name2))

    dglc.cp()
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    if nametyple == 34:
        dglc.dp(45, ts, te, 1)
        dglc.dpall(45, ts, te, 3)
    else:
        dglc.dp(123, ts, te, 1)
        dglc.dpall(123, ts, te, 3)
    dglc.sp('%s%s-交际-天猫其他' % (namess, aipl_name2))

    dglc.cp()
    if nametyple == 34:
        dglc.dpqqg(45, ts, te, 3)
    else:
        dglc.dpqqg(123, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-全球购' % (namess, aipl_name2))

    dglc.cp()
    if nametyple == 34:
        dglc.dptbjs(45, ts, te, 3)
    else:
        dglc.dptbjs(123, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-淘宝集市' % (namess, aipl_name2))

    dglc.cp()
    dglc.hy(1, ts, te, 3)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s%s-xX-新增会员' % (namess, aipl_name2))


def qudaofenbu_huizong(ts, te, namess):

    dglc.cp()
    dglc.ud([1, 99], ts, te, 2, action=1)
    dglc.ud([1, 99], ts, te, 2, action=2)
    dglc.sp('%s-汇总-UD' % (namess))

    dglc.cp()
    dglc.ykgg([1, 99], ts, te, 2, action=1)
    dglc.ykgg([1, 99], ts, te, 2, action=2)
    dglc.sp('%s-汇总-优酷广告' % (namess))

    dglc.cp()
    dglc.jhs(2, ts, te, 2)
    dglc.jhs(1, ts, te, 2)
    dglc.sp('%s-汇总-聚划算' % (namess))

    dglc.cp()
    dglc.tqg(2, ts, te, 2)
    dglc.tqg(1, ts, te, 2)
    dglc.sp('%s-汇总-淘抢购' % (namess))

    dglc.cp()
    dglc.syzx(2, ts, te, 2)
    dglc.syzx(1, ts, te, 2)
    dglc.sp('%s-汇总-试用中心' % (namess))

    dglc.cp()
    dglc.tmux(1, ts, te, 2)
    dglc.sp('%s-汇总-天猫U先' % (namess))

    dglc.cp()
    dglc.cjppr(1, ts, te, 2)
    dglc.cjppr(2, ts, te, 2)
    dglc.cjppr(3, ts, te, 2)
    dglc.cjppr(4, ts, te, 2)
    dglc.sp('%s-汇总-超级品牌日' % (namess))

    dglc.cp()
    dglc.hjr(1, ts, te, 2)
    dglc.hjr(2, ts, te, 2)
    dglc.sp('%s-汇总-欢聚日' % (namess))

    dglc.cp()
    dglc.hdb(2, 1, ts, te, 2)
    dglc.hdb(1, 1, ts, te, 2)
    dglc.sp('%s-汇总-互动吧' % (namess))

    dglc.cp()
    dglc.thllb(3, 2, ts, te, 2)
    dglc.thllb(3, 1, ts, te, 2)
    dglc.thllb(2, 2, ts, te, 2)
    dglc.thllb(2, 1, ts, te, 2)
    dglc.thllb(1, 1, ts, te, 2)
    dglc.thllb(1, 2, ts, te, 2)
    dglc.sp('%s-汇总-天合流量宝' % (namess))

    dglc.cp()
    dglc.pph(1, 1, ts, te, 2)
    dglc.pph(2, 1, ts, te, 2)
    dglc.sp('%s-汇总-品牌号' % (namess))

    dglc.cp()
    dglc.tbtt(1, ts, te, 2)
    dglc.tbtt(2, ts, te, 2)
    dglc.tbtt(3, ts, te, 2)
    dglc.tbtt(4, ts, te, 2)
    dglc.tbtt(5, ts, te, 2)
    dglc.tbtt(6, ts, te, 2)
    dglc.tbtt(7, ts, te, 2)
    dglc.tbtt_v(1, ts, te, 2)
    dglc.tbtt_v(2, ts, te, 2)
    dglc.tbtt_v(3, ts, te, 2)
    dglc.tbtt_v(4, ts, te, 2)
    dglc.tbtt_v(5, ts, te, 2)
    dglc.tbtt_v(6, ts, te, 2)
    dglc.tbtt_v(7, ts, te, 2)
    dglc.sp('%s-汇总-淘宝头条' % (namess))

    dglc.cp()
    dglc.yhh(1, ts, te, 2)
    dglc.yhh(2, ts, te, 2)
    dglc.yhh(3, ts, te, 2)
    dglc.sp('%s-汇总-有好货' % (namess))

    dglc.cp()
    dglc.bmqd(1, ts, te, 2)
    dglc.sp('%s-汇总-必买清单' % (namess))

    dglc.cp()
    dglc.cnxh(1, ts, te, 2)
    dglc.sp('%s-汇总-猜你喜欢' % (namess))

    dglc.cp()
    dglc.zb(1, ts, te, 2)
    dglc.zb(2, ts, te, 2)
    dglc.sp('%s-汇总-直播' % (namess))

    dglc.cp()
    dglc.wt_gg(2, ts, te, 2)
    dglc.wt(1, ts, te, 2)
    dglc.wt(2, ts, te, 2)
    dglc.wt(3, ts, te, 2)
    dglc.wt(4, ts, te, 2)
    dglc.wt(5, ts, te, 2)
    dglc.wt(6, ts, te, 2)
    dglc.wt(7, ts, te, 2)
    dglc.wt_v(1, ts, te, 2)
    dglc.wt_v(2, ts, te, 2)
    dglc.wt_v(3, ts, te, 2)
    dglc.wt_v(4, ts, te, 2)
    dglc.wt_v(5, ts, te, 2)
    dglc.wt_v(6, ts, te, 2)
    dglc.wt_v(7, ts, te, 2)
    dglc.sp('%s-汇总-微淘' % (namess))

    dglc.cp()
    dglc.mrhd(1, ts, te, 2)
    dglc.mrhd(2, ts, te, 2)
    dglc.sp('%s-汇总-每日好店' % (namess))

    dglc.cp()
    dglc.yybp([1, 99], ts, te, 2, action=1)
    dglc.yybp([1, 99], ts, te, 2, action=2)
    dglc.sp('%s-汇总-一夜霸屏' % (namess))

    dglc.cp()
    dglc.ppld([1, 99], ts, te, 2, action=1)
    dglc.ppld([1, 99], ts, te, 2, action=2)
    dglc.sp('%s-汇总-品牌雷达' % (namess))

    dglc.cp()
    dglc.ppzq([1, 99], ts, te, 2, action=1)
    dglc.ppzq([1, 99], ts, te, 2, action=2)
    dglc.sp('%s-汇总-品牌专区' % (namess))

    dglc.cp()
    dglc.mxdp([1, 99], ts, te, 2, action=1)
    dglc.mxdp([1, 99], ts, te, 2, action=2)
    dglc.sp('%s-汇总-明星店铺' % (namess))

    dglc.cp()
    dglc.zszw([1, 99], ts, te, 2, action=1)
    dglc.zszw([1, 99], ts, te, 2, action=2)
    dglc.sp('%s-汇总-钻石展位' % (namess))

    dglc.cp()
    dglc.pptx([1, 99], ts, te, 2, action=1)
    dglc.pptx([1, 99], ts, te, 2, action=2)
    dglc.sp('%s-汇总-品牌特秀' % (namess))

    dglc.cp()
    dglc.yyy([1, 99], ts, te, 2, action=1)
    dglc.sp('%s-汇总-摇一摇' % (namess))

    dglc.cp()
    dglc.cnyz(3, ts, te, 2)
    dglc.cnyz(1, ts, te, 2)
    dglc.sp('%s-汇总-菜鸟驿站' % (namess))

    dglc.cp()
    dglc.xianxiaUxian(1, ts, te, 2)
    dglc.sp('%s-汇总-线下U先' % (namess))

    dglc.cp()
    dglc.zhsq(2, ts, te, 2)
    dglc.zhsq(1, ts, te, 2)
    dglc.sp('%s-汇总-智慧商圈' % (namess))

    dglc.cp()
    if nametyple == 34:
        dglc.dptmgj(45, ts, te, 2)
    else:
        dglc.dptmgj(123, ts, te, 2)
    dglc.sp('%s-汇总-天猫国际' % (namess))

    dglc.cp()
    if nametyple == 34:
        dglc.dptmgjzy(45, ts, te, 2)
    else:
        dglc.dptmgjzy(123, ts, te, 2)
    dglc.sp('%s-汇总-国际直营' % (namess))

    dglc.cp()
    if nametyple == 34:
        dglc.dptmcs(45, ts, te, 2)
    else:
        dglc.dptmcs(123, ts, te, 2)
    dglc.sp('%s-汇总-天猫超市' % (namess))

    dglc.cp()
    if nametyple == 34:
        dglc.dp(45, ts, te, 2)
    else:
        dglc.dp(123, ts, te, 2)
    dglc.sp('%s-汇总-天猫旗舰店' % (namess))

    dglc.cp()
    if nametyple == 34:
        dglc.dpall(45, ts, te, 2)
    else:
        dglc.dpall(123, ts, te, 2)
    dglc.sp('%s-汇总-天猫全部' % (namess))

    dglc.cp()
    if nametyple == 34:
        dglc.dp(45, ts, te, 1)
        dglc.dpall(45, ts, te, 2)
    else:
        dglc.dp(123, ts, te, 1)
        dglc.dpall(123, ts, te, 2)
    dglc.sp('%s%s-交际-天猫其他' % (namess))

    dglc.cp()
    if nametyple == 34:
        dglc.dpqqg(45, ts, te, 2)
    else:
        dglc.dpqqg(123, ts, te, 2)
    dglc.sp('%s-汇总-全球购' % (namess))

    dglc.cp()
    if nametyple == 34:
        dglc.dptbjs(45, ts, te, 2)
    else:
        dglc.dptbjs(123, ts, te, 2)
    dglc.sp('%s-汇总-淘宝集市' % (namess))

    dglc.cp()
    dglc.hy(1, ts, te, 2)
    dglc.zdy('%s%s' % (namess, aipl_name), 3)
    dglc.sp('%s-汇总-新增会员' % (namess))
