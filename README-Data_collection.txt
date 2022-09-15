Requirements: Python 3.7.12
              pandas 1.3.5
	      pytrends 4.8.0

TECH-ASSESSMENT for EonLabs - Data Collection


1. Description of my idea: Utilizing pytrends, it is very straightforward getting daily google trends data, but for our purposes we must grab specific weekly trend data as well. By extracting trend data from each year, we get weekly data, concatenating these years together gives us the trend data from 2015 until now. It is important to note that the weekly trend data is normalized yearly, and daily trend data is normalized monthly. 

	Note: To scale the data to be relative in the time window from 2015 til present, we would also require yearly trend data and monthly trend data. The process of scaling the data is the same as the one performed in the other part of my take-home assessment(Machine Learning Research Scientist), where I was given and monthly data, weekly, and hourly data. From my understanding this question did not require the final data to be given on a relative scale

2. I spent a little under an hour in total doing everything, about 45-50 minutes

3. I first researched a few ways of getting trend data using pytrends. This saved me some time since I was ready to write a function which concatenates the daily data for every month between now and January 2015, it turned out that there was a built in dailydata package in pytrends.

4. I settled on my current approach after reading through the assessment again to make sure that we did not need to put to output data on a relative scale. I also read the documentation on the dailydata package to make sure it would satisfy my needs.

5. To execute my program, make sure the requirements are installed and then run data_collection.py, it will generate two .csv files under the output folder containing the weekly data and the daily data from 2015 until present.

