
import csv
import matplotlib.pyplot as plt
import pandas
from wordcloud import WordCloud, STOPWORDS 

from textblob import TextBlob

## CSV with one column, rows of open ended survey responses, sentence structure

with open('survey_data.csv', encoding='UTF8') as csvfile:
	spamreader = csv.reader(csvfile)
	
	i = 0
	block_string = ""
	for line  in spamreader:
		#print(line)
		
		block_string += line[i].lower()
		
		
	stopwords = set(STOPWORDS)
	
	wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(block_string)
                
                
	plt.figure(figsize = (8, 8), facecolor = None) 
	plt.imshow(wordcloud) 
	plt.axis("off") 	
	plt.tight_layout(pad = 0) 
  
	plt.show() 
		
		
#	analysis = TextBlob(block_string)
#	print(analysis.sentiment)
#	
#	#for sentence in analysis.sentences:
#		#print(sentence, " " , sentence.sentiment)
#		#print("\n")
#	
#	#print(analysis.word_counts["portal"])
#	print(analysis.noun_phrases)
	
