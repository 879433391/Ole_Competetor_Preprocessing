import pandas as pd
from config import *


# ----------------读取文件---------------------
# 读取竞品数据
ole_jingpin_col = ['时间', '营运区域', '门店编码', '门店名称', '小类编码', '小类名称', '商品编码', '商品名称', '品牌', '数量', '金额']
df_ole_jingpin = pd.read_excel(ole_jingpin_path)[ole_jingpin_col]

# 读取商品匹配表
sql = "select * from goods_info_ka where 渠道 = 'Ole' and 模块 = '竞品'"
df_ole_goods_mapping = pd.read_sql(sql,engine_RDS)

# ---------------筛选出每季度新增的商品---------------
df_ole_append = df_ole_jingpin.loc[~df_ole_jingpin['商品编码'].isin(df_ole_goods_mapping['商品编码']),['商品编码','商品名称']]
df_ole_append.drop_duplicates(inplace=True)

# ------------- 写入文件 --------------------
df_ole_append.to_excel(ole_append_path,index=False)



