import maya.cmds as mc


def main(is_first=True, are_selected_frames=True, scale_amount=1):
    mc.ls(sl=True)
    anim_curves = mc.keyframe(q=True, sl=True, name=True)
    for anim_curve in anim_curves:
        scale_frames_on_curve(anim_curve, is_first, are_selected_frames, scale_amount)

def scale_frames_on_curve(anim_curve, is_first=True, are_selected_frames=True, scale_amount=1):

    selected_frame_times = mc.keyframe(anim_curve, q=True, sl=True, timeChange=True)
    selected_frame_values = mc.keyframe(anim_curve, q=True, sl=True, valueChange=True)
    all_times = mc.keyframe(anim_curve, q=True, timeChange=True)

    if is_first:
        time_pivot = selected_frame_values[0]
        value_pivot = selected_frame_values[0]
        time_start = selected_frame_times[0]
        time_end = selected_frame_times[-1]
        if not are_selected_frames:
            time_end = all_times[-1]

    else:
        time_pivot = selected_frame_values[-1]
        value_pivot = selected_frame_values[-1]
        time_start = selected_frame_times[-1]
        time_end = selected_frame_times[0]
        if not are_selected_frames:
            time_end = all_times[0]

    mc.scaleKey(anim_curve, time=(time_start, time_end),
                timePivot=time_pivot, valuePivot=value_pivot,
                valueScale=scale_amount)