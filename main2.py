import requests
from bs4 import BeautifulSoup
import pandas as pd  # gunakan library pandas

"""
result = requests.get("https://www.bhinneka.com/jual?cari=iphone")
# print(result.status_code)
# print(result.headers)
src = result.content
soup = BeautifulSoup(src, 'html.parser')

products = soup.find_all("div", "o_wsale_product_grid_wrapper position-relative h-100")

#membuat list kosong untuk menampung nama dan harga
product_name = []
price = []
final_output = []

#looping untuk mengambil data sekaligus cleaning data
for product in products :
    nama = product.find('a', 'text-primary text-decoration-none').get_text()
    harga = product.find('span','oe_currency_value').get_text().replace("Rp","").replace(".", "").replace(" ", "")
    
    product_name.append(nama)
    price.append(harga)

    output = {"name" : nama, "price" : harga}
    
    final_output.append(output)
    
#membuat dictionary
product_dict = {
'nama' : product_name,
'harga' : price
}

#print(output)

print(final_output)

# mengubah data dict menjadi dataframe pandas
df = pd.DataFrame(product_dict)
df.sort_values('harga', ascending=True)
print(df)

# mengubah dataframe menjadi csv
df.to_csv('bhinneka.csv', sep = ',')
"""

"""
def get_html(url):
    result = requests.get(url)
    src = result.content
    return src

def convert_to_bs4_obj(src):
    soup = BeautifulSoup(src, "html.parser")
    return soup

def scrape_looping(url,products_item):    
    for url in range(1, + 1):
        result = requests.get(f"https://www.bhinneka.com/jual?page={url}&cari=iphone&order=")
        parsing(products_item)
    save_to_csv()
    return result

def get_products_items(soup):
    item_products = soup.find_all("div", "o_wsale_product_grid_wrapper position-relative h-100")
    return item_products

def parsing(item_products):
    item_products = soup.find_all("div", "o_wsale_product_grid_wrapper position-relative h-100")
    final_output = []
    for product in item_products:
        nama = product.find('a', 'text-primary text-decoration-none').get_text()
        harga = product.find('span','oe_currency_value').get_text().replace("Rp","").replace(".", "").replace(" ", "")
        installment = product.find('span', class_ = "bmd-installment").get_text().replace("Cicilan Rp. ", "").replace("/bln", "").replace(".", "")
        location = product.find('div', class_ = "o_wsale_product_sub d-flex justify-content-between align-items-end pb-1").find('div', class_ = "d-flex flex-column").find('span', class_ = "bmd-installment").get_text().replace("\n", "").replace(" ","") # -> None.get_text()
        url = product.find('a', 'text-primary text-decoration-none')['href'].replace(" ", "")
        final_url = (f"https://www.bhinneka.com/{url}")
        output = {"Name" : nama, "Price" : harga, "Installment" : installment, "Location" : location, "URL" : final_url}
        final_output.append(output)
    return final_output

def save_to_csv(final_output):
    df = pd.DataFrame(final_output, index=range(1, len(final_output) + 1))
    print(df)
    df.sort_values('Price', ascending=True)
    df.to_csv('bhinneka.csv', sep = ',')


def scrape_looping(url):
    all_output = []
    
    for i in range(1, max_page + 1):
        result = requests.get(f"https://www.bhinneka.com/jual?page={i}&cari=iphone&order=")
        soup = convert_to_bs4_obj(result.content)
        item_products = get_products_items(soup)
        output = parsing(item_products)
        all_output.extend(output)
        
    save_to_csv()
    return result

if __name__ == "__main__":
    src = get_html("https://www.bhinneka.com/jual?order=list_price+desc&cari=iphone")
    soup = convert_to_bs4_obj(src)
    item_products = get_products_items(soup)
    final_output = parsing(item_products)
    looping = scrape_looping("https://www.bhinneka.com/jual?order=list_price+desc&cari=iphone")
    save_to_csv(final_output)

def scrape()`
    for url in urls:
        request.get(url)
        lakukan parsing
        dikonstruk jadi dictionary, lalu di masukan ke list output akhir
    save_to_csv 
    b
"""

"""
def parsing_inside(products_inside):
    item_products = soup.find_all("div", class_ = "js_product js_main_product mb-3")
    for product in item_products:
        installment2 = product.find("span", class_ = "oe_currency_value").get_text()
        estimation = product.find("div", class_ = "row product-data-row").find("div", class_ = "")
"""

"""
def get_html(url):
    result = requests.get(url)
    src = result.content
    return src

def convert_to_bs4_obj(src):
    soup = BeautifulSoup(src, "html.parser")
    return soup

def scrape_looping():
        

def get_products_items(soup):
    max_page = soup.find("ul", class_ = "pagination m-0")
    for i in range(1, page + 1):

        item_products = soup.find_all("div", "o_wsale_product_grid_wrapper position-relative h-100")
    return item_products

def parsing(item_products):
    final_output = []
    for product in item_products:
        nama = product.find('a', 'text-primary text-decoration-none').get_text()
        harga = product.find('span','oe_currency_value').get_text().replace("Rp","").replace(".", "").replace(" ", "")
        installment = product.find('span', class_ = "bmd-installment").get_text().replace("Cicilan Rp. ", "").replace("/bln", "").replace(".", "")
        location = product.find('div', class_ = "o_wsale_product_sub d-flex justify-content-between align-items-end pb-1").find('div', class_ = "d-flex flex-column").find('span', class_ = "bmd-installment").get_text().replace("\n", "").replace(" ","") # -> None.get_text()
        url = product.find('a', 'text-primary text-decoration-none')['href'].replace(" ", "")
        final_url = (f"https://www.bhinneka.com/{url}")
        output = {"Name" : nama, "Price" : harga, "Installment" : installment, "Location" : location, "URL" : final_url}
        final_output.append(output)
    return final_output

def save_to_csv(final_output):
    df = pd.DataFrame(final_output, index=range(1, len(final_output) + 1))
    print(df)
    df.sort_values('Price', ascending=True)
    df.to_csv('bhinneka.csv', sep = ',')


if __name__ == "__main__":
    src = get_html("https://www.bhinneka.com/jual?order=list_price+desc&cari=iphone")
    soup = convert_to_bs4_obj(src)
    item_products = get_products_items(soup)
    final_output = parsing(item_products)
    save_to_csv(final_output)
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_html(url):
    result = requests.get(url)
    src = result.content
    return src


def convert_to_bs4_obj(src):
    soup = BeautifulSoup(src, "html.parser")
    return soup


def get_products_items(soup):
    item_products = soup.find_all(
        "div", class_="o_wsale_product_grid_wrapper position-relative h-100"
    )
    return item_products


def parsing(item_products):
    final_output = []
    for product in item_products:
        nama = product.find("a", class_="text-primary text-decoration-none").get_text()
        harga = (
            product.find("span", class_="h6 mb-0")
            .find("span", class_="oe_currency_value")
            .get_text()
            .replace("Rp", "")
            .replace(".", "")
            .replace(" ", "")
        )
        installment = (
            product.find("span", class_="bmd-installment")
            .get_text()
            .replace("Cicilan Rp. ", "")
            .replace("/bln", "")
            .replace(".", "")
        )
        location = (
            product.find(
                "div",
                class_="o_wsale_product_sub d-flex justify-content-between align-items-end pb-1",
            )
            .find("div", class_="d-flex flex-column")
            .find("span", class_="bmd-installment")
            .get_text()
            .replace("\n", "")
            .replace(" ", "")
        )
        url = product.find("a", class_="text-primary text-decoration-none")[
            "href"
        ].replace(" ", "")
        final_url = f"https://www.bhinneka.com/{url}"
        output = {
            "Name": nama,
            "Price": harga,
            "Installment": installment,
            "Location": location,
            "URL": final_url,
        }
        final_output.append(output)
    return final_output


def scrape_product_details(product_url):
    src = get_html(product_url)
    soup = convert_to_bs4_obj(src)
    estimated_arrival_element = (
        soup.find("div", class_="js_product js_main_product mb-3")
        .find("div", class_="row product-data-row")
        .find("div", class_="col-sm-9")
        .find("span", id_="productHandlingTimeInformation")
        .get_text()
    )
    estimated_arrival = (
        estimated_arrival_element.text if estimated_arrival_element else None
    )
    return {"Est_Arrival": estimated_arrival}


def save_to_csv(final_output):
    df = pd.DataFrame(final_output, index=range(1, len(final_output) + 1))
    df.to_csv("bhinneka_iphone.csv", sep=",")


def scrape_bhinneka(base_url, max_pages):
    all_output = []
    for page_num in range(1, max_pages + 1):
        url = f"{base_url}&page={page_num}"
        src = get_html(url)
        soup = convert_to_bs4_obj(src)
        item_products = get_products_items(soup)
        output = parsing(item_products)
        all_output.extend(output)

    save_to_csv(all_output)

    for idx, product_data in enumerate(all_output, start=1):
        print(f"Product {idx} : {product_data}")


if __name__ == "__main__":
    base_url = "https://www.bhinneka.com/jual?order=list_price+desc&cari=iphone"
    max_pages = 3  # Change this to the desired number of pages to scrape
    scrape_bhinneka(base_url, max_pages)
