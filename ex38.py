# batch_file_rename.py
# Created: 6th August 2012

"""
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
一旦传递了当前和新的扩展，此批处理将重命名给定目录中的一组文件。
"""

# just checking
__author__ = 'Craig Richards'
__version__ = '1.0'
#导入os模块
import os
#导入argparse模块
import argparse


def batch_rename(work_dir, old_ext, new_ext):
    """
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    一旦传递了当前和新的扩展，此批处理将重命名给定目录中的一组文件。
    """
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # Get the file extension
        # 获取文件扩展名
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        # 开始检查文件扩展名的逻辑，if old_ext = file_ext
        if old_ext == file_ext:
            # Returns changed name of the file with new extention
            newfile = split_file[0] + new_ext

            # Write the files
            # 写文件
            # print(os.rename('c.txt','a.txt'))#修改文件名称
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser


def main():

    #This will be called if the script is directly invoked.
    #如果直接调用脚本，将调用此函数
    # adding command line argument
    # 添加命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable work_dir with the first argument passed
    # 用传递的第一个参数设置变量new_ext
    work_dir = args['work_dir'][0]
    # Set the variable old_ext with the second argument passed
    # 用传递的第二个参数设置变量new_ext
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    # Set the variable new_ext with the third argument passed
    # 用传递的第三个参数设置变量new_ext
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)

#当.py文件被直接运行时，if __name__ ==__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__ == '__main__':
    main()