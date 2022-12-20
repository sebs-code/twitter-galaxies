# Twitter Galaxies

Twitter Galaxies aims to map communties within Twitter in an intuative and visual way. 


## Categories
The app will take a Twitter account, and look at a number of different categories for each follower of that account. At present there are siz categories:

- Activity
- Political
- Literature
- Family
- Business
- Movies

For each category, a score between -1 and 1 will be given (e.g. Movies: 0.45), showing where they are on the spectum. -1 being least inclined, +1 being most inclined. 

## Limitations
- For now, these weightings are produced with dummy data, but future endhancements will use Machine Learning / Sentiment Analysis to create the scores. 
- For Now, this is limited to the 50 top accounts for the @FatTonysHQ Twitter account. We are waiting to be approved for 'enhanced' Twitter API access, which will allow us to pull any user's total followers. 

## Backend
The MVP backend is a simple Flask app that servers a JSON response. params for X, Y, and Z must be provided, and they must be existing categories.

## Getting started
To the the backend
1. Clone this repo onto your machine locally
2. Install Python 3.xx if your machine does not already have it
3. navigate to the directory in your terminal
4. pip3 install -r requirements.txt
5. cd src
6. flask --app app run

... The backend will now be running locally at http://127.0.0.1:5000. You can now make cals to the API (i.e. http://127.0.0.1:5000/?x=activity&y=political&z=movies)
