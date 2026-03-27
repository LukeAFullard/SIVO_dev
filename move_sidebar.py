with open('src/sivo/templates/dashboards/sidebar_right.html', 'r') as f:
    content = f.read()

sidebar_start = content.find('<!-- Right Sidebar Slot -->')
sidebar_end = content.find('<!-- Main Content Slot -->')

main_start = content.find('<!-- Main Content Slot -->')
main_end = content.find('    </div>\n\n    <!-- Global Sliding Sidebar Overlay -->')

if sidebar_start != -1 and sidebar_end != -1 and main_start != -1 and main_end != -1:
    sidebar = content[sidebar_start:sidebar_end]
    main = content[main_start:main_end]

    before = content[:sidebar_start]
    after = content[main_end:]

    new_content = before + main + sidebar + after

    with open('src/sivo/templates/dashboards/sidebar_right.html', 'w') as f:
        f.write(new_content)
    print("Done")
else:
    print("Failed to find sections")
