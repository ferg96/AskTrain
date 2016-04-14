
#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('inputString')

print searchterm