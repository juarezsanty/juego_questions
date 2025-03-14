import random
import sys
# Preguntas para el juego
questions = [ "¿que funcion se usa para obtener la longitud de una cadena de python?" , "¿cual de las siguientes opciones es un numero entero en python?" , "¿como se solicita entrada del usuario en python?" , "¿cual de las siguientes expresiones es un comentario valido en python?" , "¿cual es el operador de comparacion para verificar si dos valores son iguales?" , ]
# respuestas posibles para cada pregunta en el mismo orden que las preguntas
answers = [ ("size()" , "len()" , "lenght()", "count()") , ("3.14" , "'42'" , "10", "true") , ("input()" , "scan()" , "read()" , "ask()") , ("//esto es un comentario" , "/* esto es un comentario */" , "--esto es un comentario" , "# esto es un comentario" ,) , ("=", "==", "!=", "===") , ]
#indice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
#junta 3 preguntas aleatorias con sus opciones y respuestas correctas en una tupla
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k = 3)
#el usuario debe contestar 3 preguntas
puntaje = 0.0
for question, answer_choices, correct_answers_index in questions_to_ask:
	
	#se muestra la pregunta y las respuestas posibles
	print (question)
	for i, answer in enumerate(answer_choices):
		print (f"{i + 1}. {answer}")
	
	#el usuario tiene 2 intentos para responder correctamente
	for intento in range(2):
		user_answer = input("respuesta: ")
		if user_answer.isdigit():
			user_answer = int(user_answer) - 1
			if user_answer >= 0 and user_answer < len(answer_choices):
				#se verifica si la respuesta es correcta
				if user_answer == correct_answers_index:
					print("¡correcto!")
					puntaje += 1.0
					break
				else:
					puntaje -= 0.5
			else:
				print ("respuesta invalida")
				sys.exit(1)
		else:
			print ("respuesta invalida")
			sys.exit(1)
	else:
		#si el usuario no responde correctamente despues de 2 intentos se muestra la respuesta correcta
		print ("incorrecto. la respuesta correcta es: ")
		print(answer_choices[correct_answers_index])
	
	#se imprime un blanco al final de la pregunta
	print()
print (puntaje)
