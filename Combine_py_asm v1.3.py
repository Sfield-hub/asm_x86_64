import ctypes
from  Nasm_obj_dll import NasmObjDll


def sum_numbers(numbers: list):
    values = (ctypes.c_uint64 * len(numbers))(*numbers)
    return sum_f(values, len(numbers)), values



numbers = [12, 20, 30, 45, 50, 60, 78]
#values = (ctypes.c_uint64 * len(numbers))(*numbers)
sum_f = NasmObjDll("Function.asm").get_function(
    "Function", [ctypes.POINTER(ctypes.c_uint64), ctypes.c_size_t],
    ctypes.c_uint64)

result, values = sum_numbers(numbers)
print(result, list(values))
