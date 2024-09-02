# NLP_APS1

# Setup

## WARNING

If your python libraries were installed in a virtual environment, enter the environment first

## Database Setup

1 - Enter the NLP_APS1 folder, and run the Get_servant_name.py file (wait until it finishes)

2 - Run the Get_servant_description.py file (wait until it finishes, can take a few minutes)

3 - Move the file Data.csv to the tiagovs_nlp_aps1 folder, on the same level as setup.py 

## App Setup

1 - Enter the tiagovs_nlp_aps1 folder, and run sudo docker build -t tiagovs_nlp_aps1 .

2 - Run sudo docker run -d -p 2103:8888 tiagovs_nlp_aps1

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

# References

https://github.com/WeebMogul/Fate--Grand-Order-Servant-Data-Extractor (used as basis for web crawler)

https://github.com/tiagoft/fastapi_template (used as basis for API)

