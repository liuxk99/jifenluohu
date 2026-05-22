import os

from matplotlib import font_manager as fm
from matplotlib.font_manager import FontProperties


def get_font_properties() -> FontProperties:
    # 字体-1. 指定你项目目录下的字体文件路径
    # 建议将字体文件放在脚本同级目录下
    font_path = 'SourceHanSansSC-Normal.otf'

    # 字体-2. 注册字体属性
    font_prop = fm.FontProperties(fname=font_path)
    if not os.path.exists(font_path):
        print(f"🛑 严重错误：找不到字体文件 '{font_path}'")
        print("💡 请将字体文件放在和 jifen_plot.py 相同的文件夹中。")
        print("💡 请检查文件名是否拼写错误（注意大小写和后缀 .otf/.ttf）。")
        # 强制退出，防止后续报错
        exit()

    # 加载字体
    try:
        font_prop = fm.FontProperties(fname=font_path)
        print(f"✅ 成功加载字体: {font_path}")
    except Exception as e:
        print(f"❌ 加载字体失败: {e}")
        exit()
    return font_prop
