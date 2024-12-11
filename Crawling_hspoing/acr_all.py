import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# רשימת הקישורים שלך
urls = [
    "https://www.rami-levy.co.il/he/online/market/%D7%A4%D7%99%D7%A8%D7%95%D7%AA-%D7%95%D7%99%D7%A8%D7%A7%D7%95%D7%AA",
    "https://www.rami-levy.co.il/he/online/market/%D7%97%D7%9C%D7%91-%D7%91%D7%99%D7%A6%D7%99%D7%9D-%D7%95%D7%A1%D7%9C%D7%98%D7%99%D7%9D",
    "https://www.rami-levy.co.il/he/online/market/%D7%91%D7%A9%D7%A8-%D7%95%D7%93%D7%92%D7%99%D7%9D",
    "https://www.rami-levy.co.il/he/online/market/%D7%9E%D7%A9%D7%A7%D7%90%D7%95%D7%AA",
    "https://www.rami-levy.co.il/he/online/market/%D7%90%D7%95%D7%A8%D7%92%D7%A0%D7%99-%D7%95%D7%91%D7%A8%D7%99%D7%90%D7%95%D7%AA",
    "https://www.rami-levy.co.il/he/online/market/%D7%A7%D7%A4%D7%95%D7%90%D7%99%D7%9D",
    "https://www.rami-levy.co.il/he/online/market/%D7%A9%D7%99%D7%9E%D7%95%D7%A8%D7%99%D7%9D-%D7%91%D7%99%D7%A9%D7%95%D7%9C-%D7%95%D7%90%D7%A4%D7%99%D7%94",
    "https://www.rami-levy.co.il/he/online/market/%D7%A7%D7%98%D7%A0%D7%99%D7%95%D7%AA-%D7%95%D7%93%D7%92%D7%A0%D7%99%D7%9D",
    "https://www.rami-levy.co.il/he/online/market/%D7%97%D7%98%D7%99%D7%A4%D7%99%D7%9D-%D7%95%D7%9E%D7%AA%D7%95%D7%A7%D7%99%D7%9D",
    "https://www.rami-levy.co.il/he/online/market/%D7%90%D7%97%D7%96%D7%A7%D7%AA-%D7%94%D7%91%D7%99%D7%AA-%D7%95%D7%91%D7%A2-%D7%97",
    "https://www.rami-levy.co.il/he/online/market/%D7%97%D7%93-%D7%A4%D7%A2%D7%9E%D7%99-%D7%95%D7%9E%D7%AA%D7%9B%D7%9C%D7%94",
    "https://www.rami-levy.co.il/he/online/market/%D7%A4%D7%90%D7%A8%D7%9D-%D7%95%D7%AA%D7%99%D7%A0%D7%95%D7%A7%D7%95%D7%AA",
    "https://www.rami-levy.co.il/he/online/market/%D7%9C%D7%97%D7%9D-%D7%9E%D7%90%D7%A4%D7%99%D7%9D-%D7%95%D7%94%D7%9E%D7%90%D7%A4%D7%99%D7%99%D7%94-%D7%94%D7%98%D7%A8%D7%99%D7%94"
]

# אתחול ה-WebDriver של Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def get_category_name(url):
    # חילוץ שם הקטגוריה מה-URL
    category_name = url.split("/")[-1]
    # המרת הקידוד URL לפורמט קריא
    return category_name.replace("%D7%9C", "ל").replace("%D7%90", "א").replace("%D7%91", "ב")  # ודא שהקידוד מתפרק נכון


def fetch_and_save(url):
    # פתיחת האתר
    driver.get(url)

    # המתנה שהדף יטען
    time.sleep(5)  # המתנה של 5 שניות להבטחת הטעינה

    # חילוץ שמות המוצרים
    products_name = driver.find_elements(By.CSS_SELECTOR, "div.inner-text.mt-2")

    # יצירת רשימות של שמות המוצרים
    texts = [product.text.strip() for product in products_name]

    # חילוץ שם הקטגוריה מה-URL
    category_name = get_category_name(url)

    # יצירת שם הקובץ
    file_name = f'{category_name}.csv'

    # שמירת הנתונים לקובץ CSV
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name'])  # כותרת לעמודה של שם המוצר
        for text in texts:
            writer.writerow([text])  # שורה לכל מוצר

    print(f"Data saved for {category_name} in {file_name}")


# עבור על כל הקישורים ברשימה ושמור את הנתונים בקובץ CSV
for url in urls:
    fetch_and_save(url)

# סגירת הדפדפן
driver.quit()
