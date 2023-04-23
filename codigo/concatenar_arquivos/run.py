import os
import pandas as pd

caminho = os.path.abspath(os.path.dirname(os.curdir))
caminho_abs = os.path.join(caminho, 'files')

os.listdir

files = []

for file in os.listdir(caminho_abs):
    file_path = os.path.join(caminho_abs, file)
    if os.path.isfile(file_path):
        files.append(file)

files.sort()
files.reverse()

recent_file = os.path.join(caminho_abs, files[0])
previous_file = os.path.join(caminho_abs, files[1])

df_recent = pd.read_excel(recent_file)
df_previous = pd.read_excel(previous_file)

df_merge = df_recent.merge(df_previous, how='outer', on='cod')
df_merge.fillna('', inplace=True)

df_adicionados = df_merge.query('nome_y == ""')
df_removidos = df_merge.query('nome_x == ""')

print(files)