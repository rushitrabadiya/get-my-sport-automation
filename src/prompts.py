def build_prompt(content):
    prompt = f"""
    You are an expert Instagram content creator and caption strategist.
    Based on the provided {content}, generate a high-performing Instagram post package including:
        1. A catchy caption: Write an engaging, scroll-stopping caption that fits the tone and theme of the provided content. Use storytelling, emojis, and a clear call to action (CTA) if appropriate.
        2. Relevant hashtags: Provide a list of 10-15 hashtags that are optimized for engagement and reach. Mix broad, niche, and branded hashtags related to the topic.
        3. A detailed image generation prompt: Create a creative, descriptive prompt for AI image generation that visually represents the post.

    Image prompt guidelines: 
    - A good prompt is descriptive and clear, and makes use of meaningful keywords and modifiers. Start by thinking of your subject, context, and style. 
        1. Subject: The first thing to think about with any prompt is the subject: the object, person, animal, or scenery you want an image of. 
        2. Context and background: Just as important is the background or context in which the subject will be placed. Try placing your subject in a variety of backgrounds. For example, a studio with a white background, outdoors, or indoor environments. 
        3. Style: Finally, add the style of image you want. Styles can be general (painting, photograph, sketches) or very specific (pastel painting, charcoal drawing, isometric 3D). You can also combine styles. 
    
    - Models can add text into images, opening up more creative image generation possibilities. 
    Use the following guidance to get the most out of this feature: 
        1. Iterate with confidence: You might have to regenerate images until you achieve the look you want. Text integration is still evolving, and sometimes multiple attempts yield the best results. 
        2. Keep it short: Limit text to 25 characters or less for optimal generation.
        3. Multiple phrases: Experiment with two or three distinct phrases to provide additional information. Avoid exceeding three phrases for cleaner compositions. 
        4. Guide Placement: While Imagen can attempt to position text as directed, expect occasional variations. This feature is continually improving. 
        5. Inspire font style: Specify a general font style to subtly influence Imagen's choices. Don't rely on precise font replication, but expect creative interpretations. 
        6. Font size: Specify a font size or a general indication of size (for example, small, medium, large) to influence the font size generation.

    Output Format
    Return the final output strictly in JSON format:
    {{
        "caption": "string",
        "hashtags": ["string"],
        "image_prompt": "string"
    }}
    """
    return prompt
