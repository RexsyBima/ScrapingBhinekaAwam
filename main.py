import requests
from bs4 import BeautifulSoup


def get_html(url: str):
    r = requests.get(url)
    return BeautifulSoup(r.content, "html.parser")


def get_page_max(soup: BeautifulSoup):
    soup: list[BeautifulSoup] = soup.find("ul", class_="pagination").find_all(
        "li", class_="page-item"
    )
    return int(soup[-1].find("a").get_text())


def get_products_items(soup):
    output = []
    item_products: list[BeautifulSoup] = soup.find_all(
        "div", class_="o_wsale_product_grid_wrapper position-relative h-100"
    )
    urls = [url.find("a")["href"] for url in item_products]
    url_text = "https://www.bhinneka.com/"
    for url in urls:
        fix_url = f"{url_text}{url}"
        output.append(fix_url)
    return output


if __name__ == "__main__":
    product_urls = []
    soup = get_html("https://www.bhinneka.com/jual?page=1&cari=iphone&order=")
    page_max = get_page_max(soup)
    for i in range(1, page_max + 1):
        soup = get_html(f"https://www.bhinneka.com/jual?page={i}&cari=iphone&order=")
        urls = get_products_items(soup)
        product_urls.extend(urls)
    for url in product_urls:
        soup = get_html(url)
        print(soup.find("div", id="product_details").find("h1").get_text())
