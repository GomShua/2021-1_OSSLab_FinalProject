# Sentiment Analyzing
## 1. What does this project do?
This project is python based web service application that allows users to analyze the bunch of sentences whether they generally contains positive or negative emotions. This project can be really useful when the person want to know the general tone of long paragraph.

## 2. How to use
You can simply clone the repository and start using web server running app.py. However, I used flask and vader-sentiment open-source packages. So, if you did not install these two packages, you will need to type these two command lines to install the packages.

Installing Flask:
    
    pip install flask

Installing Vader-sentiment:
    
    pip install vader-sentiment
    
If you successfully ran app.py, go to http://localhost:5000/ using any web browser. Then, you are ready to use sentiment analyzer. Scrolling down the website, you will be able to find the section that has textbox with button. Now, you can put sentences and press the button to use sentiment analyzer.

### etc.
If you want to know how does the sentiment analysis work, you can visit the vader-sentiment github repository. [LINK](https://github.com/cjhutto/vaderSentiment.git)

Get more information about flask package [here](https://palletsprojects.com/p/flask/).
