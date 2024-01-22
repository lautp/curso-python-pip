import read_csv
import charts

def run():
  result = read_csv.read_csv('./app/data.csv')
  result2 = []
  for x in result:
    result2.append((x['Country/Territory'],x['World Population Percentage']))

  labels = [a[0] for a in result2]
  values = [a[1] for a in result2]
  
  
  charts.generate_pie_chart(values, labels)
  
  

if __name__ == '__main__':
  result  = run()
