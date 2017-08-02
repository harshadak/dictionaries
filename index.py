def dictionaries(name, age, country, language):
    person = {"My name is ": name, "My age is": age, "My country of birth is": country, "My favorite language is": language}
    for key,data in person.iteritems():
        print key, data
        
dictionaries("Harshada", "27", "India", "Kannada")