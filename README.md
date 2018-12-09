# Twisted Examples
These examples are from the Twisted Web in 60 Seconds samples: https://twistedmatrix.com/documents/current/web/howto/web-in-60/index.html

Most of these tutorials don't explain how to test them. Below are notes on how to test each tutorial.

### Tutorial 001
* To test this navigate to http://localhost:8888
* This could also be run with `twistd -n web --path C:\Workspace\twisted_examples\tmp`

### Tutorial 002
To test this navigate to http://localhost:8880

### Tutorial 003
To test this navigate to http://localhost:8880/temp1
To test this navigate to http://localhost:8880/temp2
To test this navigate to http://localhost:8880/temp3

### Tutorial 004
I couldn't get the encoding to work right for this one. To test use http://localhost:8880/2012

### Tutorial 005
For this one, if you enter an invalid year url, then the 404 error page should display

### Tutorial 006
Run http://localhost:8880/buy this should return the custom response code

### Tutorial 007
Go to http://localhost:8880/form. The specific request arg will be displayed

### Tutorial 008
Go to http://localhost:8880/form. The full content of the request will be displayed

### Tutorial 009
This uses an .rpy script. To test run this command in the directory of the .rpy script:
`twistd -n web --path .`
Then browse to http://localhost:8080/009_rpy_scripts.rpy

### Tutorial 010
Go to http://localhost:8880/test you should get a response in 5 seconds

### Tutorial 011
Same as 010 just uses a deferred instead

### Tutorial 012
Go to http://localhost:8880/test and close the browser tab, it should print that the request was cancelled

### Tutorial 013
Go to http://localhost:8880/test and close the browser tab, this will log that the request was cancelled

### Tutorial 014
Go to http://localhost:8880. Everything will be logged to /logs/access-logging-demo.log

### Tutorial 015
Go to http://localhost:8880

### Tutorial 016
I couldn't get this to work, not sure why

### Tutorial 017
Go to http://localhost:8880/show to display your session ID. You can also click the "i" in the browser address bar, then click Cookies, you should see the TWISTED_SESSION cookie.
You can open this page many times and the session ID should stay the same.
Go to http://localhost:8880/expire to expire the cookie. Now next time you go to show page you will get a new session ID.

### Tutorial 018
Go to http://localhost:8880/ The counter should keep incrementing.