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

    'index_js': Bundle(
        'js/index.js',
        filters='jsmin',
        output='gen/index/index.js'),

    'index_css': Bundle(
        'css/index.css',
        filters='cssmin',
        output='gen/index/index.css')

}

assets = Environment(app)
assets.register(bundles)
