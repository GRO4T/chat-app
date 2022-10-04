# Dev notes
## MySQL setup
### Installation (yum)
https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/
```
wget https://dev.mysql.com/get/mysql80-community-release-el8-4.noarch.rpm
```
```
sudo rpm -Uvh mysql80-community-release-el8-4.noarch.rpm
```
```
sudo yum module disable mysql
```
```
sudo yum install mysql-community-server
```
```
sudo systemctl start mysqld
```
```
sudo systemctl status mysqld
```
```
sudo grep 'temporary password' /var/log/mysqld.log
```
```
mysql -uroot -p
```
```
ALTER USER 'root'@'localhost' IDENTIFIED BY '<new_pass>';
```
### Create database, user with priviliges
```
CREATE DATABASE chat_app;
-- '%' means allow connection from all hosts
CREATE USER 'developer'@'%' IDENTIFIED BY '<password>';
GRANT ALL ON chat_app.* TO 'developer'@'%'
FLUSH PRIVILIGES;
```
### Allow connections on port 3306 (for VMs on Oracle Cloud only)
1. virtual cloud network -> Security Lists -> add rule allowing TCP on port 3306
2. allow service mysql on VM's firewall
```
firewall-cmd --zone=public --add-service=mysql       --permanent
firewall-cmd --reload
```
### Create test table
```
USE chat_app;
CREATE TABLE user_profile (name VARCHAR(80));
INSERT INTO user_profile VALUES ('Michael Smith');
```

## Generate SSH public key from private key
Set proper permissions for private key
```
chmod 400 <private_key>
```
Create public key
```
ssh-keygen -f <private_key> -y > <public_key>
```
