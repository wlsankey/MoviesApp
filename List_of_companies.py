import companies



Almar = companies.Company("plumbing / heating", 
"680 Madison Ave",
"New York", 
"","11238","New York",
"https://www.facebook.com/pages/Almar-Plumbing-Heating-Corp/143200015725831",
"http://media.merchantcircle.com/16422355/Logo8-24_full.jpeg")


print Almar.description
print Almar.street
print Almar.city
print Almar.suite
print Almar.zip
print Almar.state
print Almar.url
print Almar.logo

companies.Subcontractor.show_website(Almar)

"""
toy_story = media.Movie("Toy Story", 
"http://youtu.be/KYz2wyBy3kc", 
"http://2.bp.blogspot.com/_IYPZY2FVRrw/TPlwzrVFMbI/AAAAAAAAAJQ/155KF1TnSjs/s1600/Toy-Story-DVD95.jpg",
"A story of a boy and his toys that come to life."
)

	def __init__(self, company_description, company_address_street, company_address_city, company_address_suite, company_address_zip, company_address_state, company_url, company_logo):
"""