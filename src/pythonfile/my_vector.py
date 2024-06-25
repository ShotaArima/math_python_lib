# 例外
class NoneVectorError(Exception):
    pass

# 足し算引き算が可能な状態かの判別
def check_vector(vector1, vector2):
    if vector1 == [] || vector2 == []:
        raise NoneVectorError
    
        

# たし引きの関数

# 内積

# 外積

# スカラー倍

# 絶対値L1

# 絶対値L2