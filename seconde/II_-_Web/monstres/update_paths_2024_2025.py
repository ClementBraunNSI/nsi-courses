import re

# Read the markdown file
with open('/Users/clementbraun/nsi-courses/docs/seconde/II_-_Web/monstres.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Update image paths to include 2024_2025 folder
# Replace ./monstres/ with ./monstres/2024_2025/
content = re.sub(r'(\!\[.*?\]\(\./monstres/)([^/]+/)', r'\g<1>2024_2025/\g<2>', content)

# Write the updated content back to the file
with open('/Users/clementbraun/nsi-courses/docs/seconde/II_-_Web/monstres.md', 'w', encoding='utf-8') as file:
    file.write(content)

print('Successfully updated all image paths to include 2024_2025 folder')

# Count the number of updated links
updated_count = len(re.findall(r'\!\[.*?\]\(\./monstres/2024_2025/', content))
print(f'Total updated links: {updated_count}')