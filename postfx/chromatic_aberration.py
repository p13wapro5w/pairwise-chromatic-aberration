"""第 58 批：广角镜头快速摇过霓虹招牌时，画面边缘红蓝分开，停下来彩边还挂在灯..."""

def offset_for_focal(focal, base):
    """按焦距返回色差偏移。"""
    raise NotImplementedError("TODO: offset_for_focal")

def apply_order(first, second):
    """返回后处理顺序。"""
    raise NotImplementedError("TODO: apply_order")

def clamp_uv(u):
    """把 UV 夹到屏幕内。"""
    raise NotImplementedError("TODO: clamp_uv")

def luma_weight(value):
    """返回亮度权重。"""
    raise NotImplementedError("TODO: luma_weight")

def exclude_ui(layer):
    """判断是否排除 UI。"""
    raise NotImplementedError("TODO: exclude_ui")

def scale_radius(radius, width, base_width):
    """按分辨率缩放半径。"""
    raise NotImplementedError("TODO: scale_radius")

def temporal_scale(speed, base):
    """按运动缩放色差。"""
    raise NotImplementedError("TODO: temporal_scale")

def channel_offset(channel, offset):
    """返回单通道偏移。"""
    raise NotImplementedError("TODO: channel_offset")

def animate_param(value, frame_delta):
    """按帧推进参数。"""
    raise NotImplementedError("TODO: animate_param")

def half_float_clamp(value):
    """半精度上限夹取。"""
    raise NotImplementedError("TODO: half_float_clamp")
