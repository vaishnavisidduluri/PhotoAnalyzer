def generate_suggestions(brightness, sharpness, contrast, saturation):
    """Generate suggestions based on image analysis results."""
    suggestions = []

    # Brightness suggestions
    if brightness < 50:
        suggestions.append("The image is too dark. Consider increasing the brightness.")
    elif brightness > 200:
        suggestions.append("The image is too bright. Consider decreasing the brightness.")

    # Sharpness suggestions
    if sharpness < 100:
        suggestions.append("The image is not sharp enough. Consider using sharpening filters.")
    elif sharpness > 300:
        suggestions.append("The image is overly sharp. Consider reducing sharpness.")

    # Contrast suggestions
    if contrast < 50:
        suggestions.append("The image has low contrast. Consider increasing contrast.")
    elif contrast > 150:
        suggestions.append("The image has high contrast. Consider reducing contrast.")

    # Saturation suggestions
    if saturation < 50:
        suggestions.append("The image is desaturated. Consider increasing saturation.")
    elif saturation > 200:
        suggestions.append("The image is oversaturated. Consider reducing saturation.")

    # Return the suggestions
    return suggestions 
