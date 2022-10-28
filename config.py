from sqlalchemy import create_engine

# ----------------文件路径-------------------

# 需剔除商品文件存储路径
drop_goods_path = r'D:\数据分析-数据建模小组\项目\微盘文件\WXWork\1688857943381142\WeDrive\LittleFreddie\线下数据\Ole\Ole竞品数据\ole竞品需要剔除的商品.xlsx'

# ole竞品季度原始数据存储路径
name = '.xlsx'
ole_competetor_path = rf'D:\数据分析-数据建模小组\项目\微盘文件\WXWork\1688857943381142\WeDrive\LittleFreddie\线下数据\Ole\Ole竞品数据\原始数据\{name}'

# ole季度可上传数据
name = '.xlsx'
ole_jingpin_path = rf'D:\数据分析-数据建模小组\项目\微盘文件\WXWork\1688857943381142\WeDrive\LittleFreddie\线下数据\Ole\Ole竞品数据\上传数据\{name}'

# 新增商品文件存储路径
ole_append_path = r'D:\数据分析-数据建模小组\项目\微盘文件\WXWork\1688857943381142\WeDrive\LittleFreddie\线下数据\Ole\Ole竞品数据\ole季度新增商品.xlsx'

# 存储数据库
SQL_RDS = 'mysql+pymysql://offline:jCm!2Gw*G!wR5d@rm-wz98f41r3x1l4050kuo.mysql.rds.aliyuncs.com/offline'
engine_RDS = create_engine(SQL_RDS,pool_recycle=1800)



