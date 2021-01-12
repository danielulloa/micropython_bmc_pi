# Micropython Baseboard Management Controller
Un panel de control para monitorear el estado de cuatro Raspberry Pi 3B

![img](/img/rpi_case_01.jpeg)

## Micropython
Es compatible con el microcontrolador ESP8266, posee integración con Visual Studio Code lo que permite desarrollar rápidamente.

![img](/img/interfaz.jpeg)

## Reduciendo HTML
El diseño sencillo de este panel tiene un tamaño de 5KB lo cual debe ser reducido para evitar que el ESP8266 se quede sin memoria.

### Usando CSS shorthand

En el body tenemos especificado el color:

````css
body {
	background-color: #000;
}
````

``size = 33 byte``

podemos cambiarlo a:

````css
body{background:#000}
````

``size = 21 byte``

para los *contenedores grid* podemos hacer lo mismo:

````css
.grid-container {
    display: grid;
    width: auto;
    margin: 0 auto;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr 1fr;
    gap: 0px 0px;
    grid-template-areas:
        "PI-1 PI-1"
        "PI-2 PI-2"
        "PI-3 PI-3"
        "PI-4 PI-4";
}
````

``size = 193 bytes``

````css
.grid-container {
    display: grid;
    width: auto;
    margin: 0 auto;
    grid: repeat(4,1fr) / 1fr 1fr;
    gap: 0px 0px;
    grid-template-areas:
        "PI-1 PI-1"
        "PI-2 PI-2"
        "PI-3 PI-3"
        "PI-4 PI-4";
}
````

``size = 157 bytes``

otro shorthand para grid:

````css
.PI-4 {
            display: grid;
            align-self: center;
            justify-self: center;
            outline: 3px solid #272727;
            background: #444;
            width: auto;
            margin: 0 auto;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr;
            grid-template-areas:
                ". button_ON button_OFF";
        }
````

``size = 222 bytes``

````css
.PI-4 {
            display: grid;
            place-self: center center;
            outline: 3px solid #272727;
            background: #444;
            width: auto;
            margin: 0 auto;
            grid: 1fr / 1fr 1fr
            grid-template-areas:
                ". button_ON button_OFF";
        }
````

``size = 175 bytes``

cuando tenemos las propiedades top lef right bottom:

````css
.slider {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            border-radius: 34px
        }
````

``size = 97 bytes``

````css
.slider {
            position: absolute;
            inset: 0;
            background-color: #ccc;
            border-radius: 34px
        }
````

### Usando HTMLcompressor

El sitio [HTMLcompressor](https://htmlcompressor.com/compressor/) es una herramienta que comprime código HTML, CSS y javascript. Elegir el charset UTF8 ya que todos los caracteres en Inglés sólo necesitan 1 byte.

El código original tiene un tamaño de ``4830 bytes`` y luego de usar la herramienta ``2888 bytes``

Luego de utilizar variables de dos caracteres y cambios en el estilo, se redujo el tamaño de ``3732 bytes`` a ``2115 bytes``

## Uso de strings para servir contenido
Al momento de integrar variables en el html es más eficiente utilizar String Formatting ya que al concatenar se utilizan más recursos.

````python
html = '''
<html>
    <head> 
        <title>ESP8266</title>
    </head>
    <body> <h1>ESP8266</h1>
        <p>Temperatura: %s</p>
        <p>Presión: %s</p>
        <p>Humedad: %s</p>
    </body>
</html>

''' % (var1, var2, var3)



