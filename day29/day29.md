I was asked a quick revision on what ive done the past month.
1.Get is a request for a page. Post is submitting a data through a form input to the server here’s my information or data. 
2.render template does the job to render the template and flask does the job of looking into template to render its file ! 
3.So, {{ }} means, “give me this value”, while {% %} = “perform this template instruction.
4.request.args is for a get page to show what’s being search in the url. request.form is for a post page to store information inputed in the form.
5.placeholders is basically For security and preventing sql injections so placeholders are defined data
6.commit means save the progress without commit it would run but after that session its not saved
7.cause we need to check if the user has a key first before querying the database if not when it gets to querying the users role In the database a keyerror would come Up.
8. For security that’s the main reason if we don’t use the hash password anyone that has access to the data base can see what each users use as Password.
9. The user gets the page using request cause flask default method is get so When someone submits a login form the method is post the database is queried to check if username matches username and password matched hash password if not it’s invalid, so if it matches the login route checks either admin or student before redirecting it to its own page(dashboard)while the user visits other branches of the dashboard as long as the session remains true and it’s not broken the user is logged in else!!the use is logged and asked to  login again.