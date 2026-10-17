import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def reorganize() :
    # 选择要整理的文件夹
    selected_folder = filedialog.askdirectory(
        title="欢迎来到文件整理器，请选择要整理的文件夹~"
    )
    # 如果用户取消选择，就结束程序
    if not selected_folder:
        messagebox.showerror("自动整理文件夹","未选择文件夹,请重新选择！")
        return
    # 主目录
    cwd = Path(selected_folder)
    # 根据后缀 -> 分类文件夹
    file_types = {
        # 文档
        '.txt': '文档',
        '.pdf': '文档',
        '.doc': '文档',
        '.docx': '文档',
        '.csv': '文档',
        '.xls': '文档',
        '.xlsx': '文档',
        '.ppt': '文档',
        '.pptx': '文档',
        '.md': '文档',
        '.rtf': '文档',
        '.json': '文档',
        '.xml': '文档',
        '.html': '文档',
        '.htm': '文档',
        '.log': '文档',

        # 照片
        '.png': '照片',
        '.jpg': '照片',
        '.jpeg': '照片',
        '.gif': '照片',
        '.bmp': '照片',
        '.webp': '照片',
        '.tif': '照片',
        '.tiff': '照片',
        '.ico': '照片',
        '.svg': '照片',
        '.heic': '照片',

        # 音频
        '.mp3': '音频',
        '.wav': '音频',
        '.flac': '音频',
        '.aac': '音频',
        '.m4a': '音频',
        '.ogg': '音频',
        '.wma': '音频',
        '.opus': '音频',

        # 视频
        '.mp4': '视频',
        '.avi': '视频',
        '.mkv': '视频',
        '.mov': '视频',
        '.wmv': '视频',
        '.flv': '视频',
        '.webm': '视频',
        '.m4v': '视频',
        '.mpeg': '视频',
        '.mpg': '视频',

        # 压缩包
        '.zip': '压缩',
        '.rar': '压缩',
        '.7z': '压缩',
        '.tar': '压缩',
        '.gz': '压缩',
        '.bz2': '压缩',
        '.xz': '压缩',
        '.tgz': '压缩',

        # 程序 / 安装包
        '.exe': '程序',
        '.msi': '程序',
        '.bat': '程序',
        '.cmd': '程序',
        '.com': '程序',
        '.apk': '程序',
        '.appx': '程序',
        '.msix': '程序',
        '.deb': '程序',
        '.rpm': '程序',

        # 代码
        '.py': '代码',
        '.pyw': '代码',
        '.js': '代码',
        '.jsx': '代码',
        '.tsx': '代码',
        '.css': '代码',
        '.scss': '代码',
        '.java': '代码',
        '.c': '代码',
        '.h': '代码',
        '.cpp': '代码',
        '.hpp': '代码',
        '.cs': '代码',
        '.go': '代码',
        '.rs': '代码',
        '.php': '代码',
        '.vue': '代码',
        '.sql': '代码',
        '.sh': '代码',
        '.ps1': '代码',

        # 字体
        '.ttf': '字体',
        '.otf': '字体',
        '.woff': '字体',
        '.woff2': '字体',

        # 电子书
        '.epub': '电子书',
        '.mobi': '电子书',
        '.azw': '电子书',
        '.azw3': '电子书',

        # 数据 / 数据库
        '.db': '数据',
        '.sqlite': '数据',
        '.sqlite3': '数据',
        '.bak': '备份',

    }
    for file in cwd.iterdir():
        if file.is_file():
            suffix = file.suffix.lower()
            # 获取分类文件夹名称，未知类型统一放到 unknown
            category_name = file_types.get(suffix, '未知')
            category = cwd / category_name
            # 如果目录不存在就创建
            category.mkdir(exist_ok=True)
            # 移动文件
            category_file_name = category / file.name
            # 重复文件跳过
            if not category_file_name.exists():
                shutil.move(file, category_file_name)
            else:
                messagebox.showwarning("自动整理文件夹",f"{category_name}文件夹内已存在{file.name}文件,未进行处理~")
                continue
             # 输入提示
    messagebox.showinfo("自动整理文件夹", "已整理完成！")

# 图形化界面
root = tk.Tk()
root.title('自动整理文件夹')
# 图标
# root.iconbitmap('icon.ico')
# 实现屏幕居中
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_width = 500
root_height = 300
width = int((screen_width-root_width)/2)
height = int((screen_height-root_height)/2)
root.geometry(f'{root_width}x{root_height}+{width}+{height}')
# 布局
top_frame = tk.Frame(root,bg="#fff")
top_frame.pack(side='top',fill="x")
bottom_frame = tk.Frame(root, bg="#fff")
bottom_frame.pack(side='bottom',fill="x")
# 标题
label = tk.Label(top_frame,text="欢迎使用我的自动整理文件夹程序，这是一个简单的小程序~",font=("宋体",20),height=4,justify="center",wraplength=450,bg="#fff")
label.pack(padx=10, pady=20)
# 按钮
button = tk.Button(bottom_frame, text="请选择文件夹",font=("宋体",16),height=2)
button.pack(pady=50)
button.config(command=reorganize)
root.mainloop()

