Simple OCR server

This OCR server runs on Tesseract and flask

Once the two previous dependencies have been installed application can simple be run the following way

 once in the folder run

 python executable.py

 you will get the message below, this means a webserver is running. All you have to do now if open a web browser and got to
 URl http://http://127.0.0.1:5000/

* Restarting with stat
* Debugger is active!
* Debugger pin code: 228-832-533
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Once on the main page,
* Select a file from your machine to process
* Once file has been selected, you have two options
	*Convert to text - this will convert to text the content of the image. Keep in mind we are using English language at this time
	*Get text orientation - this will return the orientation of the text on the image.
		for example - if we get 180 - this means the text is upside down
					  if we get 0   - this means the text is in the proper position