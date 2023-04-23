import sys
import pandas as pd
sys.path.append('C:\code\estudos\python\\automacao_projeto\codigo\config')

from conexao import conexao
#import conexao

class tables:

    @staticmethod
    def get_notas_fiscais() -> pd.DataFrame:
        sql_query = 'select * from [NOTAS FISCAIS]'
        with conexao.get_conexao() as con:
            df = pd.read_sql(sql=sql_query, con=con)
            return df

