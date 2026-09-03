Why book.get("year") Can Be Safer
book["year"] will raise a KeyError if the "year" field does not exist in the dictionary.
book.get("year") is safer when a field might be missing because it returns None instead of causing an error. We can also provide a default value, such as "Unknown".