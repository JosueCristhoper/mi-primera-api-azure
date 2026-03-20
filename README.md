# Backend con FastAPI: Despliegue Automatizado en Azure

Este repositorio contiene una API REST funcional desarrollada en **Python**, diseñada para demostrar la integración entre el desarrollo de software moderno y la computación en la nube.

## Descripción del Proyecto
El proyecto consiste en un servicio backend que expone diversos "endpoints" (puntos de acceso) para interactuar con el usuario. Ha sido optimizado para ejecutarse en entornos Linux dentro de la infraestructura de **Microsoft Azure**.

## Stack Tecnológico
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) - Elegido por su alto rendimiento y validación de datos automática.
* **Lenguaje:** Python 3.11.
* **Servidor Web:** Uvicorn (para ejecución local).
* **Plataforma Cloud:** Azure App Service.
* **CI/CD:** GitHub Actions (automatización de despliegues).

## Arquitectura y Flujo de Trabajo
El proyecto utiliza un modelo de **Despliegue Continuo**:
1. El código se desarrolla y prueba en un entorno local (**Localhost**).
2. Al realizar un `git push`, **GitHub Actions** activa un flujo de trabajo automático.
3. El código se empaqueta y se despliega en **Azure App Service**, actualizando la API pública en minutos sin intervención manual.



## Cómo probar la API
La API está disponible públicamente. Puedes interactuar con ella de dos formas:

### 1. Interfaz de Documentación (Recomendado)
Accede a la documentación interactiva estándar **OpenAPI**:
https://mi-api-cris123-etehgeepa4fbb7a0.westeurope-01.azurewebsites.net/docs

*Aquí puedes probar el endpoint `/saludar/{nombre}` usando el botón "Try it out".*

### 2. Acceso Directo
También puedes probar el endpoint de saludo dinámico directamente en el navegador:
`https://mi-api-cris123-etehgeepa4fbb7a0.westeurope-01.azurewebsites.net/saludar/TuNombre`

## Instalación Local (Para desarrolladores)
Si deseas replicar este proyecto localmente:

1. Clona el repositorio:

    ```bash
    git clone https://github.com/JosueCristhoper/mi-primera-api-azure.git
    ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar al servidor:

   ```bash
   uvicorn main:app --reload
   ```
   
## Autor
Desarrollado por **Josue Cruz** - https://www.linkedin.com/in/josuecristhoper/
