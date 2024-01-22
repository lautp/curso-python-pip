import re
import random
import read_csv
import charts

def run():
  country = input('Selecciona un pais ').title()
  data = read_csv.read_csv('./data.csv')
  selection = dict(list(filter(lambda x: country in x['Country/Territory'], data))[0])

  dicc = {year[0:4]: int(population) for (year, population) in selection.items() 
             if 'population' in year.lower() 
             and re.search('[0-9]+', year)}
  
  labels = list(dicc.keys())
  labels.reverse()

  values = list(dicc.values())
  values.reverse()
  
  charts.genereate_bar_chart(selection['Country/Territory'], labels, values)


if __name__ == '__main__':
  result  = run()
