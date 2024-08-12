from extractCSV import extract_bancos, extract_empregados, extract_reclamacoes
from transformLoad import load, transform_bancos, transform_empregados, transform_reclamacoes
from config import db, mysql_db
from analyse import create_view, select_from_table, create_view_mysql, select_from_table_mysql

def main():
    try:
        print('Configuring Database')
        db.configure()
        mysql_db.configure()
        
        print('Extracting bancos files')
        extract_bancos.execute()

        print('Extracting  empregados files')
        extract_empregados.execute()

        print('Extracting  reclamacoes files')
        extract_reclamacoes.execute()
        
        print('Transforming bancos')
        transform_bancos.execute()
        
        print('Transforming empregados')
        transform_empregados.execute()
        
        print('Transforming reclamacoes')
        transform_reclamacoes.execute()

        print('Transforming reclamacoes')
        load.main()

        print('Creating view')
        create_view.execute()
        
        print('Selecting from Table')
        select_from_table.execute('mydb')
        
        print('Creating view in mysql')
        create_view_mysql.execute()
        
        print('Selecting from Table in mysql')
        select_from_table_mysql.execute()
        
    except Exception as err:
        print(err)
        raise err
main()
