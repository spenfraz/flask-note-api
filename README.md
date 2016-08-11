# flask-mysql-note-api


### 1. Download & Install Python (2.7.x)
  --> https://wiki.python.org/moin/BeginnersGuide/Download
  
### 2. Install pip & virtualenv 
  --> https://pip.pypa.io/en/latest/installing/
  
  --> (windows) http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/

### 3. Install MySQL (Start the Server and create initial user account)
  --> https://dev.mysql.com/doc/refman/5.7/en/installing.html
  
  --> https://dev.mysql.com/doc/refman/5.7/en/starting-server.html
  
  --> https://dev.mysql.com/doc/refman/5.7/en/windows-server-first-start.html
  
  --> https://dev.mysql.com/doc/refman/5.7/en/default-privileges.html
  
### 4. Initialize MySQL db and table
       Edit the LOAD DATA INFILE line with 
               the full path to note.csv
               
       Login to MySQL commandline shell/prompt 
       $ mysql -u <username> -p <password>
       
       Run note.sql
       $ source /full/path/to/note.csv
       
       Exit the MySQL shell
       $ exit
       
### 5. Install Git
  --> https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
  
### 6. Clone this Repo & navigate into it
       $ git clone https://github.com/spenfraz/flask-note-api.git
       $ cd flask-note-api
       
### 7. Create virtualenv
       $ virtualenv venv
      
### 8. Activate virtualenv & Install from requirements.txt
       $ . venv/bin/activate
              (OR)
     ( $ source venv/bin/activate )
       $ pip install -r requirements.txt
       
### 9. Edit the 
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password>@localhost/notesdb'
                line. (line 7, in note-server-json.py) 
                
### 10. Run the flask app!
       (virtualenv is activated & current working directory is flask-note-api/)
       $ python note-server-json.py
      
### 11. Test it Out!

        curl -i http://localhost:5000/notes/api/v1/notes

        curl -i -H "Content-Type: application/json" -X POST -d '{"title":"title","body":"body"}' http://localhost:5000/notes/api/v1/add

      
