# author: Hayden Johnston
# github: hgjohn
# date: 07/11/2023
# description: Single entry-point to resolve import dependencies.

from app import app, create_table
from api import api

api.init_app(app)

if __name__ == '__main__':
    app.run()
    create_table()