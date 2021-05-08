import pickle

def read_info():
    with open('static/DB/coronaDB.dat','rb') as f:
        Coronavirus_Cases = pickle.load(f)
        Deaths = pickle.load(f)
        Recovered = pickle.load(f)
        Table_Info = pickle.load(f)

    Info_dict = {
        'Coronavirus_Cases': Coronavirus_Cases,
        'Deaths' : Deaths,
        'Recovered' : Recovered,
        'Table_Info': Table_Info
    }
    return Info_dict