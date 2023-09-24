import pika,json,sys,os

def callback(ch, method, properties, body):
    # Recibir el mensaje de la cola
    rutina = json.loads(body)
    print("Cuerpo del mensaje:", rutina)    
    # Realizar cálculos
    ejercicios_realizados = 0
    duracion_total = 0
    for dia in rutina['dias_semana']:
        ejercicios_realizados += len(dia['ejercicios'])
        # Suponemos que la duración es en minutos, así que convertimos la hora de inicio a minutos
        hora_inicio = dia['Hora_inicio'].split(':')
        duracion_total += int(hora_inicio[0]) * 60 + int(hora_inicio[1])
    # Calcular la duración promedio
    dias_semana = len(rutina['dias_semana'])
    duracion_promedio = duracion_total / dias_semana
    # Mostrar los resultados
    print(f"Usuario {rutina['usuario_id']}:")
    print(f"Ejercicios realizados: {ejercicios_realizados}")
    print(f"Duración promedio: {duracion_promedio} minutos")

def main():
    # Conexión a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
    channel = connection.channel()
    # Nombre de la cola a la que deseas suscribirte
    nombre_cola = 'rutinas'
    # Declarar la cola
    channel.queue_declare(queue=nombre_cola)
    # Configurar la función de callback
    channel.basic_consume(queue=nombre_cola, on_message_callback=callback, auto_ack=True)
    # Iniciar el consumo de mensajes
    print("Esperando mensajes. Para salir, presiona CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
