styles = {
    "Cinematic":
        "Epic cinematic movie scene, dramatic Rembrandt lighting, ",

    "Anime":
        "Anime style, digital and detailed illustration",

    "Cyberpunk":
        "Cinematic anime cyberpunk style, vibrant neon glow",

    "Fantasy":
        "Whimsical high-fantasy movie frame, soft volumetric lighting",

    "3D":
        "cel-shading, vibrant color palettes combined with a gritty, post-apocalyptic sci-fi"
}


def enhance_prompt(text, style):

    return f"""
    {text},
    {styles[style]},
    ultra detailed,
    high quality,
    8k
    """