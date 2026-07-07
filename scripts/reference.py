"""参考图处理：裁剪三张标准尺寸图，白边填充不裁剪内容"""
from PIL import Image
import os

def process_reference_image(input_path, output_dir):
    """处理单张参考图，生成三张标准尺寸图"""
    img = Image.open(input_path).convert('RGB')
    w, h = img.size

    # 1. reference.jpg — 最长边1200px，保持比例
    ratio = min(1200 / w, 1200 / h, 1.0)
    ref = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)
    ref.save(os.path.join(output_dir, 'reference.jpg'), 'JPEG', quality=85, optimize=True)

    # 2. reference_square.jpg — 800×800 白边填充
    def to_square(im, size, bg_color=(255, 255, 255)):
        """等比例缩放并填充白边到正方形，保留全部内容"""
        iw, ih = im.size
        scale = min(size / iw, size / ih)
        nw, nh = int(iw * scale), int(ih * scale)
        resized = im.resize((nw, nh), Image.LANCZOS)
        square = Image.new('RGB', (size, size), bg_color)
        x = (size - nw) // 2
        y = (size - nh) // 2
        square.paste(resized, (x, y))
        return square

    square = to_square(img, 800)
    square.save(os.path.join(output_dir, 'reference_square.jpg'), 'JPEG', quality=85, optimize=True)

    # 3. reference_thumb.jpg — 400×400 白边填充
    thumb = to_square(img, 400)
    thumb.save(os.path.join(output_dir, 'reference_thumb.jpg'), 'JPEG', quality=75, optimize=True)

    print(f"处理完成: {os.path.basename(input_path)}")
    print(f"  reference.jpg: 1200px 保持比例")
    print(f"  reference_square.jpg: 800×800 白边填充")
    print(f"  reference_thumb.jpg: 400×400 白边填充")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("用法: python reference.py <图片路径> [输出目录]")
        sys.exit(1)
    input_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(input_path)
    process_reference_image(input_path, output_dir)
