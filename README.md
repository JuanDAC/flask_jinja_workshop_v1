# REST API

- interface \ la conexión funcional entre dos sistemas
- cacheable
- stateless
  <br> <br> <br> <br> <br> <br>
  <br> <br> <br> <br> <br> <br>
  <br> <br> <br> <br> <br> <br>

# Dominio

- 129.214.322:8080 -> mi-tienda-bonita.com
  <br> <br> <br> <br> <br> <br>
  <br> <br> <br> <br> <br> <br>
  <br> <br> <br> <br> <br> <br>

# PATH / ROUTE / EndPoint

| products             | user           |
| :------------------- | :------------- |
| /products            | /user/         |
| /products/categories | /user/settings |

<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>

# PATH OPERATIONS

| METHOD / OPERATION | user                                          |
| :----------------- | :-------------------------------------------- |
| GET                | Trae informacion                              |
| POST               | Envia informacin                              |
| PUT                | Actualiza Informacion                         |
| DELETE             | Elimina la informacion                        |
| PATCH              | Actualiza parcialmente la informacion         |
| HEAD               | Trae informacion sin cuerpo                   |
| CONECT             | Establece un puente hacia el servidor         |
| OPTIONS            | Trae los path operations hábiles del endpoint |
| TRACE              | Observar y traza detalles de la peticion      |

<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>

# Handler of PATH operations

```python3
@app_views.route('/', methods=["GET"])
def index():
    return 'hello world'
```

<br> <br> <br> <br> <br> <br>

## PATH operation decorator

```python3
@app_views.route('/', methods=["GET"])
```

<br> <br> <br> <br> <br> <br>

## PATH operation function

```python3
def index():
    return 'hello world'
```

<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>

# Dynamic ROUTE or PATH Parameter

| product      | user          |
| :----------- | :------------ |
| /product/786 | /profile/6498 |
| /product/984 | /profile/0476 |
| /product/273 | /profile/5420 |

```python3
@app_views.route('/product/<int:product_id>')
def show_product(product_id = None):
    pass
```

<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>

<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>
<br> <br> <br> <br> <br> <br>

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install flask`
- `pip freeze`
- `export FLASK_APP=run.py`
- `export FLASK_DEBUG=1`

# flask_jinja_workshop_v1

```

```
