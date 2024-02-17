# Note
In order to run the bash file inside the `.py` file: inside the target dir and run `chmod +x file_name.sh` for example: `chmod +x delete.sh` to give the file authentication. But not applicable on win.

I wanted to create error handling message that could appear in popup window, but haven't success. My thought: could use backend js code or use bootstrap, but the current bootstrap I added and comment out is shown behind my nav bar and cannot show the X button to close it. So current version of error handling is now manual page to show error msg.

There are two modes for the application, one is website and two is webview. To use the webview, uncomment `import webview`, `window = webview.create_window('Mapping', app)` and `webview.start()` inside `server.py` file.

This is a pure Flask app, only contains html and py file because considering my day job's computer has a strict data leackage protection and fire wall that ban some of the website like bootstrap so in windows version, I don't use bootstrap but only html to style the navbar.

To convert web app to a desktop app, I use pyinstaller and auto-py-to-exe on windows os system and **note** the auto-py-to-exe cannot work on mac.

# In Order To Run
python server.py