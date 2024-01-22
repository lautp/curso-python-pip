import utils

data = [
  {
    'Country':'Colombia',
    'Population':500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():
  
  keys, values = utils.getPopulation()
  
  print(keys, values)
  
  
  country = input('Ingrese pais a buscar (Bolivia o Colombia) ').title()
  
  selected = utils.populationByCountries(data, country)
  
  print(selected)

if __name__ == '__main__':
  run()