results = []
cat = ["category-1", "category-2"]
for category in cat:
    querystring = {"htmlName":category,"countryCode":"US"}
    r = requests.request("GET", url, params=querystring)
 
    data = r.json()
    for product in data['pageData']['categoryData']['products']:
        site = {
            'name': product['product_name'],
            'website': product['product_url'],
            'category': category
        }
        results.append(site)
 
    df = pd.json_normalize(results)
    df.to_csv(category + '.csv', index=False)
