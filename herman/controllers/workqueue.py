#!/usr/bin/env python
from flask import Blueprint, render_template
from herman.extensions import redis_store

workqueue = Blueprint('workqueue', __name__)

@workqueue.route( '/workqueue', methods=['GET'])
def show_queue():
    qlength = redis_store.llen( 'queue:work' )
    return render_template( 'workqueue.html', qlength=qlength )

