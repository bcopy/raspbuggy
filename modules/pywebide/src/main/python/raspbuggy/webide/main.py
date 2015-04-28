'''
Created on Apr 19, 2015

@author: bcopy
'''
import os
import cherrypy

class HelloWorld(object):
    def hello(self):
        return "Hello from Raspbuggy !"
    hello.exposed = True

# [/]
# tools.staticdir.on = True
# tools.staticdir.dir = "/home/bcopy/workspace/raspbuggy/modules/pywebide/src/main/webapp"
# 
# [/favicon.png]
# tools.staticfile.on = True
# tools.staticfile.file = "/home/bcopy/workspace/raspbuggy/modules/pywebide/src/main/webapp/images/favicon.png"
# 
# [/blockly]
# tools.staticdir.on = True
# tools.staticdir.dir = "/home/bcopy/workspace/raspbuggy/modules/pywebide/target/webjars/META-INF/resources/webjars/blockly/b35c0fbfa2"

if __name__ == '__main__':
    print os.path.abspath(os.getcwd()+"/../../../webapp")
    print os.path.abspath(os.getcwd()+"/../../../../../target/webjars/META-INF/resources/webjars/blockly/b35c0fbfa2")
    cherrypy.quickstart(HelloWorld(), "/", 
        {
              '/':
              {
               'tools.staticdir.on': True,
               'tools.staticdir.dir': os.path.abspath(os.getcwd()+"/../../../webapp")
              },
              '/blockly':
              {
               'tools.staticdir.on': True,
               'tools.staticdir.dir': os.path.abspath(os.getcwd()+"/../../../../../target/webjars/META-INF/resources/webjars/blockly/b35c0fbfa2")
              }                           
        })
