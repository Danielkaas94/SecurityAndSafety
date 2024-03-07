import json
import websocket
ws = websocket.WebSocket()   
ws.connect('ws://chat.students.dk:8080/') 
while True: 
  message = ws.recv()
  if (len(message)==0):
    print("Connection closed by server\n")
    break
  print(message)
  j = json.loads(message)
  hex = j['message'].replace(" ","")
  print(hex)

