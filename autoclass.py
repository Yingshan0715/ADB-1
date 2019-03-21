from .baseclass import BaseAuto


class AutoDatabank(BaseAuto):

    def __repr__(self):
        return('A toolclass writed by Ausar.Lu from connext.Ltd\r \
        →→→→  zhanghao     :%s        ←←←←\r \
        →→→→  tmall_global :%s    ←←←←\r \
        →→→→  purchase_Behaviour :%s ←←←←\r \
        →→→→  yybp_order   :%s        ←←←←\r \
        →→→→  ppld_order   :%s        ←←←←\r \
        →→→→  ppzq_order   :%s        ←←←←\r \
        →→→→  mxdp_order   :%s        ←←←←\r \
        →→→→  zszw_order   :%s        ←←←←' % (
            self.zhanghao, self.tmall_global,
            self.purchase_Behaviour, self.yybp_order,
            self.ppld_order, self.ppzq_order,
            self.mxdp_order, self.zszw_order))

    def qll(self, aipl, start_date, end_date, jbc='j'):
        '''全链路状态--不带二级类目'''
        self._quanlianluzhuangtai(aipl, None, start_date, end_date, jbc)

    def qll_erjileimu(self, aipl, erjileimu, start_date, end_date, jbc='j'):
        '''全链路状态--带二级类目'''
        assert isinstance(erjileimu, str)
        self._quanlianluzhuangtai(aipl, erjileimu, start_date, end_date, jbc)
    #############################☆######################################

    def ud(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---Uni Desk'''
        zh_p = 0  # 必填参数 补位 无实际影响
        self._fufeiguanggao(1, qujian, start_date,
                            end_date, jbc, action, zh_p)

    def ykgg(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---优酷广告'''
        zh_p = 0  # 必填参数 补位 无实际影响
        self._fufeiguanggao(2, qujian, start_date,
                            end_date, jbc, action, zh_p)

    def yybp(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---一页霸屏 '''
        zh_p = self.yybp_order
        if zh_p == 0:
            pass
        else:
            self._fufeiguanggao(3, qujian, start_date,
                                end_date, jbc, action, zh_p)

    def ppld(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---品牌雷达 '''
        zh_p = self.ppld_order
        if zh_p == 0:
            pass
        else:
            self._fufeiguanggao(4, qujian, start_date,
                                end_date, jbc, action, zh_p)

    def ppzq(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---品牌专区 '''
        zh_p = self.ppzq_order
        if zh_p == 0:
            pass
        else:
            self._fufeiguanggao(5, qujian, start_date,
                                end_date, jbc, action, zh_p)

    def mxdp(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---明星店铺 '''
        zh_p = self.mxdp_order
        if zh_p == 0:
            pass
        else:
            self._fufeiguanggao(6, qujian, start_date,
                                end_date, jbc, action, zh_p)

    def zszw(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---钻石展位 '''
        zh_p = self.zszw_order
        if zh_p == 0:
            pass
        else:
            self._fufeiguanggao(7, qujian, start_date,
                                end_date, jbc, action, zh_p)

    def pptx(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---品牌号衍生广告'''
        zh_p = 0  # 必填参数 补位 无实际影响
        self._fufeiguanggao(8, qujian, start_date,
                            end_date, jbc, action, zh_p)

    def yyy(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---摇一摇'''
        zh_p = 0  # 必填参数 补位 无实际影响
        self._fufeiguanggao(9, qujian, start_date,
                            end_date, jbc, action, zh_p)

    def _sjyx(self, qujian, start_date, end_date, jbc='j', action=1):
        '''付费广告---事件营销|暂不开启'''
        zh_p = 0  # 必填参数 补位 无实际影响
        self._fufeiguanggao(10, qujian, start_date,
                            end_date, jbc, action, zh_p)

    #############################☆######################################
    #############################☆######################################

    def pph(self, actype, action, start_date, end_date, jbc='j'):
        '''内容渠道---品牌号'''
        self._pinpaihao(actype, action, start_date, end_date, jbc)

    def tbtt(self, action, start_date, end_date, jbc='j'):
        '''内容渠道---淘宝头条'''
        self._neirongyunying(2, action, start_date, end_date, jbc)

    def yhh(self, action, start_date, end_date, jbc='j'):
        '''内容渠道---有好货'''
        self._neirongyunying(3, action, start_date, end_date, jbc)

    def bmqd(self, action, start_date, end_date, jbc='j'):
        '''内容渠道---必买清单'''
        action = 1  # 默认只有一种行为 适应输入性的友好设计
        self._neirongyunying(4, action, start_date, end_date, jbc)

    def cnxh(self, action, start_date, end_date, jbc='j'):
        '''内容渠道---猜你喜欢'''
        action = 1  # 默认只有一种行为 适应输入性的友好设计
        self._neirongyunying(5, action, start_date, end_date, jbc)

    def shyjs(self, action, start_date, end_date, jbc='j'):
        '''内容渠道---生活研究所'''
        self._neirongyunying(6, action, start_date, end_date, jbc)

    def zb(self, action, start_date, end_date, jbc='j'):
        '''内容渠道---直播 action为是否V任务'''
        self._neirongyunying(7, action, start_date, end_date, jbc)

    def wt(self, action, start_date, end_date, jbc='j'):
        '''内容渠道---微淘'''
        self._neirongyunying(8, action, start_date, end_date, jbc)

    def mrhd(self, action, start_date, end_date, jbc='j'):
        '''内容渠道---每日好店'''
        self._neirongyunying(10, action, start_date, end_date, jbc)
    #############################☆######################################
    #############################☆######################################

    def cjppr(self, action, start_date, end_date, jbc='j'):
        '''天猫营销平台---超级品牌日'''
        self._yingxiaopingtai(1, 1, action, start_date, end_date, jbc)

    def hdb(self, actype, action, start_date, end_date, jbc='j'):
        '''天猫营销平台---互动吧'''
        self._yingxiaopingtai(2, actype, action, start_date, end_date, jbc)

    def thllb(self, actype, action, start_date, end_date, jbc='j'):
        '''天猫营销平台---天合&流量宝'''
        self._yingxiaopingtai(3, actype, action, start_date, end_date, jbc)

    def jhs(self, action, start_date, end_date, jbc='j'):
        '''天猫营销平台---聚划算'''
        self._yingxiaopingtai(4, 1, action, start_date, end_date, jbc)

    def syzx(self, action, start_date, end_date, jbc='j'):
        '''天猫营销平台---试用中心'''
        self._yingxiaopingtai(5, 1, action, start_date, end_date, jbc)

    def tmux(self, action, start_date, end_date, jbc='j'):
        '''天猫营销平台---天猫U先'''
        self._yingxiaopingtai(6, 1, action, start_date, end_date, jbc)

    def tqg(self, action, start_date, end_date, jbc='j'):
        '''天猫营销平台---淘抢购'''
        self._yingxiaopingtai(7, 1, action, start_date, end_date, jbc)

    def hjr(self, action, start_date, end_date, jbc='j'):
        '''天猫营销平台---欢聚日'''
        self._yingxiaopingtai(8, 1, action, start_date, end_date, jbc)
    #############################☆######################################
    #############################☆######################################

    def cnyz(self, action, start_date, end_date, jbc='j'):
        '''线下触点---菜鸟驿站'''
        self._xianxiachudian(1, action, start_date, end_date, jbc)

    def xianxiaUxian(self, action, start_date, end_date, jbc='j'):
        '''线下触点---菜鸟驿站'''
        self._xianxiachudian(2, action, start_date, end_date, jbc)

    def zhsq(self, action, start_date, end_date, jbc='j'):
        '''线下触点---菜鸟驿站'''
        self._xianxiachudian(3, action, start_date, end_date, jbc)
    #############################☆######################################
    #############################☆######################################

    def xtmgj(self, action, start_date, end_date, jbc='j'):
        '''销售渠道---天猫国际'''
        assert action in [1, 2, 3]
        action = 2 if action == 3 else action
        self._xiaoshouqudao(1, action, start_date, end_date, jbc)

    def xtmcs(self, start_date, end_date, jbc='j'):
        '''销售渠道---天猫超市'''
        self._xiaoshouqudao(3, action, start_date, end_date, jbc)

    def xtm(self, action, start_date, end_date, jbc='j'):
        '''销售渠道---天猫'''
        assert action in [1, 2, 3]
        action = 3 if action == 2 else action
        self._xiaoshouqudao(4, action, start_date, end_date, jbc)

    # def tm: ↑↑↑↑↑↑↑↑↑↑↑↑
    # def totaltm :↑↑↑↑↑↑↑↑↑↑↑↑
    # def dp: pass ↓↓↓↓↓↓↓↓↓↓↓↓
    # def totaldp: pass↓↓↓↓↓↓↓↓↓↓↓↓

    def dpall(self, action, start_date, end_date, jbc='j'):
        '''店铺商品圈人-所有销售渠道'''
        self._dianpushangpin(1, action, start_date, end_date, jbc)

    def dptmgj(self, action, start_date, end_date, jbc='j'):
        '''店铺商品圈人-天猫国际'''
        self._dianpushangpin(2, action, start_date, end_date, jbc)

    def dptmgjzy(self, action, start_date, end_date, jbc='j'):
        '''店铺商品圈人-天猫国际直营'''
        self._dianpushangpin(3, action, start_date, end_date, jbc)

    def dptmcs(self, action, start_date, end_date, jbc='j'):
        '''店铺商品圈人-天猫超市'''
        self._dianpushangpin(4, action, start_date, end_date, jbc)

    def dptm(self, action, start_date, end_date, jbc='j'):
        '''店铺商品圈人-天猫旗舰店'''
        self._dianpushangpin(5, action, start_date, end_date, jbc)

    def dpqqg(self, action, start_date, end_date, jbc='j'):
        '''店铺商品圈人-全球购'''
        self._dianpushangpin(6, action, start_date, end_date, jbc)

    def dptbjs(self, action, start_date, end_date, jbc='j'):
        '''店铺商品圈人-全球购'''
        self._dianpushangpin(7, action, start_date, end_date, jbc)

    # 补充原来的接口
    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    def tm(self, action, start_date, end_date, jbc='j'):
        if self._purchase_Behaviour == 'gj':
            self.xtmgj(action, start_date, end_date, jbc)
        elif self._purchase_Behaviour == 'dp':
            self.xtm(action, start_date, end_date, jbc)

    def dp(self, action, start_date, end_date, jbc='j'):
        if self._purchase_Behaviour == 'gj':
            self.dptmgj(action, start_date, end_date, jbc)
        elif self._purchase_Behaviour == 'dp':
            self.dptm(action, start_date, end_date, jbc)

    qqdgm = dpall
