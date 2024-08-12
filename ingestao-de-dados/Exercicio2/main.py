from extractCSV import extract_bancos, extract_empregados, extract_reclamacoes
from transformLoad import load, transform_bancos, transform_empregados, transform_reclamacoes
from config import db
from analyse import create_view, select_from_table

def main():
    try:
        print('Configuring Database')
        db.configure()
        
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
        
    except Exception as err:
        print(err)
        raise err
main()
