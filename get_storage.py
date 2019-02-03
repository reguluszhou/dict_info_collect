# 查询指定目录的大小

import os
import time
start = time.time()




root_dict = {}



def storage_size(path, folder_name):
    '''
    :param path: given a path
    :param folder_name: folder_name
    :return: size of path for certain folder_name
    '''
    size = 0


    for root, dirs, files in os.walk(path):
        for name in files:
            size += os.path.getsize(os.path.join(root, name))

    size = ('%.3f GB' % (size/1024/1024/1024))




    folder_stat = "%s#%s" %(folder_name, size)
    print(folder_stat)
    return folder_stat


def dict_storage(path):
    '''
    :param path: given a root path
    :return: form a dictionary of dictionary shows size of each anime
    '''

    alpha_root_list = os.listdir(path)


    #次一级文件夹A-Z
    for alpha in alpha_root_list:
        alpha_root = os.path.join(path, alpha)
        if os.path.isfile(alpha_root):
            continue
        else:
            anime_root_list = os.listdir(alpha_root)
            current_anime_list = []

            for anime_folder in anime_root_list:

                #空文件直接计算
                if anime_folder == []:
                    root_dict[exec(alpha)] = {'emtpy': 0}

                else:

                    #计算动画文件夹大小
                    anime_root = os.path.join(alpha_root, anime_folder)
                    current_anime_list.append(storage_size(anime_root, anime_folder))

                # 把list append到dictionary value上
        root_dict[alpha] = current_anime_list




def storage_info_write(dict_in_str):
    '''
    :param path: give a dict in string
    :return: write info down
    '''

    #folder_info = input(r'Anime folders are: ') + '.txt'
    #txt_path = os.path.join(r'C:\Users\regul\Desktop', folder_info)
    #write_info = open(r'C:\Users\regul\Desktop\D-L.txt修改地址', 'w+', encoding='utf8', errors='ignore')
    write_info.write(dict_in_str)
    write_info.close()




#输入地址path = r'\\192.168.50.87\517-1\动漫'
dict_storage(path)

root_dict = str(root_dict)
storage_info_write(root_dict)


end = time.time()
print("process is  %2f sec" %(end - start))
