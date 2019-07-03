from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request,'home.html')

def count(request):
	data = request.GET['fulltextarea']
	word_list = data.split()
	print(word_list)
	list_len=len(word_list)
	print(list_len)
	word_dictionary = {}

	for i in word_list:

	 	if i in word_dictionary:

	 		# inncrease value of key by 1
	 		word_dictionary[i] +=1

	 	else:

	 		#initialize key value by 1
	 		 word_dictionary[i] = 1

	sorted_list = sorted(word_dictionary.items(),key = operator.itemgetter(1),reverse = True)

	return render(request,'count.html',{'fulltext':data,'words':list_len,'word_dict':sorted_list})



