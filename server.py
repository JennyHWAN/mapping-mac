from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
# Import the Maths package here
# import webview
import os
import subprocess
from subprocess import Popen, PIPE

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from mapping import process_excel
from mapping_sort import process_excel_sorted

ALLOWED_EXTENSIONS = set(['xlsx'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask("Mapping")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# window = webview.create_window('Mapping', app)

@app.route("/", methods = ['GET', 'POST'])
def render_index_page():
    # Write your code here
    # os.system('mkdir input')
    if os.listdir(os.getcwd() + '/input'):
        subprocess.Popen('./script.sh', shell=True)
    return render_template('index.html', files = os.listdir(os.getcwd() + '/example'), download=sorted(os.listdir('output')))

@app.route('/<name>')
def default_file(name):
    # return redirect(url_for('download_file', name=name))
    return send_from_directory('example', name)
    # return send_file(os.getcwd() + '/example' + name, as_attachment=True)

# @app.route("/data", methods = ['GET', 'POST'])
# def data():
#     if request.method == 'POST':
#         file = request.form['upload-file']
#         data = pd.read_excel(file)
#         return render_template('data.html', data=data.to_excel)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # subprocess.call('script.sh')
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != 'Table_A.xlsx' or file.filename != 'Table_B.xlsx':
            return render_template('500.html')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.xlsx'
            save_location = os.path.join('input', filename)
            file.save(save_location)
            files = os.listdir('./input')
            # print("Uploaded successfully")

            temp = []
            for subfile in files:
                if subfile.endswith('.xlsx'):
                    temp.append(subfile)
            if len(temp) == 2:
                output_file = process_excel()
                #return send_from_directory('output', output_file)
                return redirect(url_for('download'))
                # return redirect(url_for('index.html'))
                # render_template('index.html')
            # else:
            #     return redirect(url_for('index'))
    
    # files1 = os.listdir('example')
    return render_template('index.html', uploaded=os.listdir('input'), files = os.listdir(os.getcwd() + '/example'), download=os.listdir('output'))

# @app.route('/500')
# def error_handle():
#     return render_template('500.html')

@app.route('/upload/<upload_name>')
def upload_files(upload_name):
    return send_from_directory('input', upload_name)
    
@app.route('/upload/<name>')
def upload_default_files(name):
    return send_from_directory('example', name)

@app.route('/download')
def download():
    subprocess.Popen('./script.sh', shell=True)
    return render_template('index.html', download=sorted(os.listdir('output')), files = os.listdir(os.getcwd() + '/example'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('output', filename)

@app.route('/delete')
def delete_result():
    subprocess.Popen('./delete.sh', shell=True)
    return render_template('index.html', files = os.listdir(os.getcwd() + '/example'))

@app.route('/sort', methods=['GET', 'POST'])
def sort():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_location = os.path.join('input', filename)
            file.save(save_location)
            files = os.listdir('./input')

            temp = []
            for subfile in files:
                if subfile.endswith('.xlsx'):
                    temp.append(subfile)
            if len(temp) == 2:
                output_file = process_excel_sorted()
                return redirect(url_for('download'))
    return render_template('index.html', uploaded=os.listdir('input'), files = os.listdir(os.getcwd() + '/example'), download=os.listdir('output'))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    # webview.start()