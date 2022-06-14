from flask_assets import Environment, Bundle
from app import app

bundles = {

    'base_js': Bundle(
        'js/base.js', 
        filters='jsmin',
        output='gen/base/base.js'),

    'base_css': Bundle(
        'css/base.css',
        'css/footer.css',
        'css/header.css',
        filters='cssmin',
        output='gen/base/base.css'),

    'light_mode_js': Bundle(
        'js/light_mode.js',
        filters='jsmin',
        output='gen/light_mode/light_mode.js'),

    'light_mode_css': Bundle(
        'css/light_mode.css',
        filters='cssmin',
        output='gen/light_mode/light_mode.css'),

    'dark_mode_js': Bundle(
        'js/dark_mode.js',
        filters='jsmin',
        output='gen/dark_mode/dark_mode.js'),

    'dark_mode_css': Bundle(
        'css/dark_mode.css',
        filters='cssmin',
        output='gen/dark_mode/dark_mode.css')

}

assets = Environment(app)
assets.register(bundles)
