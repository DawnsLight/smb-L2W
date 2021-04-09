from smb.SMBConnection import SMBConnection
"""
Scripts to transfer files from linux server to Windows server
Author: cjiang
"""

"""
Test info
target server: 172.16.128.150
user:smb
password: Oxyachina11
"""
target_paths = {'data_P52': '/BACKUP_HANA_P52/data/P52', 'data_systemdb': '/BACKUP_HANA_P52/data/SYSTEMDB', 'log_P52':'Z:/BACKUP_HANA_P52/\log\DB_P52'}
source_paths = {'data_P52': 'Z:/BACKUP_HANA_P52/data/P52', 'data_systemdb': 'Z:/BACKUP_HANA_P52/data/SYSTEMDB'}

share_service_name = 'SMB_TEST'
share_path = '/ps'
Local = file = 'c:/test/ps'

conn = SMBConnection('smb', 'Oxyachina11', 'OXYA-CJIANG', 'OXYA-JAD', domain='JAD.com')
conn_status = conn.connect('172.16.128.150')
print(conn_status)

# list shares
share = conn.listShares()
share_list = []
for i in share:
    share_list.append(i.name)
if share_service_name  in share_list:
    print('Share Available')

# store files
with open('c:/test/test.txt', 'rb') as fd:
    file_size = conn.storeFile(share_service_name, share_path, fd)

# get file Attributes online
file_attribute_online = conn.getAttributes(share_service_name, share_path, timeout=30)
file_size_online = file_attribute_online.file_size
print('filesize on smb is {}'.format(file_size_online))


# retrieve files
#with open('c:/test/test.txt', 'wb') as fd:
#    file_attributes, file_size = conn.retrieveFile(share_service_name, share_path, fd)

# verify
if file_size == file_size_online:
    print('transfer ok')