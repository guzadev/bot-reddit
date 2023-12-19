# Reddit Bot - Respuesta a Publicaciones y Comentarios

Este es un simple bot de Reddit desarrollado en Python que automatiza respuestas a publicaciones y comentarios en base a palabras clave especificadas. El bot consta de dos módulos: `respuesta_post.py` para responder a publicaciones y `marvin.py` para responder a comentarios.

## Configuración

Antes de ejecutar el bot, asegúrate de seguir estos pasos de configuración:

1. Instala las dependencias:

   ```bash
   pip install praw

Asegúrate de tener el archivo requirements.txt en tu proyecto y ejecuta:

    ```bash
    pip install -r requirements.txt

Crea una aplicación en Reddit Developer para obtener las credenciales (cliente_id, cliente_secreto, usuario_agente, nombre_de_usuario y contraseña).

Completa las variables de configuración en cada archivo (respuesta_post.py y marvin.py) con las credenciales y configuraciones específicas.

## respuesta_post.py
Este módulo busca palabras clave en los títulos de las publicaciones y responde automáticamente. Además, almacena los IDs de las publicaciones para evitar respuestas duplicadas.

Uso:
Ejecuta el script:

    ```bash
    python respuesta_post.py

## marvin.py
Este módulo busca palabras clave en los comentarios de las publicaciones y responde con comentarios aleatorios. También almacena los IDs de los comentarios para evitar respuestas duplicadas.

Uso:
Ejecuta el script:

    ```bash
    python marvin.py


# Notas:

* Asegúrate de cumplir con las políticas de uso de la API de Reddit para evitar sanciones.
* Personaliza las palabras clave y respuestas según tus necesidades en los archivos respuesta_post.py y marvin.py.
* Puedes configurar intervalos de tiempo para ejecutar los scripts mediante programación, según tus preferencias.

¡Disfruta de tu bot de Reddit! Si tienes alguna pregunta o mejora, no dudes en contribuir al proyecto.