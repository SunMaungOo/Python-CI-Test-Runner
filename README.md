# Python CI Test Runner 

The docker container image which clone the project and execute the python file for testing purpose.

**Building**

First you have to clone the project

```
git clone https://github.com/SunMaungOo/Python-CI-Test-Runner.git
```
Then you have to build the image
```
cd /path/to/project
docker build -t sunmaungoo/ci-test-runner .
```

**Running**

You have to supply two parameter to the image.

-git  = The location of the repo

-file = Python file name to run

The -file flag already include the path of project. 

For example if you want to run the python file in top root folder,you just need to supply the python file name

```
-file = "top-root-file.py"
```

If you want to run the python file not located in top root folder,you need to file location starting from the projec file.

For example if you wanted to run the file in ``/project/tests/test1.py`` , you can set the file flag as shown below

``
-file = "tests/test1.py"
``

**Demo**

```
git clone https://github.com/SunMaungOo/Python-CI-Test-Runner.git
cd /path/to/project
docker build -t sunmaungoo/ci-test-runner .
docker run sunmaungoo/ci-test-runner -git "https://github.com/SunMaungOo/Ci-Test-Project" -file "main.py"
```


**Limitation**

1) Currently only support python 3
2) Currently only support public git repository
3) The requirements.txt must be in the top root folder.Other requirements.txt file are ignore.
