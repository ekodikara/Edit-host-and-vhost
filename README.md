# Edit-host-and-vhost
Edit host file and apache vhost file using python.
(Just For Fun!)

 - this is very basic python file for beginners to understand the usage and py sytax by making things easier with Python!

1. You need to edit these few lines first:

```
def gencontent(host_name):
    new_line = '\r\n'
    http_vs = '<VirtualHost *:80>'+new_line+'\tServerAdmin yourname@gmail.com'+new_line+ \
        '\tDocumentRoot "/Applications/XAMPP/xamppfiles/htdocs/'+host_name+'"'+new_line + \
        '\tServerName  '+host_name+new_line+'\tServerAlias www.'+host_name+new_line + \
        '\tErrorLog "logs/'+host_name+'.error_log"'+new_line + \
        '\tCustomLog "logs/'+host_name+'.access_log" common' + \
    new_line+'</VirtualHost>'+'\r\n'
    return http_vs
```

2. Next you need to edit the XAMPP file path

```
hostfile_path = '/etc/hosts'
httpd_vhost_path = '/Applications/XAMPP/etc/extra/httpd-vhosts.conf'
```

3. Run using terminal

`sudo python pyhost mysample.domain` 

    
