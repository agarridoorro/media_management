# Configuration of visual studio code

* Open new standard console 

```
Ctrl+Shift+P -> Terminal: Select Default Profile
```

* Install a virtual env for the project using the vs console and activate it

```
pip install virtualenv
virtualenv env
env\Scripts\activate.bat
```

* Install dependencies

```
pip install requests
pip install requests-cache
```

* Use in vs the new created venv

```
Ctrl+Shift+P -> Python: Select Interpreter
```