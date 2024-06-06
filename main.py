import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

AMOZON_URL = "https://www.amazon.in/SHAYONAM-Portable-Rechargeable-Electric-Smoothies/dp/B0CWY2S1D1/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.37bad8da-0499-4510-838e-af217f0a67c4%3Aamzn1.sym.37bad8da-0499-4510-838e-af217f0a67c4&crid=17BLAN6DMBYP&cv_ct_cx=juicer%2Bblender&dib=eyJ2IjoiMSJ9.5anrDeqk0XjIA9FN5yaG8OPd_L-hGwDi8Mz9Y2MAaKDXBlhDppC1e-piNG1KabhweFAIB8tGtOEDkVzpYYrQpA.uuXRyln3V-kkcPv9SRkDo-UHTeYmCkRwp43ujmWAN5U&dib_tag=se&keywords=juicer%2Bblender&pd_rd_i=B0CWY2S1D1&pd_rd_r=586b6141-487e-4e56-bde1-f9a063161820&pd_rd_w=wrcbd&pd_rd_wg=wdvCZ&pf_rd_p=37bad8da-0499-4510-838e-af217f0a67c4&pf_rd_r=PHSWF0MC9JQD6G97NTKS&qid=1711181763&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=juicer%2Caps%2C198&sr=1-3-ced4eeeb-b190-41d6-902a-1ecb3fb8b7c4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language""": "en-US,en;q=0.9"
}


response = requests.get(AMOZON_URL, headers=headers)
amazon_html = response.text
soup = BeautifulSoup(amazon_html, "lxml")
product_title = soup.find("span", id="productTitle")
product_name = product_title.getText()
price = soup.find("span", class_="a-price-whole")
price_num = price.getText()

if float(price_num) < float(700):
    mesage = f"your desired product: {product_name} is now Rs.{price_num}"
    app_pass = "lavr wgdi vgse edck"
    host_email = "yashwanthg2509@gmail.com" # add your email to get email from
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(host_email, app_pass)
        connection.sendmail(
            from_addr=host_email,
            to_addrs="yashwanthkumar941@gmail.com", #add your email to get notify
            msg=f"Subject:Amazon Price Alert!\n\n{mesage}\n{AMOZON_URL}".encode("utf-8")
        )

