

def check_num_len(_num):
    if not _num > -128 and _num < 127:
        raise OverflowError("输入数值溢出")


def get_7_from_str(_str):
    _list = []
    for i in _str:
        _list.append(i)
    _count = 0
    _result = ''
    _list_len = len(_list)
    if _list_len < 8:
        while _count < 7 - _list_len:
            _list.insert(0, '0')
            _count += 1
        for i in _list:
            _result += i
        return _result
    else:
        while _count < 7:
            _result += _str[_count]
            _count += 1
        return _result
    pass


def bin_7(_num):
    if not isinstance(_num, int):
        raise TypeError("输入内容非整数")
    if _num > 0:
        return get_7_from_str(str(bin(_num)).lstrip('0b'))
    if _num < 0:
        return get_7_from_str(str(bin(_num)).lstrip('-0b'))


def true_to_radix(_num):
    check_num_len(_num)
    _list = []
    _count = 1
    _result = ''
    if _num > 0:
        _num = '0' + bin_7(_num)
    elif _num < 0:
        _num = '1' + bin_7(_num)
    else:
        return 0
    for i in _num:
        _list.append(i)
    if _list[0] == '0':
        return _num
    elif _list[0] == '1':
        while _count < 8:
            if _list[_count] == '0':
                _list[_count] = '1'
            elif _list[_count] == '1':
                _list[_count] = '0'
            _count += 1
    for i in _list:
        _result += i
    return _result


def true_to_complement(_num):
    _num = true_to_radix(_num)
    if _num == 0:
        return 0
    _list = []
    _count = 0
    _result = ''
    for i in _num:
        _list.append(i)
    if _list[0] == '0':
        return _num
    if _list[7] == '0':
        _list[7] = '1'
    if _list[7] == '1':
        _list[7] = '0'
        _list[6] = int(_list[6]) + 1
        while _count < 7:
            if _list[6 - _count] < 2:
                _list[6 - _count] = str(_list[6 - _count])
                break
            if _list[6 - _count] > 1:
                _list[6 - _count] = '0'
                _list[5 - _count] = int(_list[5 - _count]) + 1 if 5 - _count > -1 else None
    for i in _list:
        _result += i
    return _result
