import pdfplumber
from gtts import gTTS
from pathlib import Path
from art import tprint


def pdf_to_mp3(path, lang='en'):
    if Path(path).is_file() and Path(path).suffix == '.pdf':
        print(f'Original pdf file is {Path(path).name}')
        print('Processing...')
        with pdfplumber.PDF(open(path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages).replace('\n', '')

        audio = gTTS(text=text, lang=lang)
        file_name = Path(path).stem
        audio.save(f'{file_name}.mp3')
        return f'Your "{file_name}.mp3" is done'
    else:
        return 'File is not PDF'


def main():
    tprint('PDF TO MP3', font='chunky')
    path = input('Please enter filepath to your file: ')
    lang = input('Please enter required language. For example "en" ')
    print(pdf_to_mp3(path, lang=lang))


if __name__ == '__main__':
    main()
