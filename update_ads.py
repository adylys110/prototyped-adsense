import re
from pathlib import Path

pattern = re.compile(
    r"(<div[^>]*class=\"[^\"]*ad-sidebar[^\"]*\"[\s\S]*?<script>\s*atOptions = \{[\s\S]*?)(?:'height'\s*:\s*)90([\s\S]*?)(?:'width'\s*:\s*)728([\s\S]*?</script>)([\s\S]*?</div>)",
    flags=re.IGNORECASE,
)

updated_files = []
for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    new_text = pattern.sub(lambda m: m.group(1) + "'height' : 250" + m.group(2) + "'width' : 300" + m.group(3) + m.group(4), text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        updated_files.append(path.name)

print('updated', updated_files)
