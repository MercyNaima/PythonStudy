from MercyStudy import getnum


# convert a decimal floating-point num to binary, return binary num
def binfloat(_num, _precision=8):
    if not isinstance(_num, float):
        raise TypeError("输入内容非浮点数")

    _integer = getnum.get_integer_from_float(_num)
    _float = getnum.get_float_from_float(_num)
    _precision_count = 0
    _result_list = []
    _final_result_float = '.'
    while _precision_count < _precision:
        _float *= 2
        _result = getnum.get_integer_from_float(_float)
        _result_list.append(_result)
        _float = getnum.get_float_from_float(_float)
        _precision_count += 1
    for i in _result_list:
        _final_result_float += str(i)
    _final_result = float(str(bin(_integer)).lstrip('0b') + _final_result_float)
    return _final_result
