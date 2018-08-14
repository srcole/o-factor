# The o-factor (the open science factor for journals; OF)
 
This project started in Neurohackademy, Seattle in August 2018 (http://neurohackademy.org/). The goal of the project is to give journals (but in the future also papers, and importantly, scientists) a score of how "open science" they are. We want to find a way to promote open science and give incentives for scientists and journals to do and support more open science.

We want to:
Measure open science across papers/journals (in the future also scientists/fields/institutions etc.)
Show open science trends across years and journals
Present the o-factor: a new measure for rank journals in terms of open-science
 
This project was initially inspired by Scott Cole's codesharing mini-project: https://github.com/srcole/codesharing 
And by the Code and Data Citation Counter: doi 10.5281/zenodo.1209095 link: https://github.com/softwaresaved/code-cite
O-Factor team
 

Contributors (ABC order):

Federico Adolfi - fedeadolfi@gmail.com

Rotem Botvinik-Nezer - rotemb9@gmail.com

Scott Cole - scott.cole0@gmail.com

Mikella Green - mikellagreen@gmail.com

Rosa Li - rosali920@gmail.com

Kristina Rapuano - kristinarapuano@gmail.com

Daniel Reznik - reznikda@gmail.com

Emily Wood - emilytwood@gmail.com
 
We first thought and discussed about the different components that should be included in the O-Factor. We decided to focus on four components: data sharing, code sharing, pre-registration and policies (e.g. preprints, open access http://www.oaspectrum.org, TOP guidelines https://cos.io/our-services/top-guidelines/ and more). Since taking policies into account required a lot of time and manual work, we decided to start from the other three components.
We scraped the scientific literature based on the pubmed database (available online at ftp.ncbi.nlm.nih.gov/pub/pmc/PMC-ids.csv.gz) with focus on journals related to biological, psychological and neuroscience research. 
 “Open-scienceness” was detected by scrapping articles’ full text for specific features (keywords) reflecting categories of data-sharing, code sharing and pre-registration. Output of such scrapping was a table in which each paper got either 1 or 0 for each openness category (three main categories in total). For example, if a paper mentioned data sharing, but not pre-registration and code sharing, it will get 1 in data sharing category, and 0 in pre-registration and code-sharing categories.
The current output table looks like that:


For each journal, o-factor was calculated by summing the total instances of “open-scienceness” in each paper (max 3 per paper) divided by the total number of papers published in a given year as summarized in the following formula:

O-Factor = # shared items / # sharable items

For example, if a certain journal published 100 papers in 2014, and 50 of these papers shared data, code and used preregistered reports, 10 of these papers shared only data and rest of the papers (40) shared nothing, the O-Factor for this journal will be
(50 * 3  +  10 * 1 + 40*0) / 100 = 160 / 100 = 1.6

In order to be able to compare between the O-Factor and impact factor, we calculated the O-Factor based on two years (for example, the O-Factor for 2018 was based on the number of shared items in 2016-2017, divided by the number of shareable items, which is the number of published papers during these years).
DISCLAIMER! It is important to note that current implementation of the OF has a few major limitations:
We scrapped only open access papers
We used only pubmed API
We did not filter for different article types (e.g., review papers, editorials, journal clubs for which the OF is not relevant)
We are also aware that the keywords we used can be dramatically improved
The codes were written and used during the 4 days of the hackaton, and should be more thoroughly tested and improved. 
We did not quantify the proportion of empirical articles published by each journal every year
 
Initially we scrapped ~35000 open access papers published in 1600 journals since 2006. After filtering out all the journals that had less than 200 papers, our analysis spanned ~31000 papers published by 216 journals. 
Data sharing
We computed the percent of papers which shared data (according to our keywords) in ten specific journals for which we had enough data, for the years 2008-2018 (until August 2018).

The following figure presents the proportion of data sharing in these journals over the years 2016-2018:

* Disclaimer: These figures are based on preliminary data with many limitations (see section 5 above), and should be considered accordingly! 

Code sharing
We computed the percent of papers which shared code (according to our keywords) in ten specific journals for which we had enough data, for the years 2008-2018 (until August 2018).

The following figure presents the proportion of code sharing in these journals over the years 2016-2018:
   
* Disclaimer: These figures are based on preliminary data with many limitations (see 5 above), and should be considered accordingly! 

O-Factor (OF) for 2018:
We computed the O-Factor of specific journals for the year 2018 (based on the years 2016-2017, see formule above). The range is 0-3.

* Disclaimer: These figures are based on preliminary data with many limitations (see section 5 above), and should be considered accordingly! 
Preliminary draft of a web app - https://o-factor.herokuapp.com/
Future plans:
To use other APIs (not just open access), filter only empirical papers and scrap more journals
To validate results – current tool is completely automatic and was not tested thoroughly
Add a tool to check if the data/codes are really shared (e.g. check that the links work)
Consider creating an O-Factor for scientists (o-index? Similar to h-index)
We thought about using the full text of the papers and training a model to differentiate between open and not open science papers (for each component or for all components together).
Promote this novel metric and cultural change in how science is evaluated and rewarded!

Acknowledgments: This project received a great conceptual, technical and emotional support from Neurohackademy mentors Kirstie Whitaker (kw401@cam.ac.uk), Tal Yarkony (tyarkoni@utexas.edu) and Ariel Rokem (arokem@gmail.com). 

If you want to contribute or have any questions, please don’t hesitate to approach us (rotemb9@gmail.com, reznikda@gmail.com). Further contact information is given in the contributors section.
