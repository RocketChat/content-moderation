# How to run the Python tests

In the command line from the project working folder ```./moderation``` execute the following command:

```
python -m unittest discover -s tests -p 'test_*.py' -v
or
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Sample output:
```
test_nsfw_images (test_inference.BasicTestCase) ... {'url': ['https://unsplash.com/photos/I2fStgjOyAg/download?force=true', 'https://unsplash.com/photos/-Hm_xIcYbUY/download?force=true&w=640']}
Retreiving Image...
 https://unsplash.com/photos/I2fStgjOyAg/download?force=true
image/jpeg
Time -  5.09s
--------------------------------------------------------------------------------
Retreiving Image...
 https://unsplash.com/photos/-Hm_xIcYbUY/download?force=true&w=640
image/jpeg
Time -  7.27s
--------------------------------------------------------------------------------
{'classification': 'nsfw'}


ok
Ran 4 tests in 18.636s

```