## The Backend is structured following the MVC pattern.

## Model-View-Controller (MVC) -> Software architecture pattern that separates data and application logic.

- Model: Represents the information that the system operates on, and manages all accesses to that information, including queries and updates, and also implements the access privileges described in the application specifications (business logic).

- Controller: Responds to events (usually user actions) and invokes requests to the 'model' when there is a request for information (for example, editing a document or a record in a database). It can also send commands to its associated 'view' if a change in the way the 'model' is presented is requested, so it could be said that the 'controller' acts as an intermediary between the 'view' and the 'model'.

- View: Presents the 'model' (information and business logic) in a suitable format for interaction (usually the user interface) and requires the 'model' to provide the information to be represented as output.


## What does init.py?
It is used to initialize Python packages.
package/
    __init__.py
    file1.py
    file2.py
    file3.py
    subpackage/
        __init__.py
        submodule.py