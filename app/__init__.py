# from flask import Flask #, flash, redirect, url_for, session, request
from flask import Flask, flash, redirect, url_for, session, request
from config import Config
from flask_compress import Compress

# from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config) #I think this should work ? 
# bootstrap = Bootstrap(app)

compress=Compress(app)

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

from app import app
from app import routes, assets, ajax_handlers
