import os,shutil

dict_extensions={
    'audio_extensions':('.mp3','.mp4a','.wav','.flac'),
    'videos_extensions':('.mp4','.mkv','.MKV','.flv','.mprg'),
    'documents_extensions':('.doc','.pdf','.txt'),
    'images_extensions':('.jpg'),
}


folderpath=input('Enter folder path : ')

def file_finder(folder_path,file_extensions):
    files=[]
    for file in os.listdir(folder_path):
         for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

#print(file_finder(folderpath,videos_extensions))

for extension_type,extension_tuple in dict_extensions.items():
    folder_name=extension_type.split('_')[0]+'Files'
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in(file_finder(folderpath,extension_tuple)):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
    #print('Calling file finder')
    #print(file_finder(folderpath,extension_tuple))