¿Cómo correr dos dockers secuencialmente y automáticamente que ejecuten transformaciones a un csv?


1. Abrir terminal Ubuntu e ingresar: sudo docker images ( Si requiere arrancar demonios ejecutar: sudo dockerd )

2. Aparece el nombre del repositorio con sus respectivas características, en este caso se debe ejecutar "prueba_csv". Ahora hay que ejecutar lo siguiente: sudo docker run -it prueba_csv . Si no surge ningún error, los archivos.py tienen que haberse ejecutado secuencialmente. En este caso, una vez ejecutado el run se tiene que haber creado el .csv con sus transformaciones.

3. Para comprobar que se ejecutó el contenedor, debemos ejecutar: sudo docker ps -a .