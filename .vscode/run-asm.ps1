param(
    [Parameter(Mandatory = $true)]
    [string]$SourcePath
)

$SourcePath = (Resolve-Path -LiteralPath $SourcePath).Path
if ([System.IO.Path]::GetExtension($SourcePath) -ne ".asm") {
    throw "Expected a .asm source file: $SourcePath"
}

$nasm = Join-Path $env:LOCALAPPDATA "bin\NASM\nasm.exe"
$clang = Join-Path $env:LOCALAPPDATA "Programs\llvm-mingw\bin\clang.exe"
if (!(Test-Path -LiteralPath $nasm -PathType Leaf)) {
    throw "NASM was not found at $nasm"
}
if (!(Test-Path -LiteralPath $clang -PathType Leaf)) {
    throw "The x64 linker was not found at $clang"
}

$directory = [System.IO.Path]::GetDirectoryName($SourcePath)
$name = [System.IO.Path]::GetFileNameWithoutExtension($SourcePath)
$objectPath = Join-Path $directory "$name.obj"
$executablePath = Join-Path $directory "$name.exe"

& $nasm -f win64 $SourcePath -o $objectPath
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

& $clang $objectPath -o $executablePath
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

& $executablePath
exit $LASTEXITCODE
