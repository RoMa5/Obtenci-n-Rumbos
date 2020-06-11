## Obtención-Rumbos
### Programa para obtener rumbos mediante coordenadas
Emanuel Rodríguez Maldonado
- Ingeniero Topografo Geomatico, Facultad de Ingeniería Civil, Coquimatlán 28400, Colima, emanuelalejandro_rodriguez@ucol.mx
#### Resumen
Se realizó un programa en lenguaje Python que sea capaz de obtener correctamente el calculo de interés anual, conociendo así las cifras que tendrá año con año, dependiendo el tiempo que el usuario desee saber, las cuales estarán afectadas por el aumento en el interés que también deberá de ser ingresado por el usuario.
- Palabras clave: Rumbos, Coordenadas.
### Introducción
La obtención de valores que requiere un In-geniero Topógrafo Geomático, en este caso rumbos son de gran utilidad en su día a día ya que esos rumbos son fundamentales para los cálculos que requiera hacer, sea cual sea su proyecto a realizar en donde se necesitan conocer: coordenadas, rumbos, vértices, dis-tancias y demás elementos necesarios por ello se decidió hacer un programa el cual ahorre el tiempo del usuario haciendo uso de las tecnologías de información.
### Función del programa
El programa pretende funcionar de la siguien-te manera.
Se darán ciertas coordenadas las cuales por medio de algunos cálculos matemáticos nos darán el rumbo que tienen.
#### Calculos matematicos
Los cálculos matemáticos que se necesitaron para desarrollar el programa fueron los siguientes.
- Tangente inversa
- r = ((x2 – x1)/(y2-y1))
- tg = math.atan(r1)
- grados1 = math.degrees(tg1)
#### Estructura
Agregaremos las librerías necesarias que necesitará el programa
- Matplotlib sirve para graficar los datos.
- Numpy, sirve para usar las fórmulas.
- Math, sirve para funciones trigonométricas. 
- Csv, sirve para poder hacer uso de archivos con esa extensión.
### Manejo de Datos
Se manejaron datos .csv los cuales contenían las coordenadas que necesitábamos para la realización de este programa, también un bloc de notas, archivo de texto el cual está delimi-tado por comas.
### Conclusiones 
Gracias a los vídeos vistos y críticas de com-pañeros de la facultad y externos a ella nos dieron las herramientas para solucionar los problemas que se presentaron, funcionó de manera adecuada, como se esperaba, se com-plicó con el uso de librerías y el acomodo del código ya que Python es un lenguaje que res-peta la indentación y eso influye en que el programa compile de manea correcta.
