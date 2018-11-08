# dictionary + list 
novel = {
    "Name" : "Harry Potter" ,
    "Date" : 1997 , 
    "Characters" : ["Emma Watson", "Daniel Radcliffe", "Rupert Grint"] ,
    "Author" : "J. K. Rowling" ,
    "Nation" : "United Kingdom" 
}
for k, v in novel.items() :
    print (k, "-", v)