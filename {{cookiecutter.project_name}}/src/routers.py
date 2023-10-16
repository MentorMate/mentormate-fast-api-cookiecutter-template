{%- if cookiecutter.add_example_apps == True %}
from src.users.v1.routers import router as users_v1
from src.auth.jwt.v1.routes import router as jwt_v1
{% else %}
# Import your apps' routers here
{% endif -%}

routers = [
    {%- if cookiecutter.add_example_apps == True %}
    jwt_v1,
    users_v1
    {% endif -%}
]
