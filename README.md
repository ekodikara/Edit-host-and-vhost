# Edit-host-and-vhost
Edit host file and apache vhost file using python

You need to edit this few lines:

`def gencontent(host_name):
    new_line = '\r\n'
    http_vs = '<VirtualHost *:80>'+new_line+'\tServerAdmin yourname@gmail.com'+new_line+'\tDocumentRoot "/Applications/XAMPP/xamppfiles/htdocs/'+host_name+'"'+new_line + \
        '\tServerName  '+host_name+new_line+'\tServerAlias www.'+host_name+new_line + \
        '\tErrorLog "logs/'+host_name+'.error_log"'+new_line + \
        '\tCustomLog "logs/'+host_name+'.access_log" common' + \
    new_line+'</VirtualHost>'+'\r\n'
    return http_vs`

    
