from flask import current_app

def testing():
    print('from testing DEBUG : %s' % current_app.config["DEBUG"])
    