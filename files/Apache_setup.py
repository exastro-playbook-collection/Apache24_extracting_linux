import os
import json
import sys
import re

# main process
args = sys.argv
if (len(args) < 2):
    sys.exit(1)
path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]
filename1 = path + '/file/etc/httpd/conf/httpd.conf'
filename2 = path + '/command/0/stdout.txt'

log_config_module_flg = False
logio_module_flg = False
result_dict = {}

# paramete
para_list_dict={
    'VAR_Apache_ServerTokens':'ServerTokens',
    'VAR_Apache_ServerRoot':'ServerRoot',
    'VAR_Apache_KeepAlive':'KeepAlive',
    'VAR_Apache_ExtendedStatus':'ExtendedStatus',
    'VAR_Apache_User':'User',
    'VAR_Apache_Group':'Group',
    'VAR_Apache_ServerAdmin':'ServerAdmin',
    'VAR_Apache_ServerName':'ServerName',
    'VAR_Apache_UseCanonicalName':'UseCanonicalName',
    'VAR_Apache_DocumentRoot':'DocumentRoot',
    'VAR_Apache_DirectoryIndex':'DirectoryIndex',
    'VAR_Apache_AccessFileName':'AccessFileName',
    'VAR_Apache_TypesConfig':'TypesConfig',
    'VAR_Apache_MIMEMagicFile':'MIMEMagicFile',
    'VAR_Apache_HostnameLookups':'HostnameLookups',
    'VAR_Apache_ErrorLog':'ErrorLog',
    'VAR_Apache_LogLevel':'LogLevel',
    'VAR_Apache_CustomLog':'CustomLog',
    'VAR_Apache_ServerSignature':'ServerSignature',
    'VAR_Apache_AddDefaultCharset':'AddDefaultCharset',
    'VAR_Apache_EnableMMAP':'EnableMMAP',
    'VAR_Apache_EnableSendfile':'EnableSendfile'
    }
int_para_list_dict={
    'VAR_Apache_Timeout':'Timeout',
    'VAR_Apache_MaxKeepAliveRequests':'MaxKeepAliveRequests',
    'VAR_Apache_KeepAliveTimeout':'KeepAliveTimeout',
    'VAR_Apache_Listen':'Listen',
    'VAR_Apache_StartServers':'StartServers',
    'VAR_Apache_MinSpareServers':'MinSpareServers',
    'VAR_Apache_MaxSpareServers':'MaxSpareServers',
    'VAR_Apache_ServerLimit':'ServerLimit',
    'VAR_Apache_MaxRequestWorkers':'MaxRequestWorkers',
    'VAR_Apache_MaxConnectionsPerChild':'MaxConnectionsPerChild',
    'VAR_Apache_MinSpareThreads':'MinSpareThreads',
    'VAR_Apache_MaxSpareThreads':'MaxSpareThreads',
    'VAR_Apache_ThreadsPerChild':'ThreadsPerChild'
    }

# For parameter in httpd.conf
def genPara( para_name, content_name, line ):
    if (re.match( '\s*' + content_name + '\s+(.*)', line) != None):
        temp_var = line.rsplit(content_name, 1)[1]
        result_dict[para_name] = temp_var.strip()
def intPara( intPara_name, content_name, line ):
    if (re.match( '\s*' + content_name + '\s+(.*)', line) != None):
        intTemp_var = line.rsplit(content_name, 1)[1]
        if intTemp_var is not None:
            result_dict[intPara_name] = int(intTemp_var.strip())

if os.path.isfile(filename1):
    fo = open(filename1)
    alllines = fo.readlines()
    for line in alllines:
        line = line.strip()
        for temp in para_list_dict.keys():
            genPara( temp, para_list_dict[temp], line )
        for intTemp in int_para_list_dict.keys():
            intPara( intTemp, int_para_list_dict[intTemp], line )
        if '<IfModule log_config_module>' in line:
            log_config_module_flg = True
        if log_config_module_flg is True:
            if line.strip().startswith('LogFormat') and line.strip().endswith('combined'):
                strLogFormat = line.rsplit('LogFormat', 1)[1]
                result_dict['VAR_Apache_LogFormat'] = strLogFormat.strip()
                log_config_module_flg = False
        if '<IfModule logio_module>' in line:
            logio_module_flg = True
        if logio_module_flg is True:
            if line.strip().startswith('LogFormat') and line.strip().endswith('combinedio'):
                strLogFormatIo = line.rsplit('LogFormat', 1)[1]
                result_dict['VAR_Apache_LogFormat_IO'] = strLogFormatIo.strip()
                logio_module_flg = False
        if '<IfModule mpm_prefork_module>' in line:
            result_dict['VAR_Apache_MPMType'] = "prefork"
        if '<IfModule mpm_worker_module>' in line:
            result_dict['VAR_Apache_MPMType'] = "worker"
        if '<IfModule mpm_event_module>' in line:
            result_dict['VAR_Apache_MPMType'] = "event"
        result_dict['VAR_Apache_ServiceState'] = "stopped"
    fo.close()

if os.path.isfile(filename2):
    fo = open(filename2)
    alllines = fo.readlines()
    for line in alllines:
        if line.strip() == 'enabled':
            result_dict['VAR_Apache_ServiceAuto'] = 'yes'
        if line.strip() == 'disabled':
            result_dict['VAR_Apache_ServiceAuto'] = 'no'
    fo.close()
print (json.dumps(result_dict))