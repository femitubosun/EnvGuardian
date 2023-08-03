# EnvGuardian

A lightweight python environment variables validator
----

EnvGuardian is a lightweight Python library designed to ensure the presence of all required environment variables when
your project is executed, thereby minimizing the occurrence of runtime errors. This functionality proves particularly
valuable in scenarios where environment variables are specified in a .env or .env.example file, ensuring that all team
members possess up-to-date versions of the mandatory variables in .env files.

By leveraging EnvGuardian, your development team can rest assured that the necessary environment variables are
appropriately set before the project is run, safeguarding against common errors resulting from missing or incorrectly
configured environment variables. This proactive approach not only enhances the stability and reliability of your
applications but also promotes seamless collaboration among team members by streamlining the management of environment
configurations.

## Installation

`pip install envguardian`

## Usage

In your project root create an `Env.py` file and define a variable called `env_schema` like so

```py
# Env.py
from envguardian import Env

env_schema = {
    'DB_NAME': Env.string(),
    'ENVIRONMENT': Env.enum(['development', 'stage']),
    'PORT': Env.integer(),
    'DEBUG': Env.boolean(),
    'SOME_VAR': Env.float()
}
```

Somewhere else in your project, ideally, the entry point of your project, validate like so

```py
from envguardian import Env

Env.validate()
```

If the validation fails, expect something like this, `.validate()` will throw a `ValueError` Exception.

```shell

Exception: {'DB_NAME': '`None` is not a string', 'ENVIRONMENT': "`None` is not one of: ['development', 'stage']", 'PORT': '`None` is not an integer', 'SOME_VAR': '`None` is not a float'}

```

You can also use EnvGuardian to get environment variables with their correct type, provided you have defined them
in `env_schema` and the variable is present in environment variables.

```python
from envguardian import Env

print(type(Env.get('DEBUG')))

```

Output : `<class 'bool'>`
