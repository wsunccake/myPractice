# Install package

```
linux:~/calculator_2 $ pyb install_build_dependencies
linux:~/calculator_2 $ pyb install_dependencies
```


# Run unit test

```
linux:~/calculator_2 $ pyb run_unit_tests
```


# Run calculator

## method 1.

```
linux:~/calculator_2 $ python run_server.py
```


## method 2.

```
linux:~/calculator_2 $ cd src/main/python
linux:~/calculator_2/src/main/python $ python manage.py runserver  
```


## method 3.

```
linux:~/calculator_2 $ cd src/main/python
linux:~/calculator_2/src/main/python $ env PYTHONPATH=. python calculator/__init__.py 
```
