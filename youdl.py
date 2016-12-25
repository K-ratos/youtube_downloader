#!/usr/bin/env python

from bs4 import BeautifulSoup
import dryscrape
from pytube import YouTube

print('youtubedownloader++++++++++++++++++')
sess = dryscrape.Session()
base_url = 'https://www.youtube.com/results?search_query='
search = input('Enter :')
search = search.split(" ")
inter= ''
for x in search:
	inter = inter + "+" + x
search = inter[1:]
print(search)
url = base_url+search

sess.visit(url)
r = sess.body()
soup = BeautifulSoup(r, 'html.parser')
links = soup.find_all('a' , class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ')
title = soup.find_all('a', class_='g-hovercard yt-uix-sessionlink spf-link ')
l = len(links)
print(len(title))
print("Please chose one")
for x in range(0,l):
	print (str(x+1)+'> '+links[x].string+'\n\tby'+title[x].string+'\n')
selec = int(input())
yt = YouTube('https://www.youtube.com/'+links[selec-1]['href'])
qual = yt.get_videos()
l = len(qual)
print('Please select one of the quality and type')
for x in range(0,l):
	print(str(x+1)+'> '+qual[x].extension + "  " + qual[x].resolution )
yt.set_filename(yt.filename)
selec = int(input())
video = yt.get(qual[selec-1].extension, qual[selec-1].resolution)
print('please wait your video is being downloaded')
video.download('/home/abhishek/Videos')
print('------thank you-----')