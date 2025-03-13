import random
# Preguntas para el juego
questions = [ "¿que funcion se usa para obtener la longitud de una cadena de python?" , "¿cual de las siguientes opciones es un numero entero en python?" , "¿como se solicita entrada del usuario en python?" , "¿cual de las siguientes expresiones es un comentario valido en python?" , "¿cual es el operador de comparacion para verificar si dos valores son iguales?" , ]
# respuestas posibles para cada pregunta en el mismo orden que las preguntas
answers = [ ("size()" , "len()" , "lenght()", "count()") , ("3.14" , "'42'" , "10", "true") , ("input()" , "scan()" , "read()" , "ask()") , ("//esto es un comentario" , "/* esto es un comentario */" , "--esto es un comentario" , "# esto es un comentario" ,) , ("=", "==", "!=", "===") , ]
#indice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
#el usuario debe contestar 3 preguntas
for _ in range(3):
	# se selecciona una pregunta aleatoria
	question_index = random.randint(0, len(questions) -1)
	
	#se muestra la pregunta y las respuestas posibles
	print (questions[question_index])
	for i, answer in enumerate(answers[question_index]):
		print (f"{i + 1}. {answer}")
	
	#el usuario tiene 2 intentos para responder correctamente
	for intento in range(2):
		user_answer = int(input("respuesta: ")) - 1
		#se verifica si la respuesta es correcta
		if user_answer == correct_answers_index[question_index]:
			print("¡correcto!")
			break
	else:
		#si el usuario no responde correctamente despues de 2 intentos se muestra la respuesta correcta
		print ("incorrecto. la respuesta correcta es: ")
		print(answers[question_index][correct_answers_index[question_index]])
	
	#se imprime un blanco al final de la pregunta
	print()
