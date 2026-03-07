with open("src/sivo/runtime/templates/echarts.html", "r") as f:
    content = f.read()

import re

search = r"""                        if \(action\.provider === 'twitter' \|\| action\.provider === 'x'\) \{
                            // Official Twitter embed URL structure
                            const tweetIdMatch = action\.url\.match\(/status\\/\(\\d\+\)/\);
                            if \(tweetIdMatch && tweetIdMatch\[1\]\) \{
                                iframe\.src = `https://platform\.twitter\.com/embed/Tweet\.html\?id=\$\{tweetIdMatch\[1\]\}`;
                            \} else \{
                                iframe\.src = action\.url;
                            \}"""

replacement = """                        if (action.provider === 'twitter' || action.provider === 'x') {
                            // Twitter has deprecated direct iframe URL embeds. Instead, we use their standard blockquote widget integration.
                            // We construct the elements via DOM API to bypass DOMPurify so they're safe but functional.
                            validSocial = false; // We don't use the default generic iframe logic for Twitter

                            var tweetContainer = document.createElement('div');
                            tweetContainer.className = 'twitter-embed-container';
                            tweetContainer.style.width = '100%';
                            tweetContainer.style.display = 'flex';
                            tweetContainer.style.justifyContent = 'center';

                            var blockquote = document.createElement('blockquote');
                            blockquote.className = 'twitter-tweet';
                            blockquote.setAttribute('data-theme', 'light');

                            var link = document.createElement('a');
                            link.href = action.url;
                            blockquote.appendChild(link);

                            var script = document.createElement('script');
                            script.async = true;
                            script.src = 'https://platform.twitter.com/widgets.js';
                            script.charset = 'utf-8';

                            tweetContainer.appendChild(blockquote);
                            tweetContainer.appendChild(script);

                            // It's technically a container, not just an iframe, but appending works identically
                            socialIframes.push(tweetContainer);"""

content = re.sub(search, replacement, content)
with open("src/sivo/runtime/templates/echarts.html", "w") as f:
    f.write(content)
