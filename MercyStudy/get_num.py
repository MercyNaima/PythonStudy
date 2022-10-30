

# return integer of float num
def get_integer_from_float(float_num):
    if not isinstance(float_num, float):
        raise TypeError("输入数据类型非浮点数")
    return int(str(float_num).split('.')[0])


# return 0.X, X = num after . from float num
def get_float_from_float(float_num):
    if not isinstance(float_num, float):
        raise TypeError("输入数据类型非浮点数")
    return float('0.' + str(float_num).split('.')[1])
