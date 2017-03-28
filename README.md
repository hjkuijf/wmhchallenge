# WMH Segmentation Challenge - MICCAI 2017
Example docker containers for the WMH Segmentation Challenge.

## Python example
A detailed description of the Python example is provided here: http://wmh.isi.uu.nl/example-python/. When this container is run according to the commands below, TEAM-NAME=example:python, YOUR-COMMAND=python&nbsp;/wmhseg_example/example.py, and TEST-ORIG/PRE are the input folders specified here: http://wmh.isi.uu.nl/data/

## Docker commands
Containers submitted to the challenge will be run with the following commands:

```
CONTAINERID=`docker run -dit -v [TEST-ORIG]:/input/orig:ro -v [TEST-PRE]:/input/pre:ro -v /output wmhchallenge/[TEAM-NAME]`
docker exec $CONTAINERID [YOUR-COMMAND]
docker cp $CONTAINERID:/output [RESULT-TEAM]
docker rm -v $CONTAINERID
```
