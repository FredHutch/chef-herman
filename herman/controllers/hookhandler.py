#!/usr/bin/env python
from flask import Blueprint, render_template
from herman.extensions import hook

hookhandler = Blueprint('hookhandler', __name__)

@hookhandler.route('/hooks', methods=['POST'])
@hook.hook('push')
def go(data, delivery):
    print "Data is {}".format( data )
    print "Delivery is {}".format( delivery )

    commit, ref, reponame = [
        data['head_commit']['id'],
        data['ref'],
        data['repository']['full_name']
    ]
    print(
        'New push {} to branch {} in repo {}'.format(
            commit, ref, reponame
        )
    )

    return 'Thanks'

