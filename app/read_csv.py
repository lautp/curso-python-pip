import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    res_dict = []
    header = next(reader)

    for row in reader:
      res_dict.append({header[i]: row[i] for i in range(len(header))})

    return res_dict

if __name__ == '__main__':
  res_dict = read_csv('./data.csv')
  print(res_dict)