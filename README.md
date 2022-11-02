# PythonStudy

## Table of Contents

- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
- [License](#license)

## Usage

```bash
from MercyStudy import *

dec_convert.bin_float(59.05)
```

## API

### dec_convert.bin_float(num, precision=8)

```bash
convert a decimal floating-point number to binary
- num <type:float>
- precision <type:int> <default:8>
- return binary-num <type:float>
```

### dec_convert.oct_float(num, precision=8)

```bash
convert a decimal floating-point number to octal
- num <type:float>
- precision <type:int> <default:8>
- return octal-num <type:float>
```

### dec_convert.hex_float(num, precision=8)

```bash
convert a decimal floating-point number to hexadecimal
- num <type:float>
- precision <type:int> <default:8>
- return hexadecimal-num <type:str>
```

### code_convert.true_to_radix(num)

```bash
calculate the inverse of a int num
- num <type:int>
- return inversed binary num <type:str>
```

### code_convert.true_to_complement(num)

```bash
calculate the complement of a int num
- num <type:int>
- return complemented binary num <type:str>
```

## Contributing
PRs accepted.

## License
[MIT](https://choosealicense.com/licenses/mit/)
