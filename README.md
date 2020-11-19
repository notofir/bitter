# bitter
Currently supports textual 01 files.
## How to run
First create the docker.
```
docker build -t bitter .
```
Either put you own binary.bin file in project, or create a binary file by running
```
docker run -p 5000:5000 -v $PWD:/var/app -t -i --rm bitter python binarize.py
```
Start the app
```
docker run -p 5000:5000 -v $PWD:/var/app -t -i --rm bitter
```