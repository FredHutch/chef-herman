#!/usr/bin/env python
from flask import Blueprint,current_app
from flask.ext.hookserver import Hooks
#import pprint

repodata = {}
repodata['atombaby/congenial-happiness'] = {}
repodata['atombaby/congenial-happiness']['branch'] = 'master'

hookserver = Blueprint('hooks', __name__)
hooks = Hooks(url='/hooks')

@hookserver.route('/hooks', methods=['POST'])
@hooks.hook('push')
def queue_task():
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
    if reponame not in repodata:
        print( '{} is not a watched repository'.format( reponame ) )
        return "No Thanks"

    print( 'This is one of mine, checking commit' )

    if ref != 'refs/heads/{}'.format( repodata[reponame]['branch'] ):
        print( 'branch {} is not built by me'.format( ref ) )
        return 'No Thanks'

    print( 'Branch {} is the build-branch- building this commit'.format(ref) )

    #pp = pprint.PrettyPrinter()
    #pp.pprint(data)

    # Hand off to builder

    return 'Thanks'

