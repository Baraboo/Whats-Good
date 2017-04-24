from flask import Flask
from flask import render_template
from flask import request
from bs4 import BeautifulSoup
import re
import csv

default_path = "/home/grassknoted/Desktop/WhatsGood/Data/"

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

restaurant_id = ""
actual_rating = []  # Food, Service and Ambience
restaurant_website = ""
image = ""
cost = ""
all_reviews = []

@app.route('/', methods=['GET', 'POST'])
def entry_page():
    global restaurant_id
    if request.method == 'POST':
        restaurant_id = request.form['restaurant']
        getData(restaurant_id)
        return render_template('rest.html', name=restaurant_id, food_rating=actual_rating[0], service_rating=actual_rating[1],
        ambience_rating=actual_rating[2], r_food = actual_rating[3], r_service = actual_rating[4], r_ambience = actual_rating[5], imgsrc = image, cost = cost, review1 = all_reviews[0],
        review2 = all_reviews[1], review3 = all_reviews[2], review4 = all_reviews[3], review5 = all_reviews[4], review6 = all_reviews[5],
        review7 = all_reviews[6], review8 = all_reviews[7], review9 = all_reviews[8], review10 = all_reviews[9]  )
    else:
        return render_template('index.html')

def getData(restaurant_id):
    found = 0
    image_id = 0
    ii=0
    global all_reviews
    global image
    global cost
    global restaurant_website
    global actual_rating
    restaurant_id = restaurant_id.encode('utf-8')
    with open('/home/grassknoted/Desktop/WhatsGood/Data/Restaurants.csv', 'rb') as csvfile:
        reeder = csv.reader(csvfile)
        next(reeder, None)
        for row in reeder:
            if(row[0] == restaurant_id):
                image_id += 1
                restaurant_website = default_path + row[2]
                found = 1
                image_id = ii
            else:
                ii += 1
    if(found == 0):
        print("Sorry, we're unable to access the Restaurant's website right now! Please try again later!")

    print(restaurant_id, restaurant_website)
    html_document = BeautifulSoup(open(restaurant_website), 'lxml')	#Open <Restautant>.html with an lxml parser
    reviews_html = html_document.findAll('div', {'class':'rv_highlights__section pr10'}) # Find all divs in the HTML with class:'rv_highlights__section pr10'

    reviews = []

    for revs in reviews_html:
        reviews.append(revs)

    food = []
    firstChar = 1;
    item = ""
    overall_ratings = []
    overall_rating = ""

    for r in reviews:
        ratings = []
        rating = r.findAll('div', {'class':'block level-10'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-9'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-8'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-7'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-6'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-5'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-4'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-3'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-2'})
        ratings.append(len(rating))
        rating = r.findAll('div', {'class':'block level-1'})
        ratings.append(len(rating))
        actual_rating.append(max(ratings))

    spans = []
    rev = ""
    review_text = html_document.findAll('div', {'class':'fontsize13 ln18'})
    for a in review_text:
        rev = ""
        spans = a.findAll('span')
        for s in spans:
            s = s.text.strip()
            rev = rev +" "+ s
        actual_rating.append(rev)

    cost = html_document.find('div', {'class':'ttupper fontsize5 grey-text'}).parent
    cost = cost.text
    image = images[image_id]

    reviewz = html_document.findAll('div', {'class':'rev-text mbot0 '}) # Find all divs in the HTML with class:'rev-text mbot0 '

    review_count = 1
    for revs in reviewz:
    	all_reviews.append(revs.text)


images = [
'background-image : url("https://b.zmtcdn.com/data/pictures/6/58576/c948604f07e41b63430082a4c3a22eca.jpg?fit=around%7C200%3A200&crop=200%3A200%3B%2A%2C%2A&output-format=webp");background-size: cover!important; background-position: center center;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/54044_RESTAURANT_b3087c04bc909708516e2406a3679b72_c.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/58842_RESTAURANT_9647d1777aa8ab161c40577d2ccfc92d_c.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/52459_RESTAURANT_d002104237b43e2e591b6dfc19ebbcb8.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/59698_RESTAURANT_61d89f69fba5152953b81f8e2681f526.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/57833_RESTAURANT_9b7564ce58c323e9a54c2ff07611cf38.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/50943_RESTAURANT_2bd9e9241030df9f392ca022e7777a9d.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/50289_RESTAURANT_d437e89f1a64727f00ba138cc0ce83ba.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/56618_CHAIN_4a9df368fb0462f4c0487f0b6c0cb052.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/58430_RESTAURANT_obp3(3).jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/51038_CHAIN_9cd6c64e9541129d588946788db3cc61.png?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/59840_CHAIN_e19667d515d970b0225134cf3fad95c5.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/56464_RESTAURANT_9a00d0f5cffecead13535f2c4552beb2.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/57329_CHAIN_abf52c4db7aada2febdf66825b513286.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/52093_RESTAURANT_58db4190704fcfb7bb71338ea7d73f88.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/53590_CHAIN_671f59168320c7213254bdf59d1f8983.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/54308_CHAIN_4d04fba660d6cee6433b82e8bfb82671.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/18298235_RESTAURANT_800b57d758f493e1485db9900b262054.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/18426353_RESTAURANT_2256c3773fd08debab4d9a92c603c0c1.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/50420_RESTAURANT_0d1b47658844cb000632394a942a76a2.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/18353121_RESTAURANT_97510f213dcb3c5dd454ae9202199914.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/51705_RESTAURANT_de534ddcc5a4833fac9753422c8875c8.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/18162866_RESTAURANT_4f90f09d0253b10ddd05def9cf69090c.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/18385443_RESTAURANT_b77a89e25f076cfb93801d0fc0354a71.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/18430785_RESTAURANT_949e4d38cc184623feddfc7ba433d3e9.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/58882_RESTAURANT_47b9d564fe315303d61f14709eb2b410.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/54470_RESTAURANT_6648e227f069abe430e67b39d41d10b6_c.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/59132_RESTAURANT_cef63896c8bd28b30ea3dfe4d9d9bf30.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/50462_RESTAURANT_d3436b5d15805f3ad881f6a22df17f88.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/53264_RESTAURANT_9e17f308d171cb2da9a3485e2c09776b.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/53872_RESTAURANT_5a6fc4b4a9ddbf40504d6f0980433baf_c.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/58268_RESTAURANT_8a28cc30bf55c30305acb7010d924374.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/58567_RESTAURANT_3e8e7414ee2798bd39aa0248cc8740d0.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/54127_RESTAURANT_ad3ddf72e5cbf72c94c37e759cd76b04.jpg?output-format=webp"); opacity: 1;',
'background-image: url("https://b.zmtcdn.com/data/res_imagery/52628_RESTAURANT_afccc1b1c5b9e03cfbcf771cc276d15b_c.jpg?output-format=webp"); opacity: 1;',
]

if __name__ == '__main__':
    app.run()
