from MercyStudy import getnum


def check_float(_num):
    if not isinstance(_num, float):
        raise TypeError("输入内容非浮点数")
    return True


# convert float part of float num from decimal to dec which you pointed, return float num
def float_dec_convert(_float_input, _dec, _precision=8):
    check_float(_float_input)
    _float = getnum.get_float_from_float(_float_input)
    _precision_count = 0
    _result_list = []
    _final_result_float = '0.'
    while _precision_count < _precision:
        _float *= _dec
        _result = getnum.get_integer_from_float(_float)
        _result_list.append(_result)
        _float = getnum.get_float_from_float(_float)
        _precision_count += 1
    for i in _result_list:
        _final_result_float += str(i)
    return float(_final_result_float)


# convert a decimal floating-point num to binary, return binary num
def bin_float(_num, _precision=8):
    check_float(_num)
    _integer = getnum.get_integer_from_float(_num)
    return float(str(bin(_integer)).lstrip('0b') + str(float_dec_convert(_num, 2)).lstrip('0'))


# convert a decimal floating-point num to oct, return oct num
def oct_float(_num, _precision=8):
    check_float(_num)
    _integer = getnum.get_integer_from_float(_num)
    return float(str(oct(_integer).lstrip('0o')) + str(float_dec_convert(_num, 8)).lstrip('0'))
