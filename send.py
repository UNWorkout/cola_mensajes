import pika, json

#credentials=pika.PlainCredentials(username='tu_usuario', password='tu_contraseña')
def enviar_rutina_a_cola(rutina):
    # connection a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
    canal = connection.channel()
    canal.queue_declare(queue='rutinas')
    # Convertir la rutina a formato JSON
    rutina_json = json.dumps(rutina)
    # Publicar el mensaje en la cola
    canal.basic_publish(exchange='',routing_key='rutinas',body=rutina_json)
    print("Mensaje enviado:", rutina_json)
    # Cerrar la connection
    connection.close()

# Datos que deseas enviar como JSON
rutina = {   
  "usuario_id": 1,
  "correo": "correo de prueba gmail",
  "dias_semana": [
      {
      "dia": "Domingo",
      "ejercicios": ["ejercicio1", "ejercicio2"],
      "Hora_inicio": "22:30"
      },
      {
      "dia": "Lunes",
      "ejercicios": ["ejercicio1", "ejercicio2"],
      "Hora_inicio": "22:30"
      },
      {
      "dia": "Martes",
      "ejercicios": ["ejercicio1", "ejercicio2"],
      "Hora_inicio": "22:30"
      },
      {
      "dia": "Miercoles",
      "ejercicios": ["ejercicio1", "ejercicio2"],
      "Hora_inicio": "22:30"
      },
      {
      "dia": "Jueves",
      "ejercicios": ["ejercicio1", "ejercicio2"],
      "Hora_inicio": "22:30"
      },
      {
      "dia": "Viernes",
      "ejercicios": ["ejercicio1", "ejercicio2"],
      "Hora_inicio": "22:30"
      },
      {
      "dia": "Sabado",
      "ejercicios": ["ejercicio1", "ejercicio2"],
      "Hora_inicio": "22:30"
      }]
}


# Llamada a la función para enviar el JSON a la cola
enviar_rutina_a_cola(rutina)