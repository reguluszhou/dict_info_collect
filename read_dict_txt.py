import os
import re
import pprint


dict_in_str = ''

def storage_info_write(dict_in_str):
    '''
    :param path: give a dict in string
    :return: write info down
    '''

    folder_info = input(r'Anime folders are: ') + '.txt'
    txt_path = os.path.join(r'C:\Users\regul\Desktop', folder_info)
    write_info = open(txt_path, 'w+', encoding='utf8', errors='ignore')
    write_info.write(dict_in_str)
    write_info.close()



def storage_info_read(txt_path):
    '''
    :param txt: given a path of dictionary info in str in txt
    :return: dictionary in string
    '''
    global dict_in_str
    read_info = open(txt_path, 'r', encoding='utf-8', errors='ignore')
    dict_in_str = read_info.read()
    read_info.close()
    return dict_in_str



storage_info_read(r'C:\Users\regul\Desktop\D-L.txt')


def search_anime(name):
    '''
    :param name: name of anime
    :return: which folder is in and what size of the anime
    '''
    root = dict_in_str
    start = root[:root.find(name)].rfind('\'') + 1
    end = root[start:].find('GB') + 2
    folder_in = root[:start].rfind(":") - 2
    list_info = [root[:start][folder_in], root[start:][:end]]
    return print(list_info)




def storage_info_size(dict):
    '''
    :param dict in str
    :return: info for anime folder
    '''
    #转换
    folder_dict = eval(dict_in_str)

    #查询数据
    for key, value in folder_dict.items():
        size = 0
        for anime in value:
            size_start = anime.find("#") + 1
            size_end = anime.find('GB') - 2
            size += float(anime[size_start:size_end])
        print('size of Folder %s is %3f' % (key, size))



search_anime(r'第一神拳')
storage_info_size(dict_in_str)