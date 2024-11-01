import pprint

filmsDict = {

    "Moana":{
      "yearRelease": 2017,
      "imdbRating": 9.1,
      "genre": ["fantasy", "Action"]
    },
    "Harry Potter":{
      "yearRelease": 2003,
      "imdbRating": 9.6,
      "genre": ["fantasy"]
    },
    "Jumper":{
      "yearRelease": 2017,
      "imdbRating": 7.4,
      "genre": ["Action"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - Buscar uma informação dentro de um dicionário aninhado
print(filmsDict["Harry Potter"]["genre"])

# 2 - Adicionar novo item
filmsDict["Moana"]["director"] = "Christopher Nolan"
print(filmsDict["Moana"])

# 3 - Excluindo um dicionário
del filmsDict["Jumper"]
pp.pprint(filmsDict)

