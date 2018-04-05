def get_google_preview(meta_tags):
    g_preview = []
    g_preview.append(meta_tags.get('og:title'))
    g_preview.append(meta_tags.get('og:url'))
    g_preview.append(meta_tags.get('og:description'))
    return g_preview
