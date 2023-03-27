## Modelo-controlador-vista (MVC) -> Patrón de arquitectura de software, separa los datos y la lógica de una aplicación.

- Modelo: Es la representación de la información con la cual el sistema opera, por lo tanto gestiona todos los accesos a dicha información, tanto consultas como actualizaciones, implementando también los privilegios de acceso que se hayan descrito en las especificaciones de la aplicación (lógica de negocio).

- Controlador: Responde a eventos (usualmente acciones del usuario) e invoca peticiones al ‘modelo’ cuando se hace alguna solicitud sobre la información (por ejemplo, editar un documento o un registro en una base de datos). También puede enviar comandos a su ‘vista’ asociada si se solicita un cambio en la forma en que se presenta el ‘modelo’, por tanto se podría decir que el ‘controlador’ hace de intermediario entre la ‘vista’ y el ‘modelo’.

- Vista: Presenta el ‘modelo’ (información y lógica de negocio) en un formato adecuado para interactuar (usualmente la interfaz de usuario) por tanto requiere de dicho ‘modelo’ la información que debe representar como salida.


# What does init.py?
Se utliza para inicializar paquetes de Python. 
package/
    __init__.py
    archivo1.py
    archivo2.py
    archivo3.py
    subpackage/
        __init__.py
        submodulo.py
