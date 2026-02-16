import py_compile
import pathlib
import sys

root = pathlib.Path(__file__).parent
failed = []
for p in root.rglob('*.py'):
    # skip virtual env or hidden folders if any
    try:
        py_compile.compile(str(p), doraise=True)
    except py_compile.PyCompileError as e:
        failed.append((str(p), str(e)))

if failed:
    print('Syntax errors found in:')
    for f, err in failed:
        print(f'- {f}: {err}')
    sys.exit(2)
else:
    print('All Python files compile cleanly.')
