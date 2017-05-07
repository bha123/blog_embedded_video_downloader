Hi All 

This program has been  developed inorder to download embedded videos from blog's.

It was initially developed inorder to download videos from a blog called "http://cksvforu.blogspot.in/" which my wife likes so much.

I hope other who are looking to download embedded videos from either websites / blogs can take advantage of this code. 


Code Walk Through:

The code will look for a text file which contains links pointing to the pages where you have to download vidoes. 
I have another code to download all the links of a blog. Which I will share in this repo soon. For now have the links of webpages/sites in the 
file named "Download_href_links.txt".


From the Download_href_links.txt file it will create another file called "Download-task.txt".This file will be used as temp file where it will copy all
the links of the Download_href_links.txt. This will delete one line after each download. This feature helps us to pause and resume downloads.

The code will have while loop which will look for line . If line is present in the Download-task.txt. It will continue inside the block. 

There are print statments in the code. Which i left as is . People can change it to debug / delete if they want to .

This lines will go throught request url . It will contact the url and get the response code. If response code is not 200 and number of retries is less than 5
the code will again contact the url if not it will cause the code to stop executing by throwing error.


After that it will create a name for the file by using endpoint and concatinating with the ".mp4".  The next code will open file with "WB" permission and saves video.

The for loop will continue until all the links are downloaded. 
Once it is done it will state "Download Completed" statment. 

It is written in a day and has got lot of room for improvment . Feel free to modify it and share it. 

Running the commands:

1. Make sure you have the Download_href_links.txt file in the same location where you have the file. Install python2.7 (https://www.python.org/downloads/release/python-2713/) in the system in order to run the file 


2. Run the below command to run the code.

   $ python embedded_blog_videos_downloader.py 

After that you will see the code downloading the videos in the directory "d_v\\". change it to "d_v/" in case of linux. 









