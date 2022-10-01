# Dev notes
## MySQL setup
### Create database, user with priviliges
```
CREATE DATABASE chat_app;
-- '%' means allow connection from all hosts
CREATE USER 'developer'@'%' IDENTIFIED BY '<password>';
GRANT ALL ON 'chat_app'.* TO 'developer'@'%'
FLUSH PRIVILIGES;
```
### Allow connections on port 3306 (for VMs on Oracle Cloud only)
1. virtual cloud network -> Security Lists -> add rule allowing TCP on port 3306
2. allow service mysql on VM's firewall
```
firewall-cmd --zone=public --add-service=mysql       --permanent
firewall-cmd --reload
```
