PART 1(Installation):

You need to install the prereqs for running this Hello World Lab if not already here.

-update repositories of available packages to install. Use following command:

$sudo apt update

-install all minimal dependencies with following command:

$ sudo apt install python3-dev python3-pip pythn3-virtualenv sqlitebrowser

-use followiung :

$ python3 manage.py migrate

PART 2(Running Django)

-to run application you need to go and clone the following:

git clone "https://github.com/szczesniak10/HelloWorld.git"

-later you need to go into the directory where such was downloaded and into following:

/HelloWorld/newapp


-To run Server use:

$ python3 manage.py runserver


-To view json:
http://127.0.0.1:8000/Json

-To view HTML using template:

http://127.0.0.1:8000/sayHello
