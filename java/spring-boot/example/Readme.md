# Spring Boot Example


---

## Hello Spring Boot


`code`

```
src/main/java/mypkg/MyApp.java

src/main/java/mypkg/MyController.java

```


`run`

```
linux:~/example $ gradle bootRun
```


`test`

```
linux:~ $ curl http://127.0.0.1:8080/ 
```


---

## URLConf


`code`

```
src/main/java/mypkg/demo

src/main/java/mypkg/demo/DemoController.java

src/main/java/mypkg/demo/DemoService.java
```


`test`

```
linux:~ $ curl http://127.0.0.1:8080/demo/hey/abc/

linux:~ $ curl http://127.0.0.1:8080/demo/hi/?name=abc
```

---

## CRUD


`code`

```
src/main/java/mypkg/crud

src/main/java/mypkg/crud/Person.java

src/main/java/mypkg/crud/CrudService.java

src/main/java/mypkg/crud/CrudService.java
```


`test`

```
linux:~ $ curl --request POST --header 'content-type: application/json' --data '{"name": "abc", "age": 1}' http://127.0.0.1:8080/crud/

linux:~ $ curl http://127.0.0.1:8080/crud/

linux:~ $ curl http://127.0.0.1:8080/crud/1/

linux:~ $ curl -X PATCH -H 'content-type: application/json' -d '{"name": "xyz", "age": 2}' http://127.0.0.1:8080/crud/

linux:~ $ curl http://127.0.0.1:8080/crud/1/
```

---
