from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from Content.models import App
from Profile.models import Profile






from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from Profile.models import Profile



class FirstNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'cover', 'category', 'biography', 'birthdate', 'gender', 'account_type', 'privacy','root', 'url']



#Getting Username and Password{"C = as Capital letter"}
#======================================================
class Post(ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input bg-secondary','placeholder':'Title'}),label=False)
  discription = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input bg-secondary','placeholder':'Discription'}),label=False)
  category = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input bg-secondary','placeholder':'Category'}),label=False)
  thumbian = forms.ImageField(widget=forms.FileInput(attrs={'class':'uk-input bg-secondary','placeholder':'Thubian'}),label=False)
  video = forms.FileField(widget=forms.FileInput(attrs={'class':'uk-input bg-secondary','placeholder':'Video'}),label=False)
  caption = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input bg-secondary','placeholder':'Caption'}),label=False, required=False)
  

  class Meta:
    model = App
    fields = ('title','discription','category','thumbian','video','caption')


#Getting Username and Password{"C = as Capital letter"}
#======================================================
class SignUpForm(ModelForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input bg-secondary','placeholder':'Discription'}),label=False, required=False)
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input bg-secondary','placeholder':'Title'}),label=False, required=False)
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'uk-input bg-secondary','placeholder':'Password'}),label=False, required=False)

  class Meta:
    model = User
    fields = ('first_name','username','password',)


#Video UserimageUpdateView Form
#=============================
class UserimageUpdateView(ModelForm):
  picture = forms.ImageField(widget=forms.FileInput(attrs={'id':'image-input', 'class':'uk-input bg-secondary','placeholder':'Select new profile picture'}),label=False, required=False)

  class Meta:
    model = Profile
    fields = ['picture']

#Video UsercoverUpdateView Form
#=============================
class UsercoverUpdateView(ModelForm):
  usercover = forms.ImageField(widget=forms.FileInput(attrs={'class':'uk-input bg-secondary','placeholder':'Example: Entrepreneur'}),label=False, required=False)

  class Meta:
    model = Profile
    fields = ['usercover']

#Video CategoryUpdateView Form
#=============================
ProfileCategory_list = (
  ("", "None"),
  ("Entrepreneur", "Entrepreneur"),
  ("Advertising / Marketing", "Advertising / Marketing"),
  ("Agriculture", "Agriculture"),
  ("Internet Company", "Internet Company"),
  ("Web Designer", "Web Designer"),
  ("Artist", "Artist"),
  ("Arts and Entertainment", "Arts and Entertainment"),
  ("Automotive,Aircraft and Boat", "Automotive,Aircraft and Boat"),
  ("Beauty, Cosmetic and Personal Care", "Beauty , Cosmetic and Personal Care"),
  ("Commercial and Industrial", "Commercial and Industrial"),
  ("Education", "Education"),
  ("Finance", "Finance"),
  ("Food and Bevarage", "Food and Bevarage"),
  ("Hotel and Lodging", "Hotel and Lodging"),
  ("Legal", "Legal"),
  ("Local Service", "Local Service"),
  ("Media / News Company", "Media / News Company"),
  ("Medical and Health", "Medical and Health"),
  ("Non Governoment Organisation", "Non Governoment Organisation"),
  ("Nonprofit Organisation", "Nonprofit Organisation"),
  ("Public and Governoment Service", "Public and Governoment Service"),
  ("Real Estate", "Real Estate"),
  ("Science, Technology and Engineering", "Science, Technology and Engineering"),
  ("Shopping and Retail", "Shopping and Retail"),
  ("Sports and Recreation", "Sports and Recreation"),
  ("Travel and Transport", "Travel and Transport"),
  ("Armed Force", "Armed Force"),
  ("Charity Organisation", "Charity Organisation"),
  ("Community Service", "Community Service"),
  ("Country Club", "Country Club"),
  ("Environmental Conservation Organisation", "Environmental Conservation Organisation"),
  ("Labor Union", "Labor Union"),
  ("Private Members Club", "Private Members Club"),
  ("Religius Organization", "Religius Organization"),
  ("Social Club", "Social Club"),
  ("Sorority and Fraternity", "Sorority and Fraternity"),
  ("Sports Club", "Sports Club"),
  ("Youth Organization", "Youth Organization"),
  ("Art", "Art"),
  ("Book and Magazine", "Book and Magazine"),
  ("Music", "Music"),
  ("Show", "Show"),
  ("TV and Movies", "TV and Movies"),
  ("ATM", "ATM"),
  ("Campus Building", "Campus Building"),
  ("City Infrastructure", "City Infrastructure"),
  ("Landmark and Historical Places", "Landmark and Historical Places"),
  ("Locality", "Locality"),
  ("Meeting Room", "Meeting Room"),
  ("Outdoor Recreation", "Outdoor Recreation"),
  ("Public Toilet", "Public Toilet"),
  ("Religious Places of Worship", "Religious Places of Worship"),
  ("Residence", "Residence"),
  ("Brand", "Brand"),
  ("Cause", "Cause"),
  ("Just for Fun", "Just for Fun"),
  ("Public Figure", "Public Figure"),
  ("Model", "Model"),
  ("Writer", "Writer"),
  ("Advertising Agency", "Advertising Agency"),
  ("American Restaurant", "American Restaurant"),
  ("Aquarium", "Aquarium"),
  ("Aquatic Pet Store", "Aquatic Pet Store"),
  ("Arabian Restaurant", "Arabian Restaurant"),
  ("Arcade", "Arcade"),
  ("Art Gallery", "Art Gallery"),
  ("Asian Restaurant", "Asian Restaurant"),
  ("Automotive Window Tinting Service", "Automotive Window Tinting Service"),
  ("Baby & Children`s Clothing Store", "Baby & Children`s Clothing Store"),
  ("Bankruptcy Lawyer", "Bankruptcy Lawyer"),
  ("Beauty Store", "Beauty Store"),
  ("Beauty Supply Store", "Beauty Supply Store"),
  ("Betting Shop", "Betting Shop"),
  ("Big box Retailer", "Big box Retailer"),
  ("Bingo Hall", "Bingo Hall"),
  ("Boat Dealership", "Boat Dealership"),
  ("Boat Service", "Boat Service"),
  ("Bookstore", "Bookstore"),
  ("Boutique Store", "Boutique Store"),
  ("Cabinet & Countertop Store", "Cabinet & Countertop Store"),
  ("Car Dealership", "Car Dealership"),
  ("Car Wash", "Car Wash"),
  ("Career Counselor", "Career Counselor"),
  ("Carpet & Countertop", "Carpet & Countertop"),
  ("Casino", "Casino"),
  ("Chicken Joint", "Chicken Joint"),
  ("Cirus", "Cirus"),
  ("Clothing Brand", "Clothing Brand"),
  ("Clothing Company", "Clothing Company"),
  ("Clothing Store", "Clothing Store"),
  ("Coach", "Coach"),
  ("Collectible Store", "Collectible Store"),
  ("College / University Bookstore", "College / University Bookstore"),
  ("Comic Bookstore", "Comic Bookstore"),
  ("Commercial Equipment", "Commercial Equipment"),
  ("Commercial Truck Dealership", "Commercial Truck Dealership"),
  ("Computer Company", "Computer Company"),
  ("Computer Repair Service", "Computer Repair Service"),
  ("Condo Building", "Condo Building"),
  ("Contemporary Art Museum", "Contemporary Art Museum"),
  ("Contract Lawyer", "Contract Lawyer"),
  ("Copywriting Service", "Copywriting Service"),
  ("Corporate Lawyer", "Corporate Lawyer"),
  ("Cosmetics Store", "Cosmetics Store"),
  ("Costume Museum", "Costume Museum"),
  ("Credit Counseling Service", "Credit Counseling Service"),
  ("Criminal Lawyer", "Criminal Lawyer"),
  ("Currency Exchange", "Currency Exchange"),
  ("Dairy Farm", "Dairy Farm"),
  ("Dating Service", "Dating Service"),
  ("Day Care", "Day Care"),
  ("Decorative Art Museum", "Decorative Art Museum"),
  ("Design & Fashion", "Design & Fashion"),
  ("Design Museum", "Design Museum"),
  ("Divorce & Family Lawyer", "Divorce & Family Lawyer"),
  ("DUI Lawyer", "DUI Lawyer"),
  ("Elementary School", "Elementary School"),
  ("Emergency Roadside Service", "Emergency Roadside Service"),
  ("Endodontist", "Endodontist"),
  ("Engineering Service", "Engineering Service"),
  ("Environmental Consultant", "Environmental Consultant"),
  ("Escrow Service", "Escrow Service"),
  ("Exotic Car Rental", "Exotic Car Rental"),
  ("Financial Aid Service", "Financial Aid Service"),
  ("Financial Consultant", "Financial Consultant"),
  ("Financial Planner", "Financial Planner"),
  ("Fireplace Store", "Fireplace Store"),
  ("Fish Farm", "Fish Farm"),
  ("Fish Market", "Fish Market"),
  ("Fitness Trainer", "Fitness Trainer"),
  ("Food Bank", "Food Bank"),
  ("Forestry & Logging", "Forestry & Logging"),
  ("Franchise Broker", "Franchise Broker"),
  ("Fruit & Vegetable Store", "Fruit & Vegetable Store"),
  ("Furniture", "Furniture"),
  ("Garden Center", "Garden Center"),
  ("Gas Station", "Gas Station"),
  ("General Dentist", "General Dentist"),
  ("Geologic Service", "Geologic Service"),
  ("Glass Manufacturer", "Glass Manufacturer"),
  ("Golf Cart Dealership", "Golf Cart Dealership"),
  ("Golf Course & Country Club", "Golf Course & Country Club"),
  ("Golf Instructor", "Golf Instructor"),
  ("Governoment Service", "Governoment Service"),
  ("Gun Range", "Gun Range"),
  ("Gymnastics Center", "Gymnastics Center"),
  ("Hair Removal Service", "Hair Removal Service"),
  ("Hang Gliding Center", "Hang Gliding Center"),
  ("Hardware Store", "Hardware Store"),
  ("Hat Store", "Hat Store"),
  ("Health Food Store", "Health Food Store"),
  ("High School", "High School"),
  ("Historical Tour Agency", "Historical Tour Agency"),
  ("Hockey Field", "Hockey Field"),
  ("Home Goods Store", "Home Goods Store"),
  ("Home Inspector", "Home Inspector"),
  ("Hookah Lounge", "Hookah Lounge"),
  ("Horse Riding School", "Horse Riding School"),
  ("Horse-Drawn Carriage Service", "Horse-Drawn Carriage Service"),
  ("Horseback Riding Center", "Horseback Riding Center"),
  ("Hospital", "Hospital"),
  ("Hot Air Balloon Tour Agency", "Hot Air Balloon Tour Agency"),
  ("Hotel Bar", "Hotel Bar"),
  ("Housing & Homeless Shelter", "Housing & Homeless Shelter"),
  ("Ice Skating Rink", "Ice Skating Rink"),
  ("Independant Bookstore", "Independant Bookstore"),
  ("Information Bookstore", "Information Bookstore"),
  ("Internet Marketing Service", "Internet Marketing Service"),
  ("Irish Pub", "Irish Pub"),
  ("Jazz & Blues Club", "Jazz & Blues Club"),
  ("Jet Ski Rental", "Jet Ski Rental"),
  ("Jewelry & Watches Company", "Jewelry & Watches Company"),
  ("Jewelry & Watches Store", "Jewelry & Watches Store"),
  ("Jewelry & Wholesaler", "Jewelry & Wholesaler"),
  ("Juice Bar", "Juice Bar"),
  ("Junior High School", "Junior High School"),
  ("Kayak Rental", "Kayak Rental"),
  ("Kiteboarding Center", "Kiteboarding Center"),
  ("Korean Restaurant", "Korean Restaurant"),
  ("Laser Hair Removal", "Laser Hair Removal"),
  ("Laser Tag Center", "Laser Tag Center"),
  ("Law Enforcement Agency", "Law Enforcement Agency"),
  ("Library", "Library"),
  ("Limo Service", "Limo Service"),
  ("Live Music Venue", "Live Music Venue"),
  ("Livestock Farm", "Livestock Farm"),
  ("Loarn Service", "Loarn Service"),
  ("Local Business", "Local Business"),
  ("Lounge", "Lounge"),
  ("Machine Shop", "Machine Shop"),
  ("Marine Service Station", "Marine Service Station"),
  ("Market Research Consultant", "Market Research Consultant"),
  ("Marketing Agency", "Marketing Agency"),
  ("Masonry Contractor", "Masonry Contractor"),
  ("Massage School", "Massage School"),
  ("Maternity Clinic", "Maternity Clinic"),
  ("Media Agency", "Media Agency"),
  ("Medical Lab", "Medical Lab"),
  ("Medical School", "Medical School"),
  ("Modern Art Museum", "Modern Art Museum"),
  ("Motorcycle Dealership", "Motorcycle Dealership"),
  ("Motorcycle Repair Shop", "Motorcycle Repair Shop"),
  ("Music Lessons & Instruction School", "Music Lessons & Instruction School"),
  ("Nursing Home", "Nursing Home"),
  ("Nursing School", "Nursing School"),
  ("Obstertrician Gynocologist", "Obstertrician Gynocologist"),
  ("Occupational Safety and Health Service", "Occupational Safety and Health Service"),
  ("Occupational Therapist", "Occupational Therapist"),
  ("Office Supplies", "Office Supplies"),
  ("Opera House", "Opera House"),
  ("Oral surgeon", "Oral surgeon"),
  ("Organic Grocery Store", "Organic Grocery Store"),
  ("Orthodontist", "Orthodontist"),
  ("Osteopathic Doctor", "Osteopathic Doctor"),
  ("Otolaryngologist", "Otolaryngologist"),
  ("Painting Lessons", "Painting Lessons"),
  ("Parking Garage / Lot", "Parking Garage / Lot"),
  ("Party & Entertainment Service", "Party & Entertainment Service"),
  ("Paving & Asphalt Service", "Paving & Asphalt Service"),
  ("Pediatrician", "Pediatrician"),
  ("Pedicab Service", "Pedicab Service"),
  ("Performance Art Theatre", "Performance Art Theatre"),
  ("Periodontist", "Periodontist"),
  ("Pest Control Service", "Pest Control Service"),
  ("Pet Groomer", "Pet Groomer"),
  ("Pet Sitter", "Pet Sitter"),
  ("Photography Museum", "Photography Museum"),
  ("Photographer", "Photographer"),
  ("Physical Therapist", "Physical Therapist"),
  ("Plumbing Service", "Plumbing Service"),
  ("Pool & Billiard Hall", "Pool & Billiard Hall"),
  ("Pop-Up Shop", "Pop-Up Shop"),
  ("Portable Building Service", "Portable Building Service"),
  ("Portable Toilet Rental", "Portable Toilet Rental"),
  ("Poultry Farm", "Poultry Farm"),
  ("Pregnancy Care Center", "Pregnancy Care Center"),
  ("Private Plane Charter", "Private Plane Charter"),
  ("Psychotherapist", "Psychotherapist"),
  ("Pub", "Pub"),
  ("Race Track", "Race Truck"),
  ("Real Estate Agency", "Real Estate Agency"),
  ("Recreational Vehicle Dealership", "Recreational Vehicle Dealership"),
  ("Recycling Center", "Recycling Center"),
  ("Religious Bookstore", "Religious Bookstore"),
  ("Religious Center", "Religious Center"),
  ("Rent to Own Store", "Rent to Own Store"),
  ("Reptile Pet Store", "Reptile Pet Store"),
  ("Restaurant Supply Store", "Restaurant Supply Store"),
  ("Retail Company", "Retail Company"),
  ("RV Rental", "RV Rental"),
  ("Sake Bar", "Sake bar"),
  ("Scooter Rental", "Scooter Rental"),
  ("Scuba Instructor", "Scuba Instructor"),
  ("Sightseeing Tour Agency", "Sightseeing Tour Agency"),
  ("Speakeasy", "Speakeasy"),
  ("Specialty Crocery Store", "Specialty Crocery Store"),
  ("Sports Bar", "Sports Bar"),
  ("Sugaring Service", "Sugaring Service"),
  ("Sunglasses & Eyewear Store", "Sunglasses & Eyewear Store"),
  ("Taxidermist", "Taxidermist"),
  ("Textile Museum", "Textile Museum"),
  ("Threading Service", "Threading Service"),
  ("Tiki Bar", "Tiki Bar"),
  ("Trade School", "Trade School"),
  ("Traffic School", "Traffic School"),
  ("Trailer Dealership", "Trailer Dealership"),
  ("Trailer Rental", "Trailer Rental"),
  ("Visual Arts", "Visual Arts"),
  ("Waxing Service", "Waxing Service"),
  ("Wig Store", "Wig Store"),
  )


class CategoryUpdateView(ModelForm):
  category = forms.ChoiceField(choices = ProfileCategory_list, widget=forms.Select(attrs={'class':'uk-select','placeholder':'Example: Entrepreneur'}),label=False, required=False)

  class Meta:
    model = Profile
    fields = ['category']

#Video BioUpdateView Form
#=============================
class BioUpdateView(ModelForm):
  bio = forms.CharField(widget=forms.Textarea(attrs={'class':'uk-textarea','placeholder':'Example: Entrepreneur'}),label=False, required=False)

  class Meta:
    model = Profile
    fields = ['bio']

#Video WebsiteUpdateView Form
#=============================
class WebsiteUpdateView(ModelForm):
  website = forms.CharField(widget=forms.URLInput(attrs={'class':'uk-input','placeholder':'www.Streame.io'}),label=False, required=False)

  class Meta:
    model = Profile
    fields = ['website']
