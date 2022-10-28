import pandas as pd
from config import *


# ----------------读取文件---------------------
# 读取需剔除商品
drop_goods_col = ['商品编码','商品名称']
df_drop_goods = pd.read_excel(drop_goods_path)[drop_goods_col]

# 读取ole原始季度数据
ole_jingpin_col = ['时间', '营运区域', '门店编码', '门店名称', '小类编码', '小类名称', '商品编码', '商品名称', '品牌', '数量', '金额']
jingpin_ole_dtype = {'营运区域':'str','门店名称':'str', '模块':'str', '时间':'datatime', '门店编码':'str', '商品编码':'str',
                     '商品名称':'str','数量':'int','金额':'float64'}
df_ole_jingpin = pd.read_excel(ole_jingpin_path,dtype=jingpin_ole_dtype)[ole_jingpin_col]


# --------------- 判别 ---------------------
df_ole_jingpin['是否剔除'] = '否'
df_ole_jingpin.loc[df_ole_jingpin['商品编码'].isin(df_drop_goods['商品编码']),['是否剔除']] = '是'


# ---------------写入文件---------------
df_ole_jingpin.to_excel(r'C:\Users\chn1158\Desktop\OLE测试\.xlsx',index=False)




