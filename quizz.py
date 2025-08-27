import random

def trivia_fetch(num: int) -> dict:
    """Devuelve un diccionario con trivia matemática sobre un número."""
    paridad = "par" if num % 2 == 0 else "impar"

    if num > 0:
        signo = "positivo"
    elif num < 0:
        signo = "negativo"
    else:
        signo = "cero"

    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    suma_digitos = sum(int(d) for d in str(abs(num)))
    return {
        "number": num,
        "paridad": paridad,
        "signo": signo,
        "es_primo": es_primo(num),
        "cuadrado": num ** 2,
        "divisible_por_3": num % 3 == 0,
        "divisible_por_5": num % 5 == 0,
        "divisible_por_10": num % 10 == 0,
        "mayor_que_100": num > 100,
        "multiplo_de_7": num % 7 == 0,
        "suma_digitos_paridad": "par" if suma_digitos % 2 == 0 else "impar"
    }

def main():
    print("🎲 Bienvenido al Quiz de los Números 🎲")
    numero = int(input("Elige tu número favorito: "))
    datos = trivia_fetch(numero)

    preguntas = [
        {
            "texto": "¿Tu número pertenece al equipo de los pares o al de los impares?",
            "opciones": ["par", "impar", "cero", "ninguno"],
            "respuesta": datos["paridad"]
        },
        {
            "texto": "Si tu número hablara de su estado de ánimo… sería:",
            "opciones": ["positivo", "negativo", "cero", "indefinido"],
            "respuesta": datos["signo"]
        },
        {
            "texto": "¿Tu número es primo?",
            "opciones": ["sí", "no", "tal vez", "ninguno"],
            "respuesta": "sí" if datos["es_primo"] else "no"
        },
        {
            "texto": "Imagina elevar tu número al cuadrado… ¿cuál es el resultado?",
            "opciones": [str(datos["cuadrado"]), str(datos["cuadrado"] + 1), str(datos["cuadrado"] - 1), "ninguno"],
            "respuesta": str(datos["cuadrado"])
        },
        {
            "texto": "Cuando divides tu número entre 3, ¿queda entero o sobra algo?",
            "opciones": ["entero", "sobra", "no se puede", "ninguno"],
            "respuesta": "entero" if datos["divisible_por_3"] else "sobra"
        },
        {
            "texto": "Si reparten tu número en montones de 5, ¿se reparte parejo o queda un resto?",
            "opciones": ["parejo", "resto", "no aplica", "ninguno"],
            "respuesta": "parejo" if datos["divisible_por_5"] else "resto"
        },
        {
            "texto": "¿Tu número obedece la regla de ser múltiplo de 10?",
            "opciones": ["sí", "no", "tal vez", "ninguno"],
            "respuesta": "sí" if datos["divisible_por_10"] else "no"
        },
        {
            "texto": "¿Tu número es un gigante que supera los 100?",
            "opciones": ["sí", "no", "no se sabe", "ninguno"],
            "respuesta": "sí" if datos["mayor_que_100"] else "no"
        },
        {
            "texto": "¿Tu número es múltiplo de 7?",
            "opciones": ["sí", "no", "tal vez", "ninguno"],
            "respuesta": "sí" if datos["multiplo_de_7"] else "no"
        },
        {
            "texto": "Si sumas las cifras de tu número, ¿el resultado final es par o impar?",
            "opciones": ["par", "impar", "no aplica", "ninguno"],
            "respuesta": datos["suma_digitos_paridad"]
        }
    ]

    puntaje = 0

    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta['texto']}")
        
        # Mezclar opciones aleatoriamente
        opciones_mezcladas = pregunta["opciones"].copy()
        random.shuffle(opciones_mezcladas)

        for idx, opcion in enumerate(opciones_mezcladas, ord('a')):
            print(f"{chr(idx)}) {opcion}")

        respuesta_usuario = input("Tu respuesta (a/b/c/d): ").strip().lower()

        # Identificar cuál letra corresponde a la respuesta correcta
        indice_correcto = chr(ord('a') + opciones_mezcladas.index(pregunta["respuesta"]))

        if respuesta_usuario == indice_correcto:
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {indice_correcto}) {pregunta['respuesta']}")

    print(f"\n🎉 Has terminado el quiz. Tu puntaje final es {puntaje}/{len(preguntas)}")

if __name__ == "__main__":
    main()
