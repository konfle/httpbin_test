# Test Execution

---
One of the simplest ways to execute all tests is type:

`pytest -v .\test_post_and_get_httpbin.py` 

![](.\img\run.png)

If would you like to run a single test use pattern:

`pytest -v .\test_post_and_get_httpbin.py::{name of test}`

e.g. `pytest -v .\test_post_and_get_httpbin.py::test_post_data`

---

The second option is running test from code edit view:
![](.\img\run_1.png)

In that case you will be able to run a single test

---

### Reqirements:
pytest==6.2.5

requests==2.26.0

---

### ENVIRONMENT
If your environment does not meet requirements of this project you can install them manually by typing in IDE terminal:

`pip install pytest==6.2.5`

`pip install requests==2.26.0`

You can also visit [how to use requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html) 
web page
