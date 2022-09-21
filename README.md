# Legacy-Tree
A website where users are able to post about their past relatives that have died recently or in the past. Users will be able to create a biography of the person of their choice where they can pay tribute to their memory by posting past stories of them with that person, achievements, funny anecdotes, etc. It will be up to the imagination of users.

# Installation guide:
**NOTE: if you have in the terminal you need to specify between python ^2.00 and ^3.00 then use the one that has the version ^3.00, normally is python3.**

Have python ^3.00 installed then run this commands:

    1. Install django: python -m pip install Django
    2. clone the repository on the folder that you prefer: git clone git@github.com:Ihosvani/Legacy-Tree.git
    3. Setting up the Database:
      1. Install pgAdmin: Acces this link https://www.pgadmin.org/download/ and download the app that is for your OS.
      2. Install postgrsSQL ^14.00: Acces this link https://www.postgresql.org/download/, choose your OS, download 
      and install, no password necessary and the port leave it deafult 5432
      3. In pgAdmin open the servers by clicking the dropdown arrow(on the left side of the app) and then right click 
      on login/group roles, and then create login/group role. In the field name put "admin", then acces the definition 
      tab and put "1234" as the password and for last acces the "priviliges" tab and make sure all of the fields are check.
      4. Then going back on the server dropdown menu right click Databases, then create Database. On the name 
      put "LegacyTreeDB" and the owner "admin".
      5. Goin back to the terminal run this command: pip install psycopg2.
    4. In the terminal and being at the root of the project(LegacyTree, where the manage.py file is) run this series of commands:
      1. python manage.py makemigations
      2. python manage.py migrate
      3. python manage.py runserver
