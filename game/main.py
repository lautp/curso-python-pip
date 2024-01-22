import random
options = ('piedra', 'papel', 'tijera')
user_win = 0
computer_win = 0

while user_win < 2 and computer_win < 2:
  user_option = input('piedra, papel o tijera! ').lower()
  
  computer_option = random.choice(options)
  
  if not user_option in options:
    print('Esa opcion no existe')
    continue
  
  if user_option == computer_option:
    print("Empate!")
  elif user_option == 'piedra':
    print(computer_option+'!')
    if computer_option == 'tijera':
      user_win+=1
      print('Ganaste!')
      print('Puntaje')
      print('Usuario: ', user_win)
      print('Computadora: ', computer_win)
    else:
      computer_win+=1
      print('Perdiste!')
      print('Puntaje')
      print('Usuario: ', user_win)
      print('Computadora: ', computer_win)
  elif user_option == 'papel':
    print(computer_option+'!')
    if computer_option == 'piedra':
      user_win+=1
      print('Ganaste')
      print('Puntaje')
      print('Usuario: ', user_win)
      print('Computadora: ', computer_win)
    else:
      computer_win+=1
      print('Perdiste!')
      print('Puntaje')
      print('Usuario: ', user_win)
      print('Computadora: ', computer_win)
  elif user_option  == 'tijera':
    print(computer_option+'!')
    if computer_option == 'papel':
      user_win+=1
      print('Ganaste!')
      print('Puntaje')
      print('Usuario: ', user_win)
      print('Computadora: ', computer_win)
    else:
      computer_win+=1
      print('Perdiste!')
      print('Puntaje')
      print('Usuario: ', user_win)
      print('Computadora: ', computer_win)

if user_win == 2:
  print('Felicitaciones, ganaste!')
  print('Fin del juego')
elif computer_win == 2:
  print('Perdiste, intentalo de nuevo!')
  print('Fin del juego')