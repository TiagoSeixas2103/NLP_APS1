# NLP_APS1

# Setup

## WARNING

If your python libraries were installed in a virtual environment, enter the environment first
```cmd
~HOME$ source venv/bin/activate
```
If they were not, you can ignore this warning 

## Database Setup

1 - Enter the NLP_APS1 folder, and run the Get_servant_name.py file (wait until it finishes)
```cmd
~NLP_APS1$ python3 Get_servant_name.py
```

2 - Run the Get_servant_description.py file (wait until it finishes, can take a few minutes)
```cmd
~NLP_APS1$ python3 Get_servant_description.py
```

3 - Move the file Data.csv to the tiagovs_nlp_aps1 folder, on the same level as setup.py 

## App Setup

1 - Enter the tiagovs_nlp_aps1 folder, and run (with sudo if necessary)
```cmd
~NLP_APS1/tiagovs_nlp_aps1$ docker build -t tiagovs_nlp_aps1 .
```

2 - Run (with sudo if necessary) the following command:
```cmd
~NLP_APS1/tiagovs_nlp_aps1$ docker run -d -p 2103:8888 tiagovs_nlp_aps1
```

3 - Access http://localhost:2103 to see if API is working (Note: localhost can be exchanged for the IP Address of the machine running the API)

# Testing

There were three case tests that needed testing to show if the API is capable of identifying characters according to words in their description.

1 - A test with 10 results as a return

http://localhost:2103/query?query=Mouth

2 - A test with less than 10 results

http://localhost:2103/query?query=Santa

3 - A test with non-obious results

http://localhost:2103/query?query=Smoke

In the case of the last test, it was expected for there to be many characters returned as a result instead of just the one, considering multiple characters on the game are comproved to smoke, but the result indicates that was not mentioned on their description, which was used to train the API.

Note: To build the docker container without executing the tests, remove the following line of the Dockerfile:
```docker
RUN pip install --no-cache-dir pytest && pytest --disable-warnings
```

# References

https://github.com/WeebMogul/Fate--Grand-Order-Servant-Data-Extractor (used as basis for web crawler)

https://github.com/tiagoft/fastapi_template (used as basis for API)

https://fategrandorder.fandom.com/ (used as source of data)

