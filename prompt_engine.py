STYLES = {
    "None": "",
    "Cinematic": "epic cinematic film still, dramatic Rembrandt lighting, anamorphic lens, shallow depth of field",
    "Photoreal": "photorealistic, natural light, shot on a 35mm lens, true-to-life textures",
    "Anime": "anime style, crisp line art, detailed digital illustration",
    "Cyberpunk": "cyberpunk, rain-soaked streets, vibrant neon glow, moody atmosphere",
    "Fantasy": "whimsical high-fantasy movie frame, soft volumetric lighting",
    "3D": "stylized 3D render, cel-shading, vibrant palette with a gritty post-apocalyptic sci-fi edge",
    "Editorial": "high-fashion editorial photograph, studio strobe, bold composition",
}

# Diffusion models respond to keyword tags; OpenAI models prefer plain sentences.
SD_QUALITY_TAGS = "ultra detailed, high quality, sharp focus"

DEFAULT_NEGATIVE = "blurry, low quality, deformed, extra fingers, watermark, text, jpeg artifacts"


def enhance_prompt(text: str, style: str, provider: str) -> str:
    text = text.strip().rstrip(",.")
    style_text = STYLES.get(style, "")

    if provider == "local":
        parts = [text, style_text, SD_QUALITY_TAGS]
        return ", ".join(p for p in parts if p)

    if not style_text:
        return text
    return f"{text}. Visual style: {style_text}."
