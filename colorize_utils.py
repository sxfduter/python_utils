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
