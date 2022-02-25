import querys as qs
import download_data as dd
import data_preprocessing as dp
from manage_data_collection import Manage_data

def run():
    pass

if __name__ == '__main__':
    #Create db and load tables
    qs.create_db()
    qs.load_tables()    

    #Save files csv in local store from website
    urls, nombreCategorias = dd.get_list_urls_csv_from_website()
    listaUrl = urls
    listaCategorias = nombreCategorias
    dfList = dd.convert_links_to_dataframe(listaUrl)
    dd.save_csv_localStorage(dfList, listaCategorias)

    # Clean data
    dp.clean_data()
 
    # Store data in the database
    md = Manage_data()
    md.insert_data()

    # Create views to analize data
    qs.load_views_registros()
    qs.load_views_cine()

    run()



