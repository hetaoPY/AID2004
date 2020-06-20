# import time
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接，修改为你的数据库用户名和密码
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/stu', echo=True)
Base = declarative_base()


class Player(Base):
    # 表的名字:
    __tablename__ = 'player'

    def __init__(self, team_id=None, player_name=None, height=None):
        self.team_id = team_id
        self.player_name = player_name
        self.height = height

    # 表的结构:
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer)
    player_name = Column(String(255))
    height = Column(Float(3, 2))


# 创建数据表结构
Base.metadata.create_all(engine)

















# def superEggDrop( K: int, N: int) -> int:
#     memo = {}
#     def dp(k, n):
#         if (k, n) not in memo:
#             if n == 0:
#                 ans = 0
#             elif k == 1:
#                 ans = n
#             else:
#                 lo, hi = 1, n
#                 # keep a gap of 2 X values to manually check later
#                 while lo + 1 < hi:
#                     x = (lo + hi) // 2
#                     t1 = dp(k-1, x-1)
#                     t2 = dp(k, n-x)
#                     if t1 < t2:
#                         lo = x
#                     elif t1 > t2:
#                         hi = x
#                     else:
#                         lo = hi = x
#                 ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
#                               for x in (lo, hi))
#             memo[k, n] = ans
#         return memo[k, n]
#     return dp(K, N)

# def get_num(K, N):
#     if K == 0 or N == 0:
#         return 0
#     if K == 1:
#         return N
#     elif N == 1:
#         return 1
#
#     result = min(max(get_num(K, X - 1), get_num(K - 1, N - X)) for X in range(1, N)) + 1
#
#     return result


# start_time = time.time()
# print(superEggDrop(4, 5000))
# over_time = time.time()
# print(over_time-start_time)
