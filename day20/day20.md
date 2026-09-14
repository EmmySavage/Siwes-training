A GET form puts the submitted data in the URL, which is why I can see something like ?movie_title=Inception in the browser’s address bar.

A POST form sends the data in the request body instead, so it does not appear in the URL.

In Flask, I use request.args.get() to get data from a GET request and request.form.get() to get data from a POST form.

I think of GET as sending information through the URL, while POST sends it separately in the request.
A lot a lot honestly 
But we thank goodness cause hmmmmm….
 Firstly failed imports, used import requests instead import request!!!! secondly writing two return inside a function forgetting that a return ends the function and the remaining doesn’t run at all!!!!