def getPopulation():
  keys=['col','bol']
  values=[300,400]
  return keys, values

def populationByCountries(data, country):
  result = list(filter(lambda item: item['Country']==country, data))
  return result