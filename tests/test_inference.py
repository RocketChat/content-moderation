import requests, unittest, base64
from server.server import app

import requests
from io import BytesIO

serverUrl = "http://localhost:5000/predict"
class BasicTestCase(unittest.TestCase):
    #The below test, tests if the images that are NSFW doesn't pass..
    def test_nsfw_images(self):
        tester = app.test_client(self)
        payload = {
            'url': [
                "https://unsplash.com/photos/I2fStgjOyAg/download?force=true",
                "https://unsplash.com/photos/-Hm_xIcYbUY/download?force=true&w=640"
            ]
        }
        resp = tester.post(serverUrl, json = payload)
        self.assertEqual(resp.status_code, 200)
        print('\n')
    
    #The below test, tests if the images that are SFW passes uninterrupted..
    def test_sfw_images(self):
        tester = app.test_client(self)
        payload = {
            'url': [
                "https://unsplash.com/photos/I2fStgjOyAg/download?force=true",
                "https://unsplash.com/photos/IMecW34PSu8/download?force=true&w=640"
            ]
        }
        resp = tester.post(serverUrl, json = payload)
        self.assertEqual(resp.status_code, 200)
        print('\n')

    #The below test, tests if the media is anything other than images passes without preprocessing in the Flask API ..
    def test_otherMedia(self):
        tester = app.test_client(self)
        payload = {
            'url': [
                "https://vod-progressive.akamaized.net/exp=1593083494~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F771%2F17%2F428858003%2F1861623299.mp4~hmac=0ceb6514ccb475f8744b0f9d73ce25af132a4c654fdb41fdc50229213db6cd24/vimeo-prod-skyfire-std-us/01/771/17/428858003/1861623299.mp4?download=1&filename=production+ID%3A4646256.mp4",
                "https://youtu.be/OUFuaMj6z-w",
                "https://www.reddit.com/r/datascience/comments/hf5x2i/data_science_for_social_good/"
            ]
        }
        resp = tester.post(serverUrl, json = payload)
        self.assertEqual(resp.status_code, 500)
        print('\n')

    #The below test, tests the invalid/false urls pass uninterrupted...
    def test_invalidUrls(self):
        tester = app.test_client(self)
        payload = {
            'url': [
                "https://vod-progressive.akamd.net/exp=1593083494~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F771%2F17%2F428858003%2F1861623299.mp4~hmac=0ceb6514ccb475f8744b0f9d73ce25af132a4c654fdb41fdc50229213db6cd24/vimeo-prod-skyfire-std-us/01/771/17/428858003/1861623299.mp4?download=1&filename=production+ID%3A4646256.mp4",
                "https://youtu.be/OUFuaz-w",
                "https://www.redit.com/r/datasnce/comments/hf5x2i/data_science_for_social_good/"
            ]
        }
        resp = tester.post(serverUrl, json = payload)
        self.assertEqual(resp.status_code, 500)
        print('\n')

if __name__ == '__main__':
    unittest.main()