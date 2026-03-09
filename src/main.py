from single_file import double
from module import *
import another_module.bits_funcs as bits_funcs

print(double(5))
print(math_funcs.sum_ints(3, 4))
print(bits_funcs.xor(True, False))