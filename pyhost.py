import datetime
import sys


def copyto(source, dest):
    from shutil import copyfile
    backup_file = datetime.date.today().strftime('%Y_%m_%d_%I_%M')
    copyfile(source, dest+backup_file)


def gencontent(host_name):
    new_line = '\r\n'
    http_vs = '<VirtualHost *:80>'+new_line+'\tServerAdmin yourname@gmail.com'+new_line+'\tDocumentRoot "/Applications/XAMPP/xamppfiles/htdocs/'+host_name+'"'+new_line + \
        '\tServerName  '+host_name+new_line+'\tServerAlias www.'+host_name+new_line + \
        '\tErrorLog "logs/'+host_name+'.error_log"'+new_line + \
        '\tCustomLog "logs/'+host_name+'.access_log" common' + \
        new_line+'</VirtualHost>'+'\r\n'
    return http_vs


def append(hostname):
    hostfile_path = '/etc/hosts'
    httpd_vhost_path = '/Applications/XAMPP/etc/extra/httpd-vhosts.conf'
    copyto(hostfile_path, hostfile_path+'_backup_')
    f = open(hostfile_path, 'a')
    hotst_conent = '127.0.0.1    ' + hostname
    f.write(hotst_conent+'\r\n')

    copyto(httpd_vhost_path, httpd_vhost_path+'_backup_')
    fv = open(httpd_vhost_path, 'a')
    fv.write(gencontent(hostname))
    print('----------------------------------------httpd-vhost.conf--------------------------------------------\n')
    print gencontent(hostname)


def getparams(params):
    append(params)


def helpscreen():
    print('\n---------------- usage ----------------')
    print('sudo python pyhost.py [mysample.domain]')
    print('---------------------------------------\n')


if len(sys.argv) > 1:
    getparams(sys.argv[1])
else:
    print helpscreen()
# end of the program --
