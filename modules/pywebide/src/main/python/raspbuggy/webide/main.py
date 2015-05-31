'''
Created on Apr 19, 2015

@author: bcopy
'''
import os
import cherrypy
import sys
import subprocess
import random
import time
import threading
import Queue
import tempfile

class ScriptMonitor(object):
    '''
    Monitors the script execution and updates result statuses
    '''
    
    def __init__(self):
        self.m_processInitialized = False
    
    def monitor(self, process):
        assert isinstance(process, subprocess.Popen)
        self.m_processInitialized = True
        self.m_process = process
        if(self.m_process.pid != None and self.m_process.poll() == None):
            print "Starting raspbuggy script process output polling..."
            self.m_stdoutQueue = Queue.Queue()
            self.m_stderrQueue = Queue.Queue()
            self.m_stdoutReader = AsynchronousFileReader(self.m_process.stdout, self.m_stdoutQueue)
            self.m_stdoutReader.start()
        else:
            print "Raspbuggy script process startup failed."
            
        
        
    def abort(self):
        print "Starting raspbuggy script process output polling..."
        if(self.m_processInitialized and self.m_process.poll() == None):
            self.m_process.terminate()
        self.m_processInitialized = False
 
    def isRunning(self):
        return (self.m_processInitialized and self.m_process.poll() == None)
        
    def getStdoutQueue(self):
        return self.m_stdoutQueue
        
    def getStderrQueue(self):
        return self.m_stderrQueue
        
    
class AsynchronousFileReader(threading.Thread):
    '''
    Helper class to implement asynchronous reading of a file
    in a separate thread. Pushes read lines on a queue to
    be consumed in another thread.
    '''
 
    def __init__(self, fd, queue):
        assert isinstance(queue, Queue.Queue)
        assert callable(fd.readline)
        threading.Thread.__init__(self)
        self._fd = fd
        self._queue = queue
 
    def run(self):
        '''The body of the thread: read lines and put them on the queue.'''
        for line in iter(self._fd.readline, ''):
            self._queue.put(line)
 
    def eof(self):
        '''Check whether there is no more content to expect.'''
        return not self.is_alive() and self._queue.empty()

class RaspbuggyService(object):
    def __init__(self):
        self.m_scriptMonitor = None
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def ping(self):
        return {"msg": "pong"}
        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def status(self):
        if(self.m_scriptMonitor != None):
            running = self.m_scriptMonitor.isRunning()
            retCode = self.m_scriptMonitor.m_process.poll()
            if(retCode == None):
                retCode = -1
            return {"running":running,"exitCode":retCode}
        else:
            return {"running":False,"exitCode":-1}
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def execute(self):
        scriptData = cherrypy.request.json
        if(self.m_scriptMonitor == None):
            self.m_scriptMonitor = ScriptMonitor()
        
        if(scriptData["scriptText"] == None):
            return {"success":False, "message":"Script contents undefined"}
        elif(self.m_scriptMonitor.isRunning()):
            return {"success":False, "message":"Script already running !"}
        else:
            # Write the script to a temporary file
            #scriptFile = tempfile.NamedTemporaryFile(prefix='raspbuggy-script-')
            scriptFile = open("/tmp/raspbuggy-script.py", "w")
            scriptFile.write(scriptData["scriptText"]+"\n")
            scriptFile.close()
            print "Executing script "+scriptFile.name+" ..."
            scriptProcess = subprocess.Popen(["python", scriptFile.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=128)
            
            if(scriptProcess.pid != None):
                self.m_scriptMonitor.monitor(scriptProcess)
                return {"success":True, "message": "Running script (pid "+str(self.m_scriptMonitor.m_process.pid)+")"}
            else:
                return {"success":False, "message": "Could not start up script"}
        
        
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def abort(self):
        return {"result":1}
    

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def tailStdOut(self):
        return  {"tail": "New line\nNew line"}


if __name__ == '__main__':
    WEBAPP_ROOT = os.getenv('RASPBUGGY_WEBAPP_ROOT',os.getcwd()+"/src/main/webapp")
    BLOCKLY_ROOT = os.getenv('BLOCKLY_ROOT',os.getcwd()+"/target/webjars/META-INF/resources/webjars/blockly/b35c0fbfa2")
    BOOTSTRAP_ROOT = os.getenv('BOOTSTRAP_ROOT',os.getcwd()+"/target/webjars/META-INF/resources/webjars/bootstrap/3.3.4")
    JQUERY_ROOT = os.getenv('JQUERY_ROOT',os.getcwd()+"/target/webjars/META-INF/resources/webjars/jquery/1.9.1")
    #print os.path.abspath(WEBAPP_ROOT)
    #print os.path.abspath(BLOCKLY_ROOT)
    cherrypy.quickstart(RaspbuggyService(), "/", 
        {
              '/':
              {
               'tools.staticdir.on': True,
               'tools.staticdir.dir': os.path.abspath(WEBAPP_ROOT)
              },
              '/blockly':
              {
               'tools.staticdir.on': True,
               'tools.staticdir.dir': os.path.abspath(BLOCKLY_ROOT)
              },
              '/bootstrap':
              {
               'tools.staticdir.on': True,
               'tools.staticdir.dir': os.path.abspath(BOOTSTRAP_ROOT)
              },
              '/jquery':
              {
               'tools.staticdir.on': True,
               'tools.staticdir.dir': os.path.abspath(JQUERY_ROOT)
              }                           
        })
