# x86-64 Assembly with Python on Windows

This project demonstrates calling a NASM-written x64 function from Python on
Windows. The example sums an array of unsigned 64-bit integers in assembly and
returns the result to Python.

## Requirements

- 64-bit Windows and 64-bit Python
- NASM at `%LOCALAPPDATA%\bin\NASM\nasm.exe`
- LLVM-MinGW at `%LOCALAPPDATA%\Programs\llvm-mingw`, including `bin\clang.exe`

The paths above are the defaults used by `NasmObjDll` in
[`Nasm_obj_dll.py`](./Nasm_obj_dll.py).

## Run the example

From this folder, run:

```powershell
py "Combine_py_asm v1.3.py"
```

The script assembles `Function.asm`, links it as `Function.dll`, loads the
function with Python's `ctypes`, and prints the sum and input array. With the
included sample values, the sum is `295`.

NASM and Clang produce `Function.obj` and `Function.dll` next to the source.
These are generated build files and are excluded from Git.

## Calling convention

`Function.asm` receives the array pointer in `RCX` and its element count in
`RDX`, as required by the Windows x64 calling convention. It adds each
8-byte element and returns the sum in `RAX`. The Python wrapper declares these
argument and return types with `ctypes` before calling the function.

## Project files

- `Function.asm` — the x64 array-summing function
- `Nasm_obj_dll.py` — assembles and links a NASM source file, then loads its DLL
- `Combine_py_asm v1.3.py` — Python example that calls `Function`
