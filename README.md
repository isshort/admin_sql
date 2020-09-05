# admin_sql
git

    git add . 
    git pull origin master
    git commit -m "some commit"
    git push origin master
    git rm -r --cached .

Database
    
    drop database auction;
    create database auction character set utf8 collate utf8_unicode_ci;
    CREATE USER 'admin1234'@'localhost' IDENTIFIED BY 'admin1234';
    GRANT ALL PRIVILEGES ON *.* TO 'admin1234'@'localhost';
    FLUSH PRIVILEGES;
    
    // To import database from local *.sql file:
    mysql -u user_name -p database_name < dump.sql
    
    //To export database to local *.sql file:
    mysqldump -u user_name -p database_name > dump.sql
    
Virtualenv

    apt install virtualenv
    virtualenv -p python3 venv
    source venv/bin/activate
    
My Config

create file my.cnf in the project and edit this file
    
    [client]
    database = admin_sql
    user = user_name
    password = password
    default-character-set = utf8

Django

    pip3 freeze > requirements.txt.
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python manage.py migrate
    