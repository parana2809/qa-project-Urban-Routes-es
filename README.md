   1.	Título:
Suite de Pruebas Automatización de pruebas de la aplicación Urban Routes, proceso completo de pedir un taxi.

   2. Introducción
Este proyecto contiene pruebas automatizadas diseñadas para verificar la funcionalidad de la aplicación Urban Routes, específicamente el proceso completo de pedir un taxi. Las pruebas cubren desde la configuración de la dirección hasta la confirmación de la asignación de un conductor. El objetivo es garantizar que todas las funcionalidades clave de la aplicación funcionen correctamente y cumplan con los requisitos establecidos.
El diseño modular del proyecto permite una fácil mantenibilidad y escalabilidad, separando los localizadores, métodos y pruebas en archivos independientes. Esto asegura que el código sea claro, reutilizable y siga las mejores prácticas de automatización de pruebas.

   3.	Descripción:

Este proyecto automatiza las pruebas unitarias para pedir un taxi. Se enfoca en validar, cada una de las siguientes pruebas: 
1- Configurar la dirección 
2- Seleccionar la tarifa Comfort.
3- Rellenar el número de teléfono.
4- Agregar una tarjeta de crédito
5- Escribir un mensaje para el controlador.
6- Pedir una manta y pañuelos.
7- Pedir 2 helados.
8- Aparece el modal para buscar un taxi.
9- Esperar a que aparezca la información del conductor en el modal

   4. Descripción:

•	Clonar Repositorio: qa-project-Urban-Routes-es
•	Configurar WebDriver

   5. Estructura del Proyecto
•	README: Documentación del proyecto
•	helpers: Dependencias del proyecto
•	data: Datos de prueba (direcciones, números de teléfono, etc.)
•	UrbanRoutesLocators: Localizadores de elementos de la página.
•	UrbanRoutesMethods: Métodos para interactuar con los elementos de la página.
•	UrbanRoutesTestcases: Pruebas funcionalidad de pedir un taxi

   6. Tecnologías Utilizadas
•	Python : Lenguaje de programación utilizado para escribir las pruebas automatizadas.
•	Selenium : Framework de automatización utilizado para interactuar con la interfaz de usuario de la aplicación web. Las siguientes funcionalidades específicas de Selenium se utilizan en este proyecto:
•	WebDriverWait y expected_conditions: Para manejar esperas dinámicas y garantizar que los elementos estén listos antes de interactuar con ellos.
•	Keys: Para simular acciones del teclado, como presionar la tecla TAB para cambiar el enfoque.
•	ElementClickInterceptedException: Para manejar excepciones cuando un elemento no es cliclable debido a superposiciones u otros problemas.
•	Pytest : Framework de pruebas utilizado para organizar y ejecutar las pruebas.
•	WebDriver : Herramienta utilizada para controlar el navegador durante las pruebas (por ejemplo, ChromeDriver).