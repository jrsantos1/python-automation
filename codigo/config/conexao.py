import pyodbc

class conexao:

    @staticmethod
    def get_conexao():
        sql_query = 'Driver={SQL Server};Server=DESKTOP-HO52AJ2;Database=SUCOS_VENDAS;Trusted_Connection=True;'
        return pyodbc.connect(sql_query)