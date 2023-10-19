tw_original = "¡Nuestras ayudantías fueron increíbles esta semana! 🚀 Un agradecimiento especial a #ElenaGarcía por su colaboracion y #LauraRodríguez por su dedicación y apoyo constante y a #CarlosMartínez por su grandioso trabajo. Gracias por hacer posible un ambiente de aprendizaje tan enriquecedor. ¡Seguimos creciendo juntos!"

aux1 = tw_original.index("#");
residuo1 = tw_original[aux1 + 1:]
aux_espacio1 = residuo1.index(" ");
print(residuo1[:aux_espacio1]) ## nombre1
aux2 = residuo1.index("#");
residuo2 = residuo1[aux2 + 1:]
aux_espacio2 = residuo2.index(" ");
print(residuo2[:aux_espacio2]) ## nombre1

tw_reverso = tw_original[::-1]
aux_ultimo = tw_reverso.index("#");
tw_reverso_reverso = tw_reverso[:aux_ultimo][::-1]
auxfinal = tw_reverso_reverso.index(" ")
print(tw_reverso_reverso[:tw_reverso_reverso.index(" ")]) ## nombre2