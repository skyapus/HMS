#!/usr/bin/env python

'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import simplejson
import web
from mimerender import mimerender
from Runner import Runner

render_json = lambda **args: simplejson.dumps(args)

class DaemonHandler:
    @mimerender(
        default = 'json',
        json = render_json
    )
    
    def GET(self, cmd, daemonName):
        data = []
        data['cmd']=cmd
        data['daemonName']=daemonName
        dispatcher = Runner()
        return dispatcher.run(data)
    
    def POST(self, cmd):
        web.header('Content-Type','application/json')
        data = web.data();
        jsonp = simplejson.loads(data)
        jsonp['cmd']=cmd
        dispatcher = Runner()
        return dispatcher.run(jsonp)

