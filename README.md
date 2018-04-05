Cody please be aware that I couldn't get this to upload to heroku.

(venv3) avargas@avargas-VirtualBox:~/Thinkful/flask_hello_world$ heroku local
[WARN] No ENV file found
21:59:47 web.1   |  [2018-04-04 21:59:47 +0000] [15376] [INFO] Starting gunicorn 19.7.1
21:59:47 web.1   |  [2018-04-04 21:59:47 +0000] [15376] [INFO] Listening at: http://0.0.0.0:5000 (15376)
21:59:47 web.1   |  [2018-04-04 21:59:47 +0000] [15376] [INFO] Using worker: sync
21:59:47 web.1   |  [2018-04-04 21:59:47 +0000] [15380] [INFO] Booting worker with pid: 15380
21:59:47 web.1   |  [2018-04-04 21:59:47 +0000] [15380] [ERROR] Exception in worker process
21:59:47 web.1   |  Traceback (most recent call last):
21:59:47 web.1   |    File "/usr/local/lib/python2.7/dist-packages/gunicorn/arbiter.py", line 578, in spawn_worker
21:59:47 web.1   |      worker.init_process()
21:59:47 web.1   |    File "/usr/local/lib/python2.7/dist-packages/gunicorn/workers/base.py", line 126, in init_process
21:59:47 web.1   |      self.load_wsgi()
21:59:47 web.1   |    File "/usr/local/lib/python2.7/dist-packages/gunicorn/workers/base.py", line 135, in load_wsgi
21:59:47 web.1   |      self.wsgi = self.app.wsgi()
21:59:47 web.1   |    File "/usr/local/lib/python2.7/dist-packages/gunicorn/app/base.py", line 67, in wsgi
21:59:47 web.1   |      self.callable = self.load()
21:59:47 web.1   |    File "/usr/local/lib/python2.7/dist-packages/gunicorn/app/wsgiapp.py", line 65, in load
21:59:47 web.1   |      return self.load_wsgiapp()
21:59:47 web.1   |    File "/usr/local/lib/python2.7/dist-packages/gunicorn/app/wsgiapp.py", line 52, in load_wsgiapp
21:59:47 web.1   |      return util.import_app(self.app_uri)
21:59:47 web.1   |    File "/usr/local/lib/python2.7/dist-packages/gunicorn/util.py", line 352, in import_app
21:59:47 web.1   |      __import__(module)
21:59:47 web.1   |    File "/home/avargas/Thinkful/flask_hello_world/hello_world.py", line 1, in <module>
21:59:47 web.1   |      from flask import Flask
21:59:47 web.1   |  ImportError: No module named flask
21:59:47 web.1   |  [2018-04-04 21:59:47 +0000] [15380] [INFO] Worker exiting (pid: 15380)
21:59:47 web.1   |  [2018-04-04 21:59:47 +0000] [15376] [INFO] Shutting down: Master
21:59:47 web.1   |  [2018-04-04 21:59:47 +0000] [15376] [INFO] Reason: Worker failed to boot.
21:59:47 web.1   Exited with exit code 3


This is the error that I was getting. I googled all that I could to see if I could get it to work.

