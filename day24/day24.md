The SQL query changed from WHERE username = ? AND password = ? to just WHERE username = ? because the password is now stored as a hash instead of plain text.

The plain password entered by the user cannot be directly compared with the stored hash in SQL. Instead, I first find the user by their username and get the stored hash from the database. Then I use check_password_hash() to check whether the password entered by the user matches that hash.

This makes the login system more secure because the actual password is not stored in the database.