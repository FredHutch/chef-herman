#!/usr/bin/env python
from flask import Blueprint, render_template
from herman.extensions import hook
from herman.extensions import redis_store

from datetime import datetime

hookhandler = Blueprint('hookhandler', __name__)

@hookhandler.route('/hooks', methods=['POST'])
@hook.hook('push')
def go(data, delivery):
    # Empty commits are most likely tags
    if len( data['commits']  ) == 0:
        print( "Skipping empty push to ref {}".format( data['ref'] ) )
        return 'Skipped'

    timestamp = datetime.today().strftime('%y-%m-%dT%H:%M:%S')
    #print "Data is {}".format( data )
    #print "Delivery is {}".format( delivery )

    commit, ref, name, url, default_branch = [
        data['head_commit']['id'],
        data['ref'],
        data['repository']['name'],
        data['repository']['url'],
        data['repository']['default_branch']
    ]
    print(
        'New push {} to branch {} in repo {}'.format(
            commit, ref, name
        )
    )
    redis_store.lpush(
        'herman',
        ( timestamp, commit, ref, name, url, default_branch )
    )

    return 'Thanks'

