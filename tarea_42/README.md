# TAREA 42: HTML5 y video

## Requerimientos

Probado con Google Chrome. Basta con abrir el fichero index.html con el navegador. Para activar el micrófono hay que autorizar el acceso desde Google Chrome.

## Resumen

Para el reconocimiento de voz se ha utilizado la API del navegador. No he conseguido poder definir mis comandos. El navegador intenta reconocer el texto y devuelve la palabra en inglés que más se asemeje. Haciendo ruebas, he delimitado los comandos a 2: PLAY y STOP.

El codigo JS se encuentra en el fichero index.js. En este fichero primero se almacenan los elementos de la página Web relevantes, que se recuperan a través de su identificador.

Al botón de id play se le cambia el texto. COmienza con START y luego cada vez que se pulsa o se recibe un comando válida cambia a PLAY o PAUSE.

AL pulsar START, se activa el reconocimiento de texto (es necesario autorizarlo en el navegador), y se muestra el elemento de video y el que muestra los comandos.

Al reconocer un comando, se muestra en pantalla.

La página se ha maquetado con Bootstrap de forma sencilla. Los colores y el estilo están cogidos de una plantilla gratuita de Internet y sólo tienen pequeñas variaciones (gracias Omar Dsoky
https://freefrontend.com/css-headers-footers/)
