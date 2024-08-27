from pathlib import Path

home_dir = Path.home()
cwd = Path.cwd()
one_above = Path.cwd().parent
two_above = Path.cwd().parents[1]
print(f'Home: {home_dir}')
print(f'Current work directory: {cwd}')
print(f'One above cwd: {one_above}')
print(f'Two above cwd: {two_above}')
