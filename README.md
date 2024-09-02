# NLP_APS1

# Setup

## Database Setup

1 - Enter the tiagovs_nlp_aps1 folder, and run Get_servant_name.py (wait until it finishes)

2 - Run Get_servant_description.py (wait until it finishes)

3 - Make sure Data.csv is inside the tiagovs_nlp_aps1 folder, on the same level as setup.py 

## App Setup

1 - Enter the tiagovs_nlp_aps1 folder, and run docker build -t tiagovs_nlp_aps1 .

2 - Run docker run -d -p 2103:8888 tiagovs_nlp_aps1

3 - Access localhost:2103 to see if API is working