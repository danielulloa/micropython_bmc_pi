import socket
from machine import Pin

LED = Pin(2,Pin.OUT)

def pagina_web():
    if LED.value() == 1:
        estadoLED = '<h1 class="up">PI-1</h1>'
    else:
        estadoLED = '<h1 class="down">PI-1</h1>'

    html = """
<!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=300, initial-scale=1.0">
            <title>Raspberry Rack</title>
            <style>
                body{background-color:#000}.grid-container{display:grid;width:100%;margin:0 auto;grid-template-columns:1fr 1fr 1fr 1fr;grid-template-rows:1fr 1fr 1fr 1fr;gap:0 0;grid-template-areas:"PI-1 PI-1 PI-1 PI-1" "PI-2 PI-2 PI-2 PI-2" "PI-3 PI-3 PI-3 PI-3" "PI-4 PI-4 PI-4 PI-4"}.PI-1,.PI-2,.PI-3,.PI-4{display:grid;align-self:center;justify-self:center;outline:3px solid #272927;background-color:#444;width:100%;margin:0 auto;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr;gap:0 0;grid-template-areas:". button_ON button_OFF"}.PI-1{grid-area:PI-1}.PI-2{grid-area:PI-2}.PI-3{grid-area:PI-3}.PI-4{grid-area:PI-4}.button_ON{grid-area:button_ON;align-self:center;justify-self:center}.button_OFF{grid-area:button_OFF;align-self:center;justify-self:center}h1{color:#fff}.btn,.down,.up{padding:1em 2.1em 1.1em;border-radius:3px;margin:8px 8px 8px 8px;color:#fbdedb;background-color:#fbdedb;display:inline-block;background:#e74c3c;font-family:sans-serif;font-weight:800;font-size:.85em;text-transform:uppercase;text-align:center;text-decoration:none;box-shadow:0 -.3rem 0 rgba(0,0,0,.1) inset;position:relative}.up{color:green;background-color:#2f2f2f}.down{color:red;background-color:#2f2f2f}.red{background-color:#d55050}.green{background-color:#5bbd72}
            </style>
        </head>
        <body>
            <h1 align="center">PANEL CONTROL</h1>
            <div class="grid-container">
                <div class="PI-1">""" + estadoLED + """
                    <div class="button_ON"><a href="/?LED1=ON" class="btn green">ON</a></div>
            <div class="button_OFF"><a href="/?LED1=OFF" class="btn red">OFF</a></div>
        </div>
        <div class="PI-2">
            <h1 class="down">PI-2</h1>
            <div class="button_ON"><a href="/?LED2=ON" class="btn green">ON</a></div>
            <div class="button_OFF"><a href="/?LED2=OFF" class="btn red">OFF</a></div>
        </div>
        <div class="PI-3">
            <h1 class="down">PI-3</h1>
            <div class="button_ON"><a href="/?LED3=ON" class="btn green">ON</a></div>
            <div class="button_OFF"><a href="/?LED3=OFF" class="btn red">OFF</a></div>
        </div>
        <div class="PI-4">
            <h1 class="down">PI-4</h1>
            <div class="button_ON"><a href="/?LED4=ON" class="btn green">ON</a></div>
            <div class="button_OFF"><a href="/?LED4=OFF" class="btn red">OFF</a></div>
        </div>
    </div>
</body>

</html>
"""

    return html

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',80))
s.listen(5)

while True:
    cl, addr = s.accept()
    request = cl.recv(1024)
    request = str(request)
    LED_ON = request.find('/?LED1=ON')
    LED_OFF = request.find('/?LED1=OFF')
    if LED_ON == 6:
        LED.value(1)
    if LED_OFF == 6:
        LED.value(0)
    response = pagina_web()
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    cl.send('Connection: close\n\n')
    cl.sendall(response)
    cl.close()