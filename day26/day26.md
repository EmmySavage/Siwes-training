I  learnt how to create a database model using db.Model and define columns such as id, title, director, and available.

I learned that db.create_all() creates the database tables based on the models I define.

I also learned how to troubleshoot errors by checking the exact line where the error occurs and testing the database configuration separately.
I Misspelled the SQLALCHEMY_DATABASE_URI config key with incorrect capitalization, causing a RuntimeError                                                                                                                                                                                                                                                                                                                                                                                  For over 1 hour kept on checking line by line not knowing the error was from upper case and lower case usage…. 
How I solved them   I Compared the exact spelling character by character against the traceback and documentation, corrected it in both the config line and the debug print statement