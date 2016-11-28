import os
from flask import render_template, request
from app import app
import subprocess
import re


APP_ROOT= os.path.dirname(os.path.abspath(__file__))

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    button_title = {'title1': 'Upload Image', 'title2':'Convert to text','title3':'Get text orientation'}
    return render_template('index.html',
                           button_title=button_title)

                           

def get_orientation(linktoimage):
    orientationdata = subprocess.check_output(["tesseract", linktoimage, "stdout", "-psm", "0"], stderr=subprocess.STDOUT)
    orientpattre = re.compile('Orientation in degrees: (\d+)')
    degrees = orientpattre.findall(orientationdata)
    degrees = degrees[0]
    #return degrees
    header='Text Orientation'
    button_title = {'title1': 'Upload File', 'titlex':'Go Back to main page'}
    return render_template('submissionsuccess.html',
                           button_title=button_title,title=header,info=degrees)
                    

@app.route('/submissionsuccess',methods=['GET','POST'])
def success():
    
    target=os.path.join(APP_ROOT,'images')
    
    if not os.path.isdir(target):
        os.mkdir(target)
    destination1="/".join([target,'file1.png'])  
    file1 = request.files['file1']
    file1.save(destination1)

    if request.method == 'POST':
        if request.form['submit'] == 'Convert to text':
            text1=subprocess.check_output(['tesseract',destination1,"stdout","-l","eng","-psm","4"])
            header='Text Conversion'
            button_title={'title1': 'Upload File', 'title2':'Submit', 'titlex':'Go Back to main page'}
            return render_template('submissionsuccess.html',button_title=button_title,title=header, info = text1)
        elif request.form['submit'] == 'Get orientation':
            orientation1=get_orientation(destination1)
            return orientation1            
        else:
            pass # unknown
