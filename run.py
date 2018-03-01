#! /usr/bin/env python
from app import app
#app.run(sudo service postgresql start )
app.run(debug=True,host="0.0.0.0",port=8080)
