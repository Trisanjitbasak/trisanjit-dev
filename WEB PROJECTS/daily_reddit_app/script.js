document.addEventListener('DOMContentLoaded', function() {
    const links = {
        java: document.getElementById('java-link'),
        python: document.getElementById('python-link'),
        c: document.getElementById('c-link'),
        ai: document.getElementById('ai-link'),
        robotics: document.getElementById('robotics-link'),
        problems: document.getElementById('problems-link')
    };

    const containers = {
        java: document.getElementById('java-news'),
        python: document.getElementById('python-news'),
        c: document.getElementById('c-news'),
        ai: document.getElementById('ai-news'),
        robotics: document.getElementById('robotics-news'),
        problems: document.getElementById('problems-news')
    };

    const showContainer = (container) => {
        container.classList.add('active');
    };

    const hideContainers = () => {
        Object.values(containers).forEach(container => {
            container.classList.remove('active');
        });
    };

    const activateLink = (activeLink) => {
        Object.values(links).forEach(link => {
            link.classList.remove('active');
        });
        activeLink.classList.add('active');
    };

    const showPopup = (title, description, url) => {
        const popup = document.createElement('div');
        popup.classList.add('popup');

        // Strip HTML tags from description
        const strippedDescription = description.replace(/<[^>]*>?/gm, '');

        popup.innerHTML = `
            <div class="popup-content">
                <span class="close" onclick="closePopup()">&times;</span>
                <h2>${title}</h2>
                <p>${strippedDescription}</p>
                <div class="popup-buttons">
                    <a href="${url}" class="redirect-btn" target="_blank">View on Original Site</a>
                    <button class="close-btn">Close</button>
                </div>
            </div>
        `;
        document.body.appendChild(popup);

        const closeButton = popup.querySelector('.close-btn');
        closeButton.addEventListener('click', closePopup);
    };

    const closePopup = () => {
        const popup = document.querySelector('.popup');
        if (popup) {
            popup.remove();
        }
    };

    links.java.addEventListener('click', () => {
        hideContainers();
        showContainer(containers.java);
        activateLink(links.java);
    });

    links.python.addEventListener('click', () => {
        hideContainers();
        showContainer(containers.python);
        activateLink(links.python);
    });

    links.c.addEventListener('click', () => {
        hideContainers();
        showContainer(containers.c);
        activateLink(links.c);
    });

    links.ai.addEventListener('click', () => {
        hideContainers();
        showContainer(containers.ai);
        activateLink(links.ai);
    });

    links.robotics.addEventListener('click', () => {
        hideContainers();
        showContainer(containers.robotics);
        activateLink(links.robotics);
    });

    links.problems.addEventListener('click', () => {
        hideContainers();
        showContainer(containers.problems);
        activateLink(links.problems);
    });

    const fetchNews = async (topic, containerId) => {
        try {
            const response = await fetch(`https://www.reddit.com/r/${topic}.json`);
            const data = await response.json();
            const posts = data.data.children;

            const newsContainer = document.getElementById(containerId);
            newsContainer.innerHTML = '';

            posts.forEach(post => {
                const title = post.data.title;
                const description = post.data.selftext; // Get the description
                const url = post.data.url;

                const newsItem = document.createElement('div');
                newsItem.classList.add('news-item');
                newsItem.innerHTML = `
                    <h2>${title}</h2>
                `;
                newsItem.addEventListener('click', (event) => {
                    event.preventDefault(); // Prevent default link behavior
                    showPopup(title, description, url);
                });

                newsContainer.appendChild(newsItem);
            });
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    fetchNews('java', 'java-news');
    fetchNews('python', 'python-news');
    fetchNews('c_programming', 'c-news');
    fetchNews('artificial', 'ai-news');
    fetchNews('robotics', 'robotics-news');

    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const searchResults = document.getElementById('search-results');

    searchButton.addEventListener('click', async () => {
        const query = searchInput.value.trim();
        if (query) {
            searchResults.innerHTML = 'Searching...';
            try {
                const redditResults = await fetch(`https://www.reddit.com/search.json?q=${query}`);
                const redditData = await redditResults.json();
                const redditPosts = redditData.data.children;

                searchResults.innerHTML = '<h2>Results from Reddit:</h2>';
                redditPosts.forEach(post => {
                    const title = post.data.title;
                    const description = post.data.selftext;
                    const url = post.data.url;

                    const resultItem = document.createElement('div');
                    resultItem.classList.add('news-item');
                    resultItem.innerHTML = `
                        <h2>${title}</h2>
                    `;
                    resultItem.addEventListener('click', (event) => {
                        event.preventDefault();
                        showPopup(title, description, url);
                    });

                    searchResults.appendChild(resultItem);
                });

                const stackOverflowResults = await fetch(`https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&q=${query}&site=stackoverflow`);
                const stackOverflowData = await stackOverflowResults.json();
                const stackOverflowPosts = stackOverflowData.items;

                searchResults.innerHTML += '<h2>Results from StackOverflow:</h2>';
                stackOverflowPosts.forEach(post => {
                    const title = post.title;
                    const description = post.body;
                    const url = post.link;

                    const resultItem = document.createElement('div');
                    resultItem.classList.add('news-item');
                    resultItem.innerHTML = `
                        <h2>${title}</h2>
                    `;
                    resultItem.addEventListener('click', (event) => {
                        event.preventDefault();
                        showPopup(title, description, url);
                    });

                    searchResults.appendChild(resultItem);
                });

                // Quora scraping
                const quoraResults = await fetch(`https://www.quora.com/search?q=${encodeURIComponent(query)}`);
                const quoraText = await quoraResults.text();
                const quoraParser = new DOMParser();
                const quoraDoc = quoraParser.parseFromString(quoraText, 'text/html');
                const quoraItems = quoraDoc.querySelectorAll('.q-box .q-box.qu-mb--tiny.qu-mr--tiny .q-box .q-box');

                searchResults.innerHTML += '<h2>Results from Quora:</h2>';
                quoraItems.forEach(item => {
                    const titleElement = item.querySelector('.q-box .q-box a');
                    if (titleElement) {
                        const title = titleElement.innerText;
                        const url = `https://www.quora.com${titleElement.getAttribute('href')}`;

                        const resultItem = document.createElement('div');
                        resultItem.classList.add('news-item');
                        resultItem.innerHTML = `
                            <h2>${title}</h2>
                        `;
                        resultItem.addEventListener('click', (event) => {
                            event.preventDefault();
                            showPopup(title, '', url);
                        });

                        searchResults.appendChild(resultItem);
                    }
                });

            } catch (error) {
                console.error('Error searching:', error);
                searchResults.innerHTML = 'Error fetching search results.';
            }

            // Set default view to Java news
    showContainer(javaContainer);
    hideContainers([pythonContainer, cContainer, aiContainer, roboticsContainer]);
        }
    });
});
