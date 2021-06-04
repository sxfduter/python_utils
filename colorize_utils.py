def colorize_mask(label, palette):
    """
    将label以类别对应颜色保存成彩色图。
    :param label:[512,1024]
    :param palette:[19*3] eg.:[0, 0, 0, 128, 0, 0,... 0, 128, 0]
    """
    zero_pad = 256 * 3 - len(palette)
    for i in range(zero_pad):
        palette.append(0)
    new_mask = PIL.Image.fromarray(mask.astype(np.uint8)).convert('P')
    new_mask.putpalette(palette)
    return new_mask
def blend_image(self, image, label, palette):
    """
    将label值以对应颜色的形式与image，以指定透明度混合。
    :param image:[512, 1024, 3]
    :param label:[512, 1024]
    :param palette:[19, 3]
    """
    mask = palette[label] #将单通道label转成三通道mask:[512,1024,3]
    mask = Image.fromarray(np.uint8(mask))
    blend_image = Image.blend(image, mask, 0.4)
    blend_image.save('./blend_image.png')
