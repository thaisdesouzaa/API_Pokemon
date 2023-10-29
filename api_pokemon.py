import requests
import json
from config.schemas import Time
from fastapi import FastAPI,Path
from config.config import ApiConfig

app = FastAPI()

@app.post("/api/teams")
def criar_time(time:Time):


    #Abrindo arquivo json
    with open(ApiConfig.ARQ, "r") as arq:
        times_salvos = json.load(arq)

    id_time = 0
    #Verificando se json esta vazio - para colocar o primeiro id
    if not times_salvos:
        id_time = 1
        #JA TENHO O VALOR DO NOVO ID
    #Buscando o ultimo valor de id do time cadastrado para gerar novo id unico
    else:
        chaves = times_salvos.keys()
        chaves_ordenadas = sorted(chaves, key=lambda x: int(x))
        ultimo_id = chaves_ordenadas[-1]
        id_time = int(ultimo_id) + 1
    
    user = time.user
    qtd = len(time.team)
    lista_pokemons = []

    #Time com quantidade correta
    if(qtd <= 6):   
        #Varrendo cada pokemon da lista do user
        for pokemon in time.team:
            #Verifica se o nome nao esta vazio (se for igual a zero nao tem nada escrito)
            if(len(pokemon) > 0):

                #Verifica se a busca teve resultado
                try: 
                    #Buscando informacoes do pokemon    
                    poke_info = requests.get(ApiConfig.URL + pokemon)
                    poke_info = poke_info.json()       
                except Exception as e:
                    return f"Pokemon com o nome de {pokemon} nao foi encontrado!"

                #Guardando informacoes em um dicionario: ID DO POKEMON - NOME - ALTURA - PESO
                poke_dic = {
                    "id" : poke_info["id"],
                    "name": pokemon,
                    "weight": poke_info["weight"],
                    "height": poke_info["height"]
                }
                #Adicionando o dicionario na lista de pokemons
                lista_pokemons.append(poke_dic)           
   
            else:
                return "ERRO: Nome de Pokemon está vazio"

    else:
        return "ERRO: Time excedendo 6 Pokemons"
        
    #Criando chave no dic com id unico e guardando o nome do user e lista de pokemons
    times_salvos[id_time] = {
        "owner": user,
        "pokemons": lista_pokemons
    } 

    #Salvando no Json
    with open(ApiConfig.ARQ, "w") as arq:
        json.dump(times_salvos, arq)

    #TIME SALVO - MENSAGEM DE VALIDACAO E ID 
    return "*-* Sucesso!! Seu time de Pokemons foram salvos corretamente! *-*"
    return f"Seu ID do time é: {id_time}"


#Busca e retorna todos os times registrados
@app.get("/api/teams")
def busca_todos_times():

    #Abrindo arquivo json
    with open(ApiConfig.ARQ, "r") as arq:
        times_salvos = json.load(arq)

    #Verificando se json esta vazio 
    if not times_salvos:
        return "Poxa! Nenhum time foi criado ainda!"

    else:
        return times_salvos


#Retorna times registrados referentes ao id 
@app.get("/api/teams/{id}")
def busca_time_id(id:int = Path()):

    #Abrindo arquivo json
    with open(ApiConfig.ARQ, "r") as arq:
        times_salvos = json.load(arq)
 
    chaves = times_salvos.keys()
    nao_encontrado = len(chaves)

    #Buscando id de busca
    for id_time in times_salvos:
        if(int(id_time) == id):

            return times_salvos[id_time]
        nao_encontrado = nao_encontrado - 1 
    
    #Id nao encontrado
    if nao_encontrado == 0:
        return f"Poxa! O time com o id: {id} nao foi encontrado!"