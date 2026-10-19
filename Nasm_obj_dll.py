import ctypes
import os
import subprocess
from pathlib import Path

class NasmObjDll:
    def __init__(self, source_file: str):
        self.folder = Path(__file__).resolve().parent
        self.nasm = Path(os.environ["LOCALAPPDATA"]) / "bin" / "NASM" / "nasm.exe"
        self.clang = Path(os.environ["LOCALAPPDATA"]) / "Programs" / "llvm-mingw" / "bin" / "clang.exe"
        self.source = self.folder / source_file
        self.obj = self.folder / (self.source.stem + ".obj")
        self.dll = self.folder / (self.source.stem + ".dll")

    def __call__(self):
        if not self.obj.exists() or self.source.stat().st_mtime_ns > self.obj.stat().st_mtime_ns:
            subprocess.run(
                [str(self.nasm), "-f", "win64", str(self.source), "-o", str(self.obj)],
                check=True,
            )
        
        if not self.dll.exists() or self.obj.stat().st_mtime_ns > self.dll.stat().st_mtime_ns:
            subprocess.run(
                [str(self.clang), "-shared", str(self.obj), "-o", str(self.dll)],
                check=True,
            )
        return ctypes.CDLL(str(self.dll))

    def get_function(self, name: str, argtypes: list, restype):
        function = getattr(self(), name)
        function.argtypes = argtypes
        function.restype = restype
        return function
