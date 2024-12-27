document.addEventListener('DOMContentLoaded', () => {
    const pentagram = document.getElementById('pentagram');
    const subtopicsDiv = document.getElementById('subtopics');
    const contentDiv = document.getElementById('content');

    // Position the points of the pentagram
    const points = document.querySelectorAll('.point');
    points.forEach((point, index) => {
        const angle = (index * 72 - 90) * Math.PI / 180;
        const x = 50 + 40 * Math.cos(angle);
        const y = 50 + 40 * Math.sin(angle);
        point.style.left = `${x}%`;
        point.style.top = `${y}%`;
    });

    pentagram.addEventListener('click', (event) => {
        const point = event.target.closest('.point');
        if (point) {
            const topic = point.dataset.topic;
            fetch(`/subtopics/${topic}`)
                .then(response => response.json())
                .then(subtopics => {
                    subtopicsDiv.innerHTML = '';
                    subtopics.forEach(subtopic => {
                        const subtopicBtn = document.createElement('button');
                        subtopicBtn.textContent = subtopic;
                        subtopicBtn.addEventListener('click', () => {
                            fetch(`/content/${topic}/${subtopic}`)
                                .then(response => response.json())
                                .then(data => {
                                    contentDiv.innerHTML = `<h2>${subtopic}</h2><p>${data.content}</p>`;
                                });
                        });
                        subtopicsDiv.appendChild(subtopicBtn);
                    });
                });
        }
    });
}); 