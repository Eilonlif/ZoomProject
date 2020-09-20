import WhatsappListener as WatLis
import Listener as Lis
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36")
options.add_argument("user-data-dir=/Users/eilonlif/Library/Application Support/Google/Chrome/")
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)


WatLis.joinZoomMeeting(driver, "מגניבים")

print(Lis.devices())
Lis.listen(4, 3)  # Recommended sensitivity: 3.5 - 4.5 seconds, Recommended adjustment time 2 - 5 seconds

