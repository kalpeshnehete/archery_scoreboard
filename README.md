# archery_scoreboard

1]  Clone the project by the command : git clone https://github.com/kalpeshnehete/archery_scoreboard.git

2]  After cloning you need to create a virtual environment to isolate the project and to prevent depedndencies conflict.

3]  Now start the virtual environment on terminal and run the command : pip install -r "requirements.txt" 
    This command makes sure that you install all the libraries and packages required to run the project .
   
4]  After install the libraries and packages we need to run our server .
    Use : manage.py runserver
    Once you run this command and the server is running , open your browser and enter url : localhost:8000
   
5]  You can see our project is running . 
    This project is used to manage the scores of teams during a tournament . 
    This application was made to manage the score sof 2 teams having 2 players each and 5 rounds in  Archery Tournament .
 
6]  To set or edit no of round you can enter url and login as admin : localhost:8000/admin
    Enter username : kalpesh
    Enter password : 1234
    Once you are logged in you can edit the ROUNDS , TEAMS , PLAYERS , SCORES .
    
7]  Now get back to the url: localhost:8000/addteam
    Here add TEAMS and  PLAYERS names.
    
8}  NOW go on url : localhost:8000/addscore
    Here you can add SCORES of the PLAYERS whith respect to there TEAMS .
    
9]  After adding scores go to the SCOREBOARD and you can see the SCORES of the TEAMS .
    
