#Simple OCR server

This OCR server runs on Tesseract and flask

[link to Flask!](http://flask.pocoo.org/)

[link to Tesseract!](https://github.com/tesseract-ocr/tesseract)


## Walkthrough of how Engine works!

1. Once in the app folder run - python executable.py.
	* A message will come up to open a web browser and go to url http://http://127.0.0.1:5000/
	  ![Welcome Message](https://github.com/ralle123/ocr/blob/master/images/Capture1.PNG)
2. When address is reached the welcome page will come up.
		![Welcome Page](https://github.com/ralle123/ocr/blob/master/images/Capture2.PNG)
3. Once Image has been selected we can get the text from the image or get the orientation from the text.
		![Welcome Page](https://github.com/ralle123/ocr/blob/master/images/Capture3.PNG)
4. This is an example of what the text conversion option looks like. English language is selected in option.
		![Welcome Page](https://github.com/ralle123/ocr/blob/master/images/Capture4.PNG)
5. This is an example of what the text orientation looks like.
		![Welcome Page](https://github.com/ralle123/ocr/blob/master/images/Capture5.PNG)

		| Result 	| Explanation                    	|
		|--------	|--------------------------------	|
		| 0      	| Image is in the right position 	|
		| 180    	| Image is upside down           	|   