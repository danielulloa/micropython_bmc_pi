try:
    import usocket as socket
except:
    import socket
def web_page():
  if r1.value() == 1:
    r1_state = ''
  else:
    r1_state = 'checked'
  if r2.value() == 1:
    r2_state = ''
  else:
    r2_state = 'checked'
  if r3.value() == 1:
    r3_state = ''
  else:
    r3_state = 'checked'
  if r4.value() == 1:
    r4_state = ''
  else:
    r4_state = 'checked'
  html = """
  <html>
<head>
<meta name="viewport" content="width=300, initial-scale=1.0">
<title>Raspberry Rack</title>
<style>body{background:#000}.gC{display:grid;grid:repeat(4,1fr) / 1fr 1fr;grid-template-areas:"p1 p1" "p2 p2" "p3 p3" "p4 p4"}.p1,.p2,.p3,.p4{display:grid;place-self:center center;outline:3px solid #272727;background:#444;width:auto;margin:0 auto;grid:1fr / 1fr 1fr;grid-template-areas:". bO"}.p1{grid-area:p1}.p2{grid-area:p2}.p3{grid-area:p3}.p4{grid-area:p4}h1{color:#fff}.up{background:#2f2f2f;padding:1em 2.1em 1.1em;border-radius:3px;margin:8px;display:inline-block;font-family:sans-serif;font-weight:800;font-size:.85em;text:center;box-shadow:0 -0.3rem 0 #0000001A inset}.bO{grid-area:bO;place-self:center center}.sW{position:relative;display:inline-block;width:88px;height:50px}.sW input{display:none}.sl{position:absolute;inset:0;background-color:#ccc;border-radius:34px}.sl:before{position:absolute;content:"";height:32px;width:32px;left:8px;bottom:8px;background:#fff;-webkit-transition:.4s;transition:.4s;border-radius:68px}input:checked+.sl{background-color:#2196f3}input:checked+.sl:before{-webkit-transform:translateX(42px);-ms-transform:translateX(42px);transform:translateX(42px)}</style>
<script>function tC(a){var b=new XMLHttpRequest();if(a.checked){b.open("GET","/?r"+a.id+"=1",true)}else{b.open("GET","/?r"+a.id+"=0",true)}b.send()};</script>
</head>
<body>
<div class="gC">
<div class="p1">
<h1 class="up">Pi1</h1>
<div class="bO"> <label class="sW"><input type="checkbox" onchange="tC(this)" id="1" %s><span class="sl"></span></label></div>
</div>
<div class="p2">
<h1 class="up">Pi2</h1>
<div class="bO"> <label class="sW"><input type="checkbox" onchange="tC(this)" id="2" %s><span class="sl"></span></label></div>
</div>
<div class="p3">
<h1 class="up">Pi3</h1>
<div class="bO"> <label class="sW"><input type="checkbox" onchange="tC(this)" id="3" %s><span class="sl"></span></label></div>
</div>
<div class="p4">
<h1 class="up">Pi4</h1>
<div class="bO"> <label class="sW"><input type="checkbox" onchange="tC(this)" id="4" %s><span class="sl"></span></label></div>
</div>
</div>
</body>
</html>
  """ % (r1_state, r2_state, r3_state, r4_state)
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    if gc.mem_free() < 120000:
      gc.collect()
    conn, addr = s.accept()
    conn.settimeout(3.0)
    request = conn.recv(512)
    conn.settimeout(None)
    request = str(request)
    r1_on = request.find('/?r1=1')
    r1_off = request.find('/?r1=0')
    r2_on = request.find('/?r2=1')
    r2_off = request.find('/?r2=0')
    r3_on = request.find('/?r3=1')
    r3_off = request.find('/?r3=0')
    r4_on = request.find('/?r4=1')
    r4_off = request.find('/?r4=0')
    if r1_on == 6:
      r1.value(0)
    if r1_off == 6:
      r1.value(1)
    if r2_on == 6:
      r2.value(0)
    if r2_off == 6:
      r2.value(1)
    if r3_on == 6:
      r3.value(0)
    if r3_off == 6:
      r3.value(1)
    if r4_on == 6:
      r4.value(0)
    if r4_off == 6:
      r4.value(1)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
    print(gc.mem_free())
  except OSError as e:
    conn.close()
    print('Connection closed')