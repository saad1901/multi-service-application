import streamlit as st
import os
import time
from datetime import datetime
import pytz
import subprocess
from googletrans import Translator
import sqlite3
import platform
from pydub import AudioSegment
from pydub.playback import play

py_version = platform.python_version()
db_path = 'cns_practicals.db'

selection = st.sidebar.radio("select", ("files", "add a file","Python Compiler","music player","Translator",'CLI','Cloud Storage','add Images','Gallery'))
if selection == 'files':

    def create_login_history_table():
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS login_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login_time DATETIME
            )
        ''')
        conn.commit()
        conn.close()

    def log_login_time():
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        login_time = datetime.now(pytz.timezone('Asia/Kolkata'))
        cursor.execute('INSERT INTO login_history (login_time) VALUES (?)', (login_time,))
        conn.commit()
        conn.close()

    def get_last_login_time():
        conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = conn.cursor()
        cursor.execute('SELECT login_time FROM login_history ORDER BY id DESC LIMIT 1')
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    st.header('🚀Github FILES')

    passw = st.text_input('Enter Password', type="password")
    if passw == st.secrets["psd"]:    
        create_login_history_table()
        log_login_time()
        last_login_time = get_last_login_time()
        st.text(f'Last Login Time: {last_login_time}')

        def read_file_content(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        valid_extensions = ('txt','py','cpp','java','json','js','html','css','bat','c','kt')
        files = [''] + [file for file in os.listdir() if file.endswith(valid_extensions)]

        selected_file = st.selectbox('Select file', files)

        if selected_file:
            if selected_file != '':
                st.header(f"{selected_file}")
                content = read_file_content(selected_file)
                st.code(content, language='python')
            else:
                st.info("Select a Python file from the dropdown to view its content.")
        else:
            st.text("Please select a file from the dropdown.")
    elif passw != st.secrets["psd"] and passw != '' :
        st.error('wrong person !!')

elif(selection == "add a file"):
    # psd2 = "s"
    st.text("⚠️Note: The Files won't be stored in Github")
    st.text("they'll be only available in RAM untill App is running and cache isn't cleared")
    passwd = st.text_input('Enter Password ', type="password")
    
    if passwd == st.secrets['psd2']:

        def write_file(text, filename, extension):
            full_filename = filename + "." + extension
            if os.path.exists(full_filename):
                warn = st.warning(f"Warning: File '{full_filename}' already exists.(changes not made)")
                time.sleep(3)
                warn.empty()
                return
            with open(full_filename, "w") as file:
              file.write(text)
            succ = st.success(f"File '{full_filename}' saved successfully.")
            time.sleep(3)
            succ.empty()

        def save_to_github(text, filename, extension, repo_name, access_token):
            g = Github(access_token)
            user = g.get_user()
            repo = user.get_repo(repo_name)
            file_content = text
            try:
                # Check if the file already exists
                try:
                    repo.get_contents(filename + "." + extension)
                    raise FileExistsError(f"File '{filename}.{extension}' already exists in repository '{repo_name}'.")
                except Exception as e:
                    if isinstance(e, GithubException) and e.status == 404:
                        repo.create_file(filename + "." + extension, f"Created {filename}.{extension}", file_content)
                        st.success(f"File '{filename}.{extension}' saved to GitHub repository '{repo_name}' successfully.")
                    else:
                        raise e
            except Exception as e:
                st.error(f"An error occurred while saving to GitHub: {e}")
        
        with st.form("form"):
            x,y = st.columns(2)
            fname = x.text_input('enter Filename')
            ext = y.selectbox('select Extension',('txt','py','cpp','java','json','js','html','css','bat','c','kt'))
            text2 = st.text_area('Enter File Contents')
            button_save = st.form_submit_button('Save')

        if button_save and fname != '' and text2 != '':
            write_file(text2,fname,ext)
            
        elif button_save:
            er = st.error('above fields are mandatory')
            time.sleep(3)
            er.empty()

    elif passwd != st.secrets["psd2"] and passwd != '':
        st.error('wrong person !!')

elif selection == "Python Compiler":
    st.header(f"🐍Mini Python Compiler {py_version}")
    code = st.text_area("Enter your Python code: (currently it doesn't support inputs)")
    input_code = st.text_input('input for code')
    run_button  = st.button("RUN")
    if code and run_button:
        with open("temp_code.py", "w") as f:
            f.write(code)
        output = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True).stdout
        st.subheader(output)

elif selection == "music player":
    def get_audio_files(directory):
        audio_files = [file for file in os.listdir(directory) if file.endswith(('.mp3', '.wav'))]
        return audio_files
    st.title("🎵Music Player")
    uploaded_audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
    # Select an audio file
    audio_files = get_audio_files('songs-for-test')
    selected_audio_file = st.selectbox("Select an audio file", [""] + audio_files)
    if uploaded_audio_file is not None:
        audio_bytes = uploaded_audio_file.read()
        st.audio(audio_bytes, format='audio/' + uploaded_audio_file.type.split('/')[-1])
    elif selected_audio_file:
        audio_path = os.path.join('songs-for-test', selected_audio_file)
        st.audio(audio_path, format='audio/' + selected_audio_file.split('.')[-1])

elif selection == "Translator":
    def translate_text(text, target_language='en'):
        translator = Translator()
        translated_text = translator.translate(text, dest=target_language)
        return translated_text.text
    st.title("Language Translator")
    source_text = st.text_area("Enter Text")
    target_language = st.selectbox('Select Language', ('English', 'Hindi', 'Marathi', 'Urdu', 'Arabic'))
    if source_text != "":
        if target_language == 'Marathi': target_language = 'mr'
        translated_text = translate_text(source_text, target_language.lower()[:2])
        st.write(f"**Translated text ({target_language}):**")
        st.markdown(translated_text)

elif selection == 'CLI':
    cmd_command = st.text_input('Enter Command')
    cmd_button = st.button('execute')
    os_name = platform.system()
    os_release = platform.release()
    st.text(os_name)
    st.text(os_release)
    if cmd_button and cmd_command:
        try:
            output = subprocess.check_output(cmd_command, shell=True)
            output_str = output.decode('utf-8')
            st.write(output_str)
        except subprocess.CalledProcessError as e:
            print("Error executing command:", e)
            st.warning(e)

elif selection == 'Gallery':
    def list_images():
        current_directory = os.getcwd()
        files = os.listdir(current_directory)
        image_files = [file for file in files if file.endswith(('png', 'jpg', 'jpeg', 'gif'))]
        return image_files
    st.title(":blue[Image Gallery]")
    image_files = list_images()
    if not image_files:
        st.write("No images found in the current directory.")
    else:
        for image_file in image_files:
            try:
                st.image(image_file, caption=image_file, use_column_width=True)
            except Exception as e:
                st.write("")

elif selection == 'Cloud Storage':
    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    def get_available_files():
        files = []
        for filename in os.listdir(uploads_dir):
            files.append(filename)
        return files
    def upload_file():
        uploaded_file = st.file_uploader("Choose a file to upload")
        if uploaded_file is not None:
            filepath = os.path.join(uploads_dir, uploaded_file.name)
            with open(filepath, "wb") as f:
                f.write(uploaded_file.read())
            st.success("File uploaded successfully!")

    def download_file(filename):
        filepath = os.path.join(uploads_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                content = f.read()
            return content
        else:
            st.error(f"File '{filename}' not found")

    st.subheader("Packages")
    st.text("Upload Files")
    st.info('under development :/')
    upload_file()

    st.subheader("Download Files")
    available_files = get_available_files()
    if available_files:
        for filename in available_files:
            file_data = download_file(filename)
            if file_data is not None:
                st.download_button(label=filename, data=file_data, file_name=filename)
    else:
        # st.info("No files uploaded yet!")
        pass

elif selection == 'add images':
    def save_captured_photo(uploaded_file):
        filename = f"FromWeb_{int(time.time())}.jpg"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "wb") as buffer:
            buffer.write(uploaded_file.getvalue())
        st.success(f"Image saved successfully as '{filepath}'.")
    uploaded_files = st.file_uploader("Upload multiple photos", accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            save_captured_photo(uploaded_file)
    on = st.toggle('Open Camera')
    if on:
        captured_photo = st.camera_input(":red[OR Take a picture]")
        upload = st.button('upload')
        if captured_photo is not None and upload:
            save_captured_photo(captured_photo)

else:
    st.header(':yellow[something went wrong]')
    st.header(":yellow[You're not supposed to see this Page]")