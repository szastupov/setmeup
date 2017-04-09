# setmeup

## Usage

**setmeup.from_env** is a decorator tat takes a class and overrides its fields with data from environment variables. That's pretty much all API.

```python
import setmeup

# Define default settings
@setmeup.from_env
class Config:
    DEBUG = False
    PORT = 3000
    APP_ENV = "dev"
    ENABLE_HALLUCINATIONS = True

# Just use Config's fields
print(Config.DEBUG)
print(Config.PORT)

```

You can override any parameter via environment variable.
For example, setting `PORT=8080` before running the app sets Config.PORT to integer 8080. setmeup tries to use the same type as default value.

## Usage with Flask

Since it's all about plain objects, you can easily use setmeup to populate Flask config:

```python
import Config from yoursettings

app.config.from_object(Config)
```
