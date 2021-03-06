from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_start(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("Lists", self.browser.title)
        self.fail("End of test")
        
if __name__=="__main__":
    unittest.main(warnings='ignore')
    
