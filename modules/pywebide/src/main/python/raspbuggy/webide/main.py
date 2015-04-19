'''
Created on Apr 19, 2015

@author: bcopy
'''

import cherrypy

class HelloWorld(object):
    def hello(self):
        return "Hello from Raspbuggy !"
    hello.exposed = True

cherrypy.quickstart(HelloWorld(), "/", "/home/bcopy/workspace/raspbuggy/modules/pywebide/src/main/resources/cherrypy.cfg")

if __name__ == '__main__':
    pass